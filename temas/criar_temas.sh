#!/bin/bash

while read line
do
	tema=$( echo $line | grep -v '{' | grep -v '}' | cut -d "'" -f 4 | tr '[:upper:]' '[:lower:]' | sed 's/ /_/g')
	path=$(pwd)
	echo $path
	mkdir -p $path/$tema
	cd $path/$tema/
	touch lista.txt
	cd $path/
done < ~/Desktop/stop_cheat/temas.txt
