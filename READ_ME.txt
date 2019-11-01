***A Guide on how to run the socket program***

To Run a single client-server connection on the same machine
   1, open a comman prompt 
   2, run the single server python file and add the port number as argument 
  	e.g "python server_single.py 1234"
   3, open a different command prompt
   4, run the single client python file and add port(same port with server) and message to send as arguments
  	e.g 'python client_single.py 1234 "rediet.negash@gmail.com"'

To Run a single client-server connection on a different machine
   1, open python file for client "client_single.py" 
   2, add the ip address of the machine as a host 
     e.g "host = '125.23.12.67'"
   3, save the file and run it by followint the same procedure with same machine
 caution: make sure that the fire wall is not blocking the connection
          you should register the port manually to your machine if u fail to connect
	  please google on how u can register your port and it will work

To Run a multiple client-server 
   1, run server_multi.py on a command prompt with a port num as an argument
   2, open two or more command prompts and run client_single.py with a port and message to send as an argument
   3, to connect on a different machine change the ip address on each client.