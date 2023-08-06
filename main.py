#!/usr/bin/env python3

import argparse
import csv
import os
import sys


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=argparse.FileType("r"))

    args = parser.parse_args(argv[1:])

    print('<!DOCTYPE connections>')
    print('<qgsXYZTilesConnections version="1.0">')
    reader = csv.reader(args.input, delimiter="\t")
    for row in reader:
        if not row:
            continue
        name, area, time, folder = row
        zoom_max = 16
        if name in ["東北地方太平洋岸", "関東"]:
            zoom_max = 15
        print(f'    <xyztiles name="今昔マップ {name} {time}" zmax="{zoom_max}" password="" tilePixelRatio="0" http-header:referer="" url="https://ktgis.net/kjmapw/kjtilemap/{area}/{folder}/{{z}}/{{x}}/{{-y}}.png" authcfg="" referer="" zmin="8" username=""/>')
    print('</qgsXYZTilesConnections>')

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
