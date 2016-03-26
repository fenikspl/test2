#!/bin/bash

echo "Co wybierasz?"
select x in update upgrade rpi-update
do
  case $x in
    "update") sudo apt-get update ;;
    "upgrade") sudo apt-get upgrade ;;
    "rpi-update") sudo rpi-update ;;
    *) echo "jakis blad"
  esac
break
done
