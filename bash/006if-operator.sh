#!/bin/bash

a=10
b=10

if [ $a == $b && 10 == 10 ]; then
	echo "a is equal to b"
elif [ $a != $b ]; then
	echo "a is not equal to b"
fi