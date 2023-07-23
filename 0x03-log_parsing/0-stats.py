#!/usr/bin/env python3
"""
Defines a script that reads stdin line by line and computes metrics"""

import sys


if __name__ == "__main__":

    filesize, count = 0, 0
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """Prints stats"""
        print("File size: {:d}".format(filesize))
        for key, value in sorted(stats.items()):
            if value:
                print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass

            try:
                filesize += int(data[-1])
            except BaseException:
                pass

            if count % 10 == 0:
                print_stats(stats, filesize)

        print_stats(stats, filesize)

    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
