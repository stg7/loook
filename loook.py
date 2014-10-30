#!/usr/bin/env python3
"""
    loook - small log book tool

    author: Steve Göring
    contact: stg7@gmx.de
    2014

"""
"""
    This file is part of loook.

    loook is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    loook is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with loook.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import sys
import datetime
import argparse

def script_dir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def read_stdin():
    lines = []
    try:
        for l in sys.stdin:
            lines.append(l.replace("\n",""))
    except KeyboardInterrupt:
        print("end of log")
    return lines

def main(params):
    # argument parsing
    parser = argparse.ArgumentParser(description='loook - small log book tool', epilog="stg7 2014")

    parser.add_argument('-m', dest='message', type=str, help='short message', default="")
    parser.add_argument('-d', dest='debug', action="count", default=0, help='print debug messages')
    parser.add_argument('-s', dest='stats', action="count", default=0, help='print statistics')

    argsdict = vars(parser.parse_args())

    DEBUG = False
    if argsdict['debug'] != 0:
        DEBUG = True

    shortmessage = argsdict['message']

    date_time = str(datetime.datetime.today())
    print(date_time)

    lines = [ "% " + date_time ]
    if shortmessage == "":
        # read from stdin
        lines += read_stdin()
    else:
        print(shortmessage)
        lines.append(shortmessage)

    lines.append("------")

    # check if user has done some input, otherwise write nothing to the file
    if "".join(lines[1:-1]) == "":
        return

    outfile = open(script_dir() + "/log.book.md", "a")
    for l in lines:
        outfile.write(l + "\n")
    outfile.close()

    print("done")


if __name__ == "__main__":
    main(sys.argv[1:])

