PYTHON ?= python3
DATA_DIR := data
TXT := $(DATA_DIR)/training_calendar.txt
SQL := training_calendar.sql

.PHONY: all run clean

all: run

$(DATA_DIR):
	mkdir -p $(DATA_DIR)

$(TXT): | $(DATA_DIR)
	shortcuts run "Training Calendar" --output-path "$(TXT)"

run: $(TXT) $(SQL)
	$(PYTHON) convert_txt_to_csv.py --input "$(TXT)" | duckdb -f "$(SQL)"

clean:
	rm -rf "$(DATA_DIR)"
