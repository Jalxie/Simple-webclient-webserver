# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:48:17 2017

@author: jalsey
"""
import os
from socket import *
from time import ctime


HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)# address

#create an INET, STREAMing socket
s = socket(AF_INET, SOCK_STREAM)
s.bind(ADDR)
s.listen(5)

while True:
    print('waiting for connection...')
    #accept connection from client
    scli, addr = s.accept()
    print('...connected from:',addr)

    while True:
        raw = scli.recv(BUFSIZ)
        #decode the incoming data 
        data = raw.decode()
        
        if not data:
            break
        
        #shut down the server when input is 'shut down'
        if data == 'shut down':
            exit()
            
        #print the data
        print(data)
        #send timestamp to client 
        scli.send(ctime().encode())
    #close client
    scli.close()
#close server    
s.close()