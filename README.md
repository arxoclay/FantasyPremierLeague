This library has been created to facilitate/foster mathematical approaches of analyzing Fantasy Premier League game weeks.

The high-level design is as follows:
(1) Scrape component - The basic idea is to scrape webpages to collect the raw source data.

(2) Mapping component - Transform the data from (1) into an internal well-defined data model.

(3) Analysis component - Use the data model from (2) in mathematical analyses (Heuristics, machine learning, optimization algorithms etc).

The mapping in (2) should be well defined such that anyone can plugin their own analysis component ((3) in the above given points) and derive useful insights.
Potentially, the results from (2) could also be exposed via a web service in the future.
