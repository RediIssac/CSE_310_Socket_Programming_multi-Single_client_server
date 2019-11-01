# Name Rediet Negash
# 111820799

import socket
import sys
from sys import argv

def run_client(PORT, message):
    try:
        port = int(PORT)
        host = 'localhost'
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to the server
        s.connect((host, port))

        # add message type and length of string as a header in front of the message and encode it as a byte
        q_message = bytes("Q" + chr(len(message)) + message, "UTF-8")
        # send the encoded message to server
        s.sendall(q_message)
        # print what was sent
        print('client sent', repr(message))
        # now receive data from the server
        print('receiving data...')
        data = s.recv(1024)
        if data:
            # decode the received message and print it to the screen
            name = str(data[2:],'utf-8')
            print('Client Received:  ', (name))
            print('Successfully received the file')
            s.close()
            print('connection closed')
        # if no data is received prompt to the screen the error
        else:
            print("ERROR FOUND: no data received")
            sys.exit(1)
    except socket.error as exc:
        print("Caught exception socket.error : %s" % exc)

if __name__== "__main__":
    # get port and message as input arguments from terminal
    try:
        run_client(argv[1], argv[2])
    except Exception as e:
        print ("Error found ", repr(e))
        print("please enter arguments when running the code: port, message")