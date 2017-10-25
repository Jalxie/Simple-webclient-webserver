# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:48:17 2017

@author: jalsey
"""
import os
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)# address

#create an INET, STREAM socket
scli = socket(AF_INET, SOCK_STREAM)
scli.connect(ADDR)

#main loop 
while True:
    #get input
    rawdata = input("Say something> ")
    
    if len(rawdata) > 140:# the length of input must less than 140
        print('Invalid input, input must less than 140 characters')
        break
    if rawdata == 'exit' or not rawdata :# exit if input is exit or no input
        print('Shutting down...')
        exit()
    #encode data the tramsimit
    data = rawdata.encode()
    scli.send(data)
    #receive data from server
    data = scli.recv(BUFSIZ)
    #decode
    data = data.decode()
    #display data
    print(data)

#close the socket
scli.close()






