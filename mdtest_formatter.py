import argparse
import sys
import re
import csv


table_line_regex = '\s*(?P<operation>.+?)\s*:\s*(?P<data>.+)\s*$'


def parse_header_line(line):
    return line.strip().split(None, 4)


def parse_table_line(line):
    match = re.match(table_line_regex, line)
    res = list()
    res.append(match.group(1))
    numbers = [float(x) for x in match.group(2).split()]
    return res + numbers


def parse_mdtest(input):
    data = []
    # Skip all lines before data table
    for line in input:
        if line.startswith("SUMMARY"):
            break
    # Parse table header
    column_names = parse_header_line(next(input))
    data.append(column_names)

    # Skip header separator line
    if not next(input):
        raise RuntimeError("Error while parsing input:"
                           "Missing expected second line of table header")
    # Parse table data
    for line in input:
        if not line.startswith("   "):
            break
        data.append(parse_table_line(line))

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Converts mdtest output into CSV format.')
    parser.add_argument('-i', '--input',
            type=argparse.FileType('r'),
            default=sys.stdin,
            help="input file produced by mdtest, '-' for stdin."
                 "By default stdin will be read")
    parser.add_argument('-o', '--output',
            type=argparse.FileType('w'),
            default=sys.stdout,
            help="output file to write, '-' for stdout."
                 "By default output will be printed on stdout")
    args = parser.parse_args()

    # parse input
    data = parse_mdtest(args.input)
    csv_out = csv.writer(args.output)
    # format output
    for line in data:
        csv_out.writerow(line)
