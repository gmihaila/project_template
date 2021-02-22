# coding=utf-8
# Copyright 2020 George Mihaila.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Main python script to run for this project.
"""

import argparse

from __version__ import __version__
from utils.helper_functions import power_up


def parse_args() -> argparse.ArgumentParser:
    """
    Parsing input script arguments.

    Returns:
        argparse.ArgumentParser: Parsed arguments.
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="This is my project template.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="Display version information.",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        "-d",
        "--debug",
        action="store_true",
        dest="verbose",
        default=False,
        help="Display extra debugging information and metrics.",
        required=False,
    )
    parser.add_argument(
        "--output",
        "-o",
        dest="output",
        help="If using single username, the output of the result will be saved to this file.",
        required=False,
    )
    parser.add_argument(
        "-l", "--list", nargs="+", help="List argument.", required=False
    )

    return parser.parse_args()


def main():
    """
    Main function.
    """
    # Parse arguments.
    args = parse_args()

    power_up(2, 3)

    print(args)


if __name__ == "__main__":
    main()
