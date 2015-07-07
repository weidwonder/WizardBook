#!/bin/bash
# use break
while [[ true ]]
do
	echo -n "Input a number between 1 to 5:"
	read aNum
	case $aNum in
		1|2|3|4|5) echo "Your number is $aNum!"
		;;
		*) echo "You do not select a number between 1 to 5,game is over!"
		break
		;;
	esac
done

# break n can break multiloop, n represent loop deep.
# this deepth is from inside to outside.
# another keyword 'contine' is same as break,
# little different is it won't break loop,just
# jump directly to next loop.