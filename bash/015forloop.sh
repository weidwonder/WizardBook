# gramma:(only)
# for <variable> in <list>
# do
# 	command1
# 	command2
# 	...
# done
for loop in 1 2 3 4 5 
do
	echo "The value is $loop"
done

for FILE in $HOME/.bash*
do
	echo $FILE
done