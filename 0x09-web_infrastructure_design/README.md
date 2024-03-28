# 0x09-web_infrastructure_design

## Simple web stack

A server is a computer or program can be physical or virtual that provides functionality or services to other computers, known as clients, over a network.It is located in a data center and runs an OS. It typically uses the HTTP or HTTPS protocol to communicate with the user's computer when requesting a website.
The role of a domain name is to provide a user-friendly way to navigate the internet and to map to specific IP addresses where the website's content is hosted.
The DNS record type for "www" in "www.foobar.com" is typically an "A" record (Address record) because it resolves to an IP address.
The DNS’s role is to translate the record of a domain name into an IP address.
The role of a web server is to receive requests from clients such as web browsers process those requests, and deliver web pages.
An application server hosts the software applications and business logic that handle the dynamic generation of content in response to client requests.
The role of a database is to store information such as user accounts, product details, and other application data.


## Distributed web infrastructure

The load balancer is configured with a distribution algorithm such as Round Robin and is enabling an Active-Active setup.The MySQL Master-Replica cluster used replication to keep data synchronized.The Master database node can accept reads/writes while the Replica can only accept reads

## Secured and monitored web infrastructure

Firewalls are network security devices or software that monitor and control incoming and outgoing network traffic based on predetermined security rules.
Traffic is served over HTTPS (HTTP Secure) to encrypt data transmitted between the web server and the user's browser.
Monitoring is used to track the performance, availability, and health of the infrastructure components and applications. 

## Scale up

An additional load balancer there and is configured as a cluster so that if one fails, the other takes over
