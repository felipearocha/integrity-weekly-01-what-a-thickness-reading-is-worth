"""Screening correction for ultrasonic thickness readings taken on hot carbon steel.

What it computes
    The wall thickness at calibration temperature from a gauge reading taken on hot
    metal, and the corrosion rate between the first and last survey of one CML, with
    and without that correction.

Standard followed
    API 570, 4th Edition (2016), 5.7.1: above 150 F (65 C), if the procedure does not
    compensate for temperature, readings are to be adjusted by the appropriate
    temperature correction factor. API 510, 11th Edition (2022), 5.7.2.3 asks for
    corrective procedures on vessels. Neither code gives the factor. The one used
    here is the common field
    rule of thumb for carbon steel: the gauge reads about 1% thick for every 55 C
    (100 F) the metal is above the calibration temperature.

Units
    Thickness in mm, temperature in degrees C, rate in mm/yr (loss is positive).

Limits
    Screening only, carbon steel only. The real velocity change depends on the alloy,
    and a qualified high temperature procedure (rated probe and couplant, calibration
    at temperature) governs over this estimate. Readings are synthetic.
"""
surveys = [  # (year, metal temperature C, gauge reading mm), same CML
    (2022, 20, 9.60),   # turnaround, cold
    (2024, 295, 9.94),  # on-stream, hot
    (2026, 295, 9.77),  # on-stream, hot
]
CAL_TEMP_C = 20        # calibration block temperature
K_PER_C = 0.01 / 55    # rule of thumb: reads 1% high per 55 C


def corrected(reading_mm, metal_temp_c):
    excess_c = metal_temp_c - CAL_TEMP_C
    return reading_mm * (1 - K_PER_C * excess_c)


walls = [corrected(mm, temp_c) for _, temp_c, mm in surveys]
for (year, temp_c, mm), wall in zip(surveys, walls):
    print(f"{year} {temp_c:>3} C read {mm:.2f} wall {wall:.2f}")

years = surveys[-1][0] - surveys[0][0]
raw_rate = (surveys[0][2] - surveys[-1][2]) / years
real_rate = (walls[0] - walls[-1]) / years
print(f"rate from raw readings {raw_rate:+.3f} mm/yr")
print(f"rate after correction  {real_rate:+.3f} mm/yr")
assert corrected(9.60, 20) == 9.60                      # no correction at calibration temperature
assert abs(corrected(9.94, 295) - 9.94 * 0.95) < 1e-9   # 275 C excess = 5 x 55 C = 5%
assert abs(walls[1] - 9.443) < 1e-3 and abs(walls[2] - 9.2815) < 1e-3
assert abs(raw_rate - (9.60 - 9.77) / 4) < 1e-12 and raw_rate < 0   # raw readings show growth
assert abs(real_rate - (9.60 - 9.2815) / 4) < 1e-9                   # 0.080 mm/yr
