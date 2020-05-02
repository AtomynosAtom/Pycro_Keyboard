#!/bin/python3
f = open("Keys.txt","a")
for i in range(0, 95):
    f.write(chr(32 + i)+"::\n")

