#!/bin/bash

i=32768
for x in {1..40}; 
do
	((i++))
	echo "alias r$x='telnet 192.168.101.253 $i'"
done

