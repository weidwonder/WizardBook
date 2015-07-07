# just like switch in c, ';;' is just like break.
echo 'Input a number between 1 to 4'
echo 'Your number is:\c'
read aNum
case $aNum in
	1) echo 'You select 1'
	;;
	2) echo 'You select 2'
	;;
	3) echo 'You select 3'
	;;
	4) echo 'You select 4'
	;;
	*) echo 'You bad kid.'
esac