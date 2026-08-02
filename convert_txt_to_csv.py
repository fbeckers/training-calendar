import argparse
import re

LOG_PATTERN = re.compile(r'^(\d{4}-\d{2}-\d{2}) (\w+) (\w+)(?: (\d+(?:\.\d)?)km)?$')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a textual training log into a csv file.')
    parser.add_argument('--input', dest='input_file', required=True, help='Path to the input txt file')
    parser.add_argument('--output', dest='output_file', required=True, help='Path to the output csv file')
    args = parser.parse_args()

    with open(args.input_file, 'r') as in_file, open(args.output_file, 'w') as out_file:
        out_file.write('date,sport,discipline,distance\n')
        for line in in_file:
            match = LOG_PATTERN.match(line)
            if match:
                date, sport, discipline, distance = match.groups()
                out_file.write(f'{date},{sport},{discipline},{distance or ""}\n')
            else:
                print(f'Warning: Line does not match the expected format and will be skipped: {line.strip()}')
