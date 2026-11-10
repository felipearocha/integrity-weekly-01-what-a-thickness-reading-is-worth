# What a thickness reading is worth

[![CI](https://github.com/felipearocha/integrity-weekly-01-what-a-thickness-reading-is-worth/actions/workflows/ci.yml/badge.svg)](https://github.com/felipearocha/integrity-weekly-01-what-a-thickness-reading-is-worth/actions/workflows/ci.yml)

Week of 2026-11-16 to 2026-11-20. Working notes on one integrity engineering problem: the posts, the code behind the numbers, and tests that hold the code to a hand calculation.

## Run it

```
pip install -r requirements-dev.txt
pytest -q
python code/hot_reading.py
```

Python 3.11 or newer.

## Code

| File | What it computes |
|---|---|
| [`code/hot_reading.py`](code/hot_reading.py) | Screening correction for ultrasonic thickness readings taken on hot carbon steel. |

Each script states its basis in the docstring, runs on synthetic data, and checks its own result against a hand calculation. The tests also confirm the printed output is the one published.

## Posts

| Day | Post | Format |
|---|---|---|
| Monday | [The Reading That Went Up](posts/161_the_reading_that_went_up.md) | text-only |
| Tuesday | [One Elbow, Two Histories](posts/162_one_elbow_two_histories.md) | single image |
| Wednesday | [Eighteen Good Readings and One Thin Spot](posts/163_eighteen_good_readings.md) | single image |
| Thursday | [The Wall Did Not Grow. The Pipe Was Hot.](posts/164_hot_reading_rate.md) | single image |
| Friday | [Before You Replace the Spool, Audit the Reading](posts/165_audit_the_reading.md) | carousel |

## Scope and limits

- All data and drawings are synthetic. No plant, tag or operating data from any facility.
- The code is a worked example for engineers, not a certified calculation. Confirm every requirement against the edition of the standard that governs your equipment.
- Short quotations from standards are identified with their section. Standards are the property of their publishers and are not reproduced here.

## License

MIT for the code. See [LICENSE](LICENSE).
