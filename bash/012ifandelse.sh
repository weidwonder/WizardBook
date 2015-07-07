# function type:
# if [ expression ]
# then
# 	statement(s) to be executed if expression is true
# fi

read a
echo "a is $a"
if [ $a -gt 1 ];then
	echo "yes"
elif [ $a == 1 ];then
	echo "no"
else
	echo "baba"
fi