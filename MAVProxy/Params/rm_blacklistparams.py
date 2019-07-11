#!usr/bin/env/python
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
                name = (line.split())[0]
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
                    if line == "\n": # Ignore empty line
                        continue
                    # Extract param name and compare with "blacklist"
                    # There are two types of param files:
                    # (1) Those that separate param + value by space
                    # (2) And those that separate param and value by comma
                    elif " " in line:
                        name = (line.split())[0] # Case 1
                    else:
                        name = line[:line.find(",")]
                    if not (name in self.__blacklist): # Case 2
                        writer.write(line) # Write only if param is not in "blacklist"

def main():

    if len(sys.argv) < 3:
        raise Exception ('Input the following: (1) param file, (2) list of blacklisted params')
    test = remover()
    test.populateblacklist()
    test.remove()

if __name__ == "__main__":
    main()