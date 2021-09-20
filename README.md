# webserv_tester

A python tester for our [webserv project](https://github.com/lmalki-h/webserv)

  
  
## Features
//TODO: List what the server tests
## Install

To test your server, run your server first, then execute the following command after replacing the [host] and [port]  with those of your server.

    $ git clone https://github.com/lmalki-h/webserv_tester.git
    $ cd webserv_tester
    $ pip install -r requirements.txt
    $ ./main.py -h

 
Alternatively, build a Docker image from the source to ensure all the dependencies are available and run tester script inside.

	$ docker network create webserv-network
    $ docker build -t webserv_tester .
    $ docker run -d --network=webserv-network --name=tester -p 4242:4242 webserv_tester
