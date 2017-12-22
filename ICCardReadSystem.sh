#!/bin/bash

binary_path=`dirname $0`
while :
do
if sudo python ${binary_path}/GUI-useServer.py
#if sudo python GUI-after.py
  then
    break
  fi
done

exit 0
