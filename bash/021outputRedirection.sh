who > file #overwrite
who >> file #not overwrite
wc -l users
wc -l < users

# redirect stdout stderr to file, like this
command > file 2 > &1
# it will merge two files

# Here Document,is insect document.
command << delimiter
	document
delimiter

ls -a > /dev/null