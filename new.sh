#! /bin/bash

echo "Co wybierasz?"
select x in "nowy program" run quit
do
  case $x in
    "install") sudo apt-get install tightvncserver ;;
    "run" ) sudo tightvncserver ;;
    "quit" ) clear
	     echo "wyjscie" ;;
    *) echo "jakis blad"
  esac
break
done
