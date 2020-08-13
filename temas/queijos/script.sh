for word in $(cat lista.txt); do
	echo ${word:0:1}: $word >> lista.txt
done
