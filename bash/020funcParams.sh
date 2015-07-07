func() {
	echo $#
	i=1
	while [[ $i -le $# ]]
	do
		echo "the $i param is $1"
		i=`expr $i + 1`
	done
}

func 1 2 3 4 5 6
# attition!!:
#	the 10th param must use ${10}, not $10!