import argparse
import re
import sys

LOG_PATTERN = re.compile(r'^(\d{4}-\d{2}-\d{2}) (\w+) (\w+)(?: (\d+(?:\.\d)?)km)?$')


def convert(in_txt_file, out_csv_file):
    with open(in_txt_file, 'r') as in_file:
        out_csv_file.write('date,sport,discipline,distance\n')
        for line in in_file:
            match = LOG_PATTERN.match(line)
            if match:
                date, sport, discipline, distance = match.groups()
                out_csv_file.write(f'{date},{sport},{discipline},{distance or ""}\n')
            else:
                print(f'Warning: Line does not match the expected format and will be skipped: {line.strip()}', file=sys.stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a textual training log into csv txt.')
    parser.add_argument('--input', dest='input_file', required=True, help='Path to the input txt file')
    args = parser.parse_args()

    convert(args.input_file, sys.stdout)
