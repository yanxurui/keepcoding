rm a.txt                    
touch a.txt

python2.7 write_file_conllision.py 2

awk -F: '{print $1}' a.txt | sort | uniq -c
