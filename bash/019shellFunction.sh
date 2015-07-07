# Shell function must be defined before using.
# gramma:
# <function_name>() {
#	[ commands|* ]
#	[ return <value> ]	
# }
# the return is optional if you haven't add a
# return it will return last command result.

# ----------test1----------
Hello(){
	echo "Hello weidwonder!"
}

Hello

# -----------test2----------
Hello(){
	return 3
}

Hello
ret=$?
echo $ret

# -----------test3----------
number_one() {
	echo "haha, this is No.1"
	number_two # this is define in one, not using
			   # so, it won't raise error.
}

number_two() {
	echo "oh yeah, this is No.2"
}

number_one

# ------------test4------------
# we can delete function as the way delete variable.
unset -f number_one
number_one