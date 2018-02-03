#!/bin/sh

#script that backs itself up, that is, copies itself to a file named backup.sh.

echo "hello My name is Sarath"
cp $0 backup.sh
echo "Here is the backup file \n$(ls -lrt backup.sh)"
