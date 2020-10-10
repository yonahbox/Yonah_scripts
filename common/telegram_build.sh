#!/bin/bash

# Script to build TDLib
# based on instructions provided at https://tdlib.github.io/td/build.html?language=Python

BONE=false
while getopts 'bg' flag
do
	case "${flag}" in
		b)
			BONE=true
			;;
		g)
			BONE=false
			;;
	esac
done

# Install dependancies

# uncomment the below line if running the script standalone
# sudo apt-get update

sudo apt install make git zlib1g-dev libssl-dev gperf php cmake clang libc++-dev

if ! $BONE
then
	sudo apt install libc++abi-dev
fi

# Clone TDLib repo, placing in repo/ to avoid cluttering home
cd ~
mkdir repo
cd repo
git clone https://github.com/tdlib/td.git
cd td
git checkout v1.6.0

# Build Telegram
echo "This process is going to take a long time, use this time to do something productive instead of staring at the screen :)"
rm -rf build
mkdir build
cd build
export CXXFLAGS="-stdlib=libc++"
CC=/usr/bin/clang CXX=/usr/bin/clang++ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/usr/local ..

if [[ $BONE ]]
then
	cmake --build . --target prepare_cross_compiling
	cd ..
	php SplitSource.php
	cd build
fi

sudo cmake --build . --target install

if [[ $BONE ]]
then
	cd ..
	php SplitSource.php --undo
fi
