PYTHON ?= python3
DATA_DIR := data
TXT := $(DATA_DIR)/training_calendar.txt
CSV := $(DATA_DIR)/training_calendar.csv
SQL := training_calendar.sql

.PHONY: all run clean

all: run

$(DATA_DIR):
	mkdir -p $(DATA_DIR)

$(TXT): | $(DATA_DIR)
	shortcuts run "Training Calendar" --output-path "$(TXT)"

$(CSV): $(TXT)
	$(PYTHON) convert_txt_to_csv.py --input "$(TXT)" --output "$(CSV)"

run: $(CSV) $(SQL)
	filename="$(CURDIR)/$(CSV)" duckdb -f "$(SQL)"

clean:
	rm -rf "$(DATA_DIR)"
