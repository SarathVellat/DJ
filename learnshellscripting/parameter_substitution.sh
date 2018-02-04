#!/bin/sh

# $@ points to all the positional parameters.
# $* points to all the positional parameters as single string.
# $# shows the total number of positional parameters passed.

for i in $@;do echo $i;done
echo $*
echo $#

# =========================================================================================
# comma operator can be used to related multiple arithmetic operations
# also we can use let. let arg [arg..]. let deals each arg as arithmetic expression

let "t2 = ((a = 3, 15/3))"

echo "Value of t2 is $t2"
echo "Value of a is $a"

id=0
echo "Value of id is $id"
for i in $@;do let ++id;done
echo "Value of id is $id"

x=5;echo $((x++ /2));echo ${x}		# difference between post and pre increment
y=5;echo $((++y /2));echo ${y}

# comman operator can also used 

for file in /{,usr/}bin/*b
do
	if [ -e $file ]
	then
		echo $file
	fi
done

# =========================================================================================

# Saraths-MacBook-Air:test_dir sarathvellat$ cat template.txt 
# The number is ${i}
# The word is ${word}
# Saraths-MacBook-Air:test_dir sarathvellat$ 

# use sed or envsubst 

sed -e "s/\${i}/1/" -e "s/\${word}/dog/" $HOME/DJ/learnshellscripting/test_dir/template.txt
i=32 word=foo envsubst < $HOME/DJ/learnshellscripting/test_dir/template.txt

# to read a file 
while read line
do
	echo "$line"
done < "$HOME/DJ/learnshellscripting/test_dir/template.txt"

# to replace variables using while loop

i=50
word=hello

while read line
do
	eval echo "$line"
done < "$HOME/DJ/learnshellscripting/test_dir/template.txt"
