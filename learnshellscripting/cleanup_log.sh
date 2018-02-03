#!/bin/sh

# script that can be used to do cleanup of any log
# By default it save last 10 lines of your log directory, otherwise we can specify the number of line we need to save


LOG_DIR=$HOME/DJ/learnshellscripting/test_dir/
FILE=test_file.txt
LINES=10
ROOT_UID=0

# defining different exit status codes for handling different errors
E_NO_ROOT=85
E_NO_DIR=86
E_BAD_ARG=87
E_NO_FILE=89

if [ "$UID" -ne "$ROOT_UID" ]				# root user ID is always 0
then
	echo "Please run this script as root user"
	exit $E_NO_ROOT
fi

if [ -n "$1" ]						# verifying positional parameter is not empty
then
	lines=$1
else
	lines=$LINES
fi

cd $LOG_DIR || { 					# usring OR we are verifying if the command executed is succeded or not
	echo "Unable to change the directory" >&2
	exit $E_NO_DIR;
}

if [ ! -f $FILE ]
then
	echo "Log $FILE not found"
	exit $E_NO_FILE
e	lse
	tail -n $lines $FILE > $FILE.tmp
	mv $FILE.tmp $FILE				# this avoid doing cat /dev/null > $FILE to empty it and then copy append it with saved line 
fi

exit 0
