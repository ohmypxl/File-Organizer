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

import core.extensions as ext
import pathlib

class FileOrganizer:
	"""
	A Class that can operate to organize your files
	with amazing 3 lines of pathlib operations!
	"""
	def __init__(self, target_path: str) -> None:
		self.target_path = pathlib.Path(target_path)

	def start(self) -> int:
		"""
		Will start the organizing process,
		"""
		print("[...] Starting organizing process.")

		# We going to count how many files do we process
		processed_count = 0

		# Now we're going to iterate all the directory in the current folder
		for files in self.target_path.iterdir():
			
			# If the files we're looking for turns out to be the directory, we skip
			if files.is_dir():
				continue

			# Get the folder name for the corresponding extension, and then combine it with target_path
			dir_path = self.target_path / pathlib.Path(ext.get_folder(files.suffix))

			# Create directory for the path if not exists, otherwise this would pretty much got ignored
			dir_path.mkdir(exist_ok=True)

			# Move the corresponding file into the appropriate folder
			files.rename(dir_path / files.name)

			# Add 1 into the variable
			processed_count += 1

		# Tell the user the organizing is success!
		if processed_count:
			print("[...] Organizing success.")
			return processed_count
		
		print("[xxx] Failed to organize the files")
		return 0

# For testing purposes
if __name__ == '__main__':
	organizer = FileOrganizer(".")
	organizer.start()
