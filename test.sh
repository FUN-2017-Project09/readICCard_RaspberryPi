#!/bin/bash
while :
do
  if sudo python GUI.py
  then
    break
  fi
done

exit 0