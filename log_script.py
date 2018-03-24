#!usr/bin/python
#Python script used to display the error_logs of web services (/var/log/httpd/error_log)
import os

f = open("/var/log/httpd/error_log","r")
of = open("./output_logs", "w")
num = 1

for line in f.readlines():
    array = line.split("] ")
    if(len(array) > 1):
        date = array[0]
        source = array[1]
        reason = array[3]
        of.write("\nLOG: " + str(num))
        of.write("\nDate: " + date[1:])
        of.write("\nSource: " + source[1:])
        of.write("\nReason: " + reason)
        num = num+1

f.close()
of.close()

