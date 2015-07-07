# Untill loop gramma.
# until <condition>
# do
# 	do sth
# done
a=0
until [ ! $a -lt 10 ]
do
	echo $a
	a=`expr $a + 1`
done