#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""


from sys import stdin

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0
                }

file = 0


def print_log():
    """logs output"""

    print("File size: {}".format(file))
    for stat in sorted(status_codes.keys()):
        if status_codes[stat]:
            print("{}: {}".format(stat, status_codes[stat]))


if __name__ == "__main__":
    count = 1
    try:
        for line in stdin:
            try:
                log = line.split()
                if log[-2] in status_codes:
                    status_codes[log[-2]] += 1
                file += int(log[-1])
            except Exception:
                pass
            if count % 10 == 0:
                print_log()
            count += 1
    except KeyboardInterrupt:
        print_log()
        raise
    print_log()
