#!/usr/bin/env

a='f_text'
b='r_text'


c="sed -i '/s/"+a+"/"+b+"/g' file.txt"
print(c)
