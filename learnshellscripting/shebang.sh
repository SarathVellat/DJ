#!/bin/sh

# the above line which we mention in our script is called shebang.. # resembles the sharp sign in music and sometime
# people says ! as bang. This lines tells our script to use which interpreter for execution under Unix/Linux operating
# systems. Its indicates the absolute path to the bash indicator.

sleep 90

# if we run this script in background, then we should be able to see what is happening.
# ./shebang.sh &

#Saraths-MacBook-Air:shell_scripting sarathvellat$ ps -fp 9097
#  UID   PID  PPID   C STIME   TTY           TIME CMD
#  501  9097  1103   0  6:52PM ttys000    0:00.00 /bin/sh ./test.sh
#Saraths-MacBook-Air:shell_scripting sarathvellat$