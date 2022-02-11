
# 0x07 - Networking basics #0


## General

### OSI Model

* What it is
* How many layers it has
* How it is organized


### What is a LAN

* Typical usage
* Typical geographical size


### What is a WAN

* Typical usage
* Typical geographical size


### What is the internet

* What is an IP address
* What are the two types of IP addresses
* What is `localhost`
* What is a subnet
* Why IPv6 was created


### TCP/UDP

* What two data transfer protocols are mainly used for IP
* What is the main difference between TCP and UDP
* What is a port
* Memorize SSH, HTTP, and HTTPS port numbers
* What tool/protocol is often used to check if a device is connected to a network


#### More Info

The second line of all your Bash scripts should be a comment explaining 
what the script is doing.

For multiple choice questions, just type the number of the correct 
answer in your answer file, adding a new line for each answer.

Example:

What is the most important position in a software company?

1. Project manager
2. Backend developer
3. System administrator
```
    user@computer$ cat your_answer_file
    3
    user@computer$
```


#### The OSI Model

The OSI model can be memorized by this phrase:
    **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

Whereas the model looks like this, and is organized from the lowest layer 
to the highest layer:

| Layer 7 | Data | Application | FTP, HTTP, SMTP |
| Layer 6 | Data | Presentation | jpeg, mpeg, gif|
| Layer 5 | Data | Session | Apple talk |
| Layer 4 | Segments | Transport | TCP, UDP |
| Layer 3 | Packets | Network | IP, IPX, ICMP |
| Layer 2 | Frame | Data Link | PPP, Ethernet |
| Layer 1 | Bits | Physical | Ethernet, USB |

The OSI model is completely conceptual, and is designed to show the flow of 
data in a communication system by breaking down the process into seven abstraction
layers. 
