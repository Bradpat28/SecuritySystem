#!/bin/bash
function installSystem { 
	echo Installing the Security System...
	echo Installing the main directory...
	mkdir -p ./.securesys
	cd .securesys
	echo Creating the File System...
	echo 'Username,Password' > fileSystem.csv
	printf 'admin,admin\n' >> fileSystem.csv
	cd ..
	echo Done Installing the Security System
}

installSystem