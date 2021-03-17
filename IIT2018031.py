
# Here we are importing various modules to build our proxy server
# importing OSmodules
import os
import sys
#import thread modules 
#Threading in python is used to run multiple threads (tasks, function calls) at the same time 
import thread
import socket

CONNECTIONS_REQUEST = 4  # pending connection in queue
Size_of_max_data = 9999  # It signifies the maximum number of bytes that can be recieved at once


#This is the main program:
def main():

    #This portion of the code checks the input for the port 
    # check the length of command running
    if (len(sys.argv)<2):
        print "When No port given, using :8080 (http-alt)" 
        port = 8080
    else:
        port = int(sys.argv[1]) # port from argument

    # host and port info.
    host = ''               # blank for localhost
    print("                  Welcome:                 "  )
    print "Our Proxy Server is running on port ",host,":",port
    print "Now visit some websites to test the working of the Proxy :"

    try:
        # This is the socket command : Create a socket with the socket() system call.
        socketName = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # associate the socket to host and port
        # Send and receive data. There are a number of ways to do this but the simplest way is to use  
        # the read() and write() system calls
        socketName.bind((host, port))

        # listenning
        # Listen for connections with the listen() system call
        socketName.listen(CONNECTIONS_REQUEST)
    
    except socket.error, (value, message):
        if socketName:
            socketName.close()
        print "Could not open socket:", message
        sys.exit(1)

    # get the connection from client
    while 1:
        connection, client_addr = socketName.accept()

        # create a thread to handle request
        # Whenever proxy recieves request from client i.e. web browser .
        # it creates a thread to handle the request
        thread.start_new_thread(proxy_thread, (connection, client_addr))
        
    socketName.close()

#End of the main program

#Printout function
#This function is made to test the print the HTTP METHOD ...which is 'get' here.
def printout(type,request,address):

    V=request;
    result=request.find("GET")
    
    #To check if the method is get or not:
    if V.find("GET")==-1:
        print("Error 501 :Not Implemented for other methods")
        print("Method is not of type of GET but we are priting it look at its type and then exiting")
        print "\033[",type,"\t",request,"\033[0m"
    elif "Block" in type :
        colornum = 91
        print "\033[",colornum,"m",address[0],"\t",type,"\t",request,"\033[0m"
    elif "Request" in type:
        colornum = 92
        print "\033[",colornum,"m",address[0],"\t",type,"\t",request,"\033[0m"
    elif "Reset" in type:
        colornum = 93
        print "\033[",colornum,"m",address[0],"\t",type,"\t",request,"\033[0m"

    #print "\033[",colornum,"m",address[0],"\t",type,"\t",request,"\033[0m"

# Proxy_thread definition:
# A thread to handle request from browser
def proxy_thread(connection, client_addr):

    # get the request from browser
    request = connection.recv(Size_of_max_data)

    # parse the first line
    first_line = request.split('\n')[0]

    # get url
    url = first_line.split(' ')[1]

    printout(" Request ",first_line,client_addr)
    # print "URL:",url
    # print
    
    # find the webserver and port
    http_pos = url.find("://")   
    # find function to find the position of  of ://       
    if (http_pos==-1):
        temp = url
    else:
        # assign the rest of url to to temp variable
        temp = url[(http_pos+3):]       
    
    # to find the port pos from url ans assigning it to port_pos (if any)
    port_pos = temp.find(":")           

    # find end of web server
    webserver_pos = temp.find("/")
    if webserver_pos == -1:
        webserver_pos = len(temp)

    webserver = ""
    port = -1
    if (port_pos==-1 or webserver_pos < port_pos):      # default port
        port = 80
        webserver = temp[:webserver_pos]
    else:       # specific port
        port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
        webserver = temp[:port_pos]

    try:
        # This portion of the code is used to create and connect to the socket of webserver
        # Create a socket to connect to the web server
        socketName = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

        #To create a TCP three way handshake : the client socket is connected to the werbserver and the port:
        socketName.connect((webserver, port))
        socketName.send(request)         # send request to webserver
        
        while 1:

            # This command is used to receive the receive data from web server
            data = socketName.recv(Size_of_max_data)

            # to copy the number from url from index 9 to 11 into the variable temp1
            temp1=data[9:12]

            #to check for Caching and error's
            if( temp1 == "304"):
                data= "Not Import"
                connection.send(data)
            elif (len(data) > 0):
                # send to browser
                connection.send(data)
            else:
                break
        socketName.close()
        connection.close()
    except socket.error, (value, message):
        if socketName:
            socketName.close()
        if connection:
            connection.close()
        sys.exit(1)
#********** END PROXY_THREAD ***********
    
if __name__ == '__main__':
    main()


