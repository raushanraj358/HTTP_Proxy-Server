                               Indian Institute of Information Technology Allahabad
                                            NAME : Raushan Raj
                                            ROLL : IIT2018031
                                                               
                                            HTTP_Proxy_Server
   The proxy sits between the client (usually web browser) and the server (web server).
   In our simple case, the client sends all its requests to the proxy instead of sending 
   requests directly to the server. The proxy then opens a connection to the server, and 
   passes on the client’s request. Then when the proxy receives the reply from the server, 
   it sends that reply back to the client. There are several reasons we use proxy for our 
   browser: Performance (the proxy caches the pages that it fetched), Content Filtering 
   and Transformation (block access to certain domain, reformat web pages), and Privacy.
   A Multi-Threaded HTTP Proxy Server 


   SOURCE FILE : IIT2018031.py

   MULTI-THREADING ENABLED

   ONLY WORKS FOR HTTP GET METHODS( shows 501 Not Implemented for other request)

   Steps to implement a proxy server on your local machine - 

   1) Install Python 2.7.17 in your machine

   2) Got to the folder and run the python file IIT2018031.py

   3) The port number  can be set by you, If you don't set port number 8080 will be used automatically.

   4) Once the source file is running, Open Mozilla Firefox, and navigate to browser settings to get the Network proxy settings tab.  Here choose the manual proxy configuration       & enter

         - HTTP PROXY : localhost
         - Port Number : set (or any other if you have changed)

   5) Enter the desired URL & observe on the terminal (or the program output where you have run the program ) that the request will be sent to the proxy than URL is parsed and         data is fetched  from the server by the proxy & returned to the  browser.

   6) for each connection a new THREAD is opened so it will work with multiple tabs or windows of browser



   NOTE: You can comment/uncomment the print lines for showing the desired steps of the process.



