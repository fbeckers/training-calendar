# Training Calendar

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This tool extracts training log entries from a macOS Calendar and aggregates them into per-sport, per-discipline statistics.

The pipeline has three steps:
1. Apple Shortcuts reads training log entries from a calendar and writes them to a TXT file
2. Python converts the TXT file to a CSV file
3. DuckDB aggregates the CSV into summary statistics

## Requirements

1. Apple Shortcut named "Training Calendar" [https://www.icloud.com/shortcuts/13341fefe6864565a66232b891734766](https://www.icloud.com/shortcuts/13341fefe6864565a66232b891734766)
2. Python 3 CLI
3. DuckDB CLI

## Usage

```sh
make run    # run full pipeline and print aggregated stats
make clean  # remove generated data directory
```

## Log format

Each line in the exported log follows this pattern:
```
YYYY-MM-DD <sport> <discipline>[ <distance>km]
```
Sport and discipline are single words. Distance is optional and has at most one decimal digit.

## Example

1. Calendar entries

| Date       | Title (-> sport) | Notes (-> discipline & distance) |
|------------|------------------|----------------------------------|
| 2026-01-01 | Gym              | Arms                             |
| 2026-01-02 | Gym              | Legs                             |
| 2026-01-03 | Swimming         | LCM 1.2km                        |
| 2026-01-04 | Swimming         | LCM 3.4km                        |
| 2026-01-05 | Swimming         | SCM 5.6km                        |

2. Generated TXT file (data/training_calendar.txt)

```text
2026-01-01 Gym Arms
2026-01-02 Gym Legs
2026-01-03 Swimming LCM 1.2km
2026-01-04 Swimming LCM 3.4km
2026-01-05 Swimming SCM 5.6km
```

3. Converted CSV file (data/training_calendar.csv)

```text
date,sport,discipline,distance
2026-01-01,Gym,Arms,
2026-01-02,Gym,Legs,
2026-01-03,Swimming,LCM,1.2
2026-01-04,Swimming,LCM,3.4
2026-01-05,Swimming,SCM,5.6
```

4. Aggregated statistics

| sport    | discipline | count | total | average |
|:---------|:-----------|------:|------:|--------:|
| Gym      | Arms       |     1 |       |         |
| Gym      | Legs       |     1 |       |         |
| Gym      |            |     2 |       |         |
| Swimming | LCM        |     2 |   4.6 |     2.3 |
| Swimming | SCM        |     1 |   5.6 |     5.6 |
| Swimming |            |     3 |  10.2 |     3.4 |
