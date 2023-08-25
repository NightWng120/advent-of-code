#!/bin/bash

if [ "$1" = "" ] ; then
	echo "No day number was entered, directory not created"
	return
fi

mkdir day$1

cd day$1

touch sample.txt input.txt day$1.c

echo -e "#include <stdio.h>\n#include <stdlib.h>\n\nvoid part1(){\n}\n\nvoid part2(){\n}\n\nint main(){\n}" >> day$1.c
