# printf function is like echo but more migratable.
printf "Hello, Shell\n"
a=10
printf "%d %c\n" $a $a
printf "%d %s\r\n" 1 "abc"

# if there is no argument then by default, %s is replaced
# by null and %d by 0
printf "%d %s %f\n" 