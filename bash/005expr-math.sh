#!/bin/bash

val=`expr 2 + 2`
echo "2+2= $val"

a=10
b=20

val=`expr $a - $b`
echo "$a - $b = $val"

val=`expr $a + $b`
echo "$a + $b = $val"

val=`expr $a \* $b`
echo "$a * $b = $val"

val=`expr $a / $b`
echo "$a / $b = $val"

val=`expr $a % $b`
echo "$a % $b = $val"