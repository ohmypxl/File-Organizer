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

import os
import tomllib as toml

file_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(file_dir, "../config-extensions.toml")

with open(config_path, "rb") as f:
	extensions_map = toml.load(f)

def get_folder(ext: str) -> str:
	for dir, ffs in extensions_map.items():
		for extensions in ffs:
			if extensions == ext:
				return dir

	return "Others"

# For testing purposes
if __name__ == '__main__':
	print(get_folder(".mp4"))
