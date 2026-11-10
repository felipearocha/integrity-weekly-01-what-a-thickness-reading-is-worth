# The Reading That Went Up

Monday 2026-11-16

A thickness reading that went up is the most honest number in your database. Many programs delete it.

Take a 6 inch naphtha line with 40 CMLs. Between two surveys three years apart, 11 of them read thicker than before, by up to 0.4 mm. Steel does not grow, so the usual clean-up follows: overwrite the new value with the old one, or let the software floor the rate at zero. The record looks tidy and those points report no corrosion.

Here is what was thrown away. Those 11 increases are a free measurement of how repeatable your readings are. If a point can come back 0.4 mm thicker with no metal added, it can come back 0.4 mm thinner with no metal lost.

Now look at another CML on the same line, down 0.3 mm over the same three years. It gets a rate of 0.10 mm/yr, a remaining life and a date. It is the same quality of evidence as the readings that were erased. You cannot believe one and delete the other.

API 570 6.5.4 asks the question as a check before any analysis: "Have data anomalies been resolved, either through a review process or verification readings, prior to data analysis?" Resolved is not the same as removed.

What I do instead:

Keep the raw value. Flag it, never edit it.

Re-shoot the largest increases at the marked point. A jump of several millimetres is usually a replaced spool or the wrong location, and each needs a different fix in the record.

Use the spread of the increases as the noise band for that circuit, and stop reporting rates that sit inside it as if they had been measured.

What does your system do today when a reading comes back thicker than the last one?

## Requirements quoted

> "Have data anomalies been resolved, either through a review process or verification readings, prior to data analysis?"
>
> API 570, 6.5.4

## Note

API 570, 4th Edition (2016), 6.5.4 Data Analysis lists five checks to run on circuit data; the quoted line is item e). The line and the numbers in the post are an illustrative case, not a specific plant.
