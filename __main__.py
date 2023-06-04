#
#    @Name: Simple File Organizer
#    @Author: https://github.com/pxlrl
#
#    About:
#    This program will try to organize your file system without installing
#    third-party libraries, and was done within `pathlib` module.
#    This is also can be used as learning method for you to have better
#    understanding about what python is and what you can do about it.
#
#    Copyright (C) 2023  pxlrl
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
import sys, os, argparse
from core import FileOrganizer

def main(args):
	organizer = FileOrganizer(args.path)
	organizer.start()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Simple file organizer made by pxl to just flex how much knowledge he have, turns out it was far from becoming pro python like cman")
	parser.add_argument('path', type=str, help="A required path for organizing the files.")
	args = parser.parse_args()
	main(args)
