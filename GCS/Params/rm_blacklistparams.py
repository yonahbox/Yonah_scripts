#!usr/bin/env/python3

# Copyright (C) 2019 Lau Yan Han and Yonah (yonahbox@gmail.com)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
This script takes 2 command line arguments: (1) Param file, (2) List of blacklisted params.
It copies the first file params to a new file (out.param), but excludes blacklisted params
Blacklisted params are params that should not be manually set by user (e.g. STAT_BOOTCNT)
"""

import sys
import os.path

class remover():
    
    __blacklist = set() # Blacklisted params, initialized as empty set

    def populateblacklist(self):
        """populate the blacklist with specified params from second command line argument
        Note: Each param in the blacklist must start on a new line"""
        listname = sys.argv[2]
        with open (listname, "r") as reader:
            for line in reader:
                if "#" in line: # Ignore comments
                    continue
                if line == "\n": # Ignore blank lines
                    continue
                # Extract param from blacklist
                # There are three types of blacklist files:
                # (1) Those that separate param + value by space
                # (2) Those that separate param and value by comma
                # (3) Those with only parameter names and no values
                if "," in line:
                    name = line[:line.find(",")] # Case 2. Extract param name before comma
                else:
                    name = (line.split())[0] # Cases 1 and 3: Extract param name before space/whitespace
                self.__blacklist.add(name)
    
    def remove(self):
        """parse param file provided in first command line argument,
        remove blacklisted params, and write results to out.param"""
        filename = sys.argv[1]
        if (not os.path.isfile(filename)):
            raise Exception('Param file doesn\'t exist in the current folder')

        with open (filename, "r") as reader: # open param file for reading
            with open ("out.param", "w") as writer: # write to output param file
                for line in reader: 
                    if "#" in line: # Ignore comments
                        continue
                    if line == "\n": # Ignore empty line
                        continue
                    # Extract param name and compare with "blacklist"
                    # There are two types of param files:
                    # (1) Those that separate param + value by space
                    # (2) And those that separate param and value by comma
                    if " " in line:
                        name = (line.split())[0] # Case 1. Extract param name before space
                    else:
                        name = line[:line.find(",")] # Case 2. Extract param name before comma
                    if not (name in self.__blacklist):
                        writer.write(line) # Write only if param is not in "blacklist"

def main():

    if len(sys.argv) < 3:
        raise Exception ('Input the following: (1) param file, (2) list of blacklisted params')
    test = remover()
    test.populateblacklist()
    test.remove()

if __name__ == "__main__":
    main()