# Bash's array is enclosed in parentheses.
# Here's three way to create a array.
array_name=(value0 value1 value2)
array_name=(
value0
value1
value2
value3
)

array_name[0]=value0
array_name[1]=value1

# The way to read array is same as variable.Different
# thing is use braces
echo ${array_name[index]}

# You can use '@' or '*' to get all elements in array.
${array_name[*]}
${array_name[@]}

#Get length of arrays. Same as string.
length=${#array_name{@}}