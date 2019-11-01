# Name : Rediet Negash
# id : 111820799

# import important modules
import socket
import json
from sys import argv
from _thread import *
import threading 

# there is a json file in the same directory that has list of names and email addresses so open that file and load it
f = open('data.json')
Names = json.load(f)

print_lock = threading.Lock()
def Main(Port):

    # make sure that port is an integer value
    port = int(Port)
    # create a socket for server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # before binding make sure that the address is not being used by the OS if it is allow it by turning on bit to 1
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind the socket to any host and a given port as an argument from cmd_line
    s.bind(('', port))
    # listen for incoming connections
    print('Server listening....')

    s.listen(5)
    while True:
        # accept if a connection is found
        conn, addr = s.accept()
        # lock acquired by client 
        print_lock.acquire() 
        # print the address of the connection found
        print ('Got connection from', addr)
        start_new_thread(threaded,(conn,))
    s.close()

# create a socket for server
def threaded(conn):
    try:
        # start receiving data
        while True:
            data = conn.recv(1024)
            if not data:
                print('Bye')
                print_lock.release()
                break
            # check if length of question/response is < 255
            if len(data) < 255:
                # check if the Length of String
                if len(data) > 2:

                    # look for a name for the corresponding email address from the opened json file and decode it
                    email = data[2:].decode('utf-8')

                    # print the received message
                    print('Server received: ', email)
                    name = Names[email]
                    # add a message type and length of string as a header and encode the found name from the DB
                    r_message = bytes("R" + chr(len(name)) + name, "UTF-8")
                    # send the response message
                    conn.sendall(r_message)
                    print('Sent ', repr(name))
            # if length is more than the message format allowed prompt a message
            else:
                print("More than expected file message format, q&R is restricted to 255 bytes")
        # close json file
        f.close()
        print('Done sending')
        # close the connection
        conn.close()
    # if Input error is found or any other error catch it
    except KeyError as e:
        print ('I got a KeyError - reason "%s"' % str(e))
        # now if a key doesn't exist in the DB prompt message
        print("key not found in the database")
    except Exception as e:
        print ("Error found ", repr(e))

if __name__ == "__main__":
    # get port as input from the terminal
    try:
        # run the server if arguments are entered from the terminal
	
        Main(argv[1])
    except Exception as e:
        print("Error found ", repr(e))
        print("please enter port as argument")