#!/bin/bash
echo "Co wybierasz?"
select y in x y z Quit
do
  case $y in
    "x") ./aktualizacja.sh ;;
    "y") echo "Wybrales Y" ;;
    "z") echo "Wybrales Z" ;;
    "Quit") exit ;;
    *) echo "Nic nie wybrales"
  esac
break
done

