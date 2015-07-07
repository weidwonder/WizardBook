# single qoute.
# --------------
# Every string in single qoute output as what it
# is exactly look like.
# Can't put another single qoute in single-qoute-string.
# --------------
str='this is a string'

# double qoute.
#---------------
# Double-qoute-string can include variables and transfer-chatacter.
#---------------
str="this is a double qoute string"

# Connect strings
str1="weidwonder"
str2=$str1" likes you"
str="hello,${str1}"

echo $str  $str2

# extract substring from string
string="abcdefghijklmnopqrstuvwxyz"
echo ${string:1:4}

# get string length
echo ${#string}

# search substring index
echo `expr index "$string" efg`