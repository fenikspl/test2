#! /bin/bash

echo "Co wybierasz?"
select x in install run quit
do
  case $x in
    "install") sudo apt-get install tightvncserver ;;
    "run" ) sudo tightvncserver ;;
    "quit" ) echo "wyjscie" ;;
    *) echo "jakis blad"
  esac
break
done
