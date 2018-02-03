#!/bin/sh

# script that can be used to do cleanup of any log
# By default it save last 10 lines of your log directory, otherwise we can read the number of line we need to save from user

read -p "Enter the number of lines you want to save :" LINES 

LOG_DIR=$HOME/DJ/learnshellscripting/test_dir/
FILE=test_file.txt
ROOT_UID=0

# defining different exit status codes for handling different errors
E_NO_ROOT=85
E_NO_DIR=86
E_BAD_ARG=87
E_NO_FILE=89

if [ "$UID" -ne "$ROOT_UID" ]			# root user ID is always 0
then
	echo "Please run this script as root user"
	exit $E_NO_ROOT
fi

	
case "$LINES" in				# using case statment we can verify if the input is an empty string, or its a non numeric string
	"" )
		lines=10
		;;
	*[!0-9])
		echo "Invalid Argumenets"
		exit $E_BAD_ARG
		;;
	*)
		lines=$LINES
		;;
esac
		

cd $LOG_DIR || { 							
	echo "Unable to change the directory" >&2
	exit $E_NO_DIR;
}						# usring OR we are verifying if the command executed is succeded or not			

if [ ! -f $FILE ]
then
	echo "Log $FILE not found"
	exit $E_NO_FILE
else
	tail -n $lines $FILE > $FILE.tmp	# this avoid doing cat /dev/null > $FILE to empty it and then copy append it with saved line 
	mv $FILE.tmp $FILE
fi

exit 0
