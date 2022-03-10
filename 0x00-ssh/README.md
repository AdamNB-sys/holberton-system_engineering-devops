# 0x00 SSH


## General


    This project is a good refresher of SSH, SSH RSA key pairs, and how to
    connect to a remote host using SSH RSA key pairs. As well as:

    * What is a server
    * Where servers usually live
    * The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`


## Tasks

0. Use a private key

    Write a bash script that uses `ssh` to connect to your server using the
    private key `~/.ssh/school` with the user `ubuntu`.

1. Create an SSH key pair

    Write a bash script that creates an RSA key pair

2. Client configuration file

    Your machine has an SSH configuration file for the local SSH client, 
    let's configure it to our needs to that you can connect to a server
    without typing a password. Share your SSH client configuration in your
    answer file.

    Requirements:
    * Your SSH client configuration must be configured to use the private key `~/.ssh/school`
    * Your SSH client configuration must be configured to refuse to authenticate using a password

3. Let me in!

    Add the SSH key from Holberton to allow them to access your server using the
    `ubuntu` user.
