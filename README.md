# ezftps
A FTP server based Python3

English [简体中文](README_cn.md "The Chinese version of this manual")。

# 1.Instructions for use

It should be noted that even the distribution version does not support instant use, and you need to make certain configurations

If the program does not correctly read the configuration file, the program will not be able to start.

Typically, configuration files should be written in this way



[Credentials]

username = Jing

password = jian

path = ./ftp/

perm = elradfmwM

[Server]

file_encoding = utf-8

serve_port = 8888

server_ip = 0.0.0.0



The perm parameter is optional. If not provided, it defaults to 'elradfmwM'. This string represents the permissions that the user has, as shown below:

e: Allow users to log in

l: Allow users to view directories

r: Allow users to download files

d: Allow users to create directories

f: Allow users to upload files

m: Allow users to delete files

w: Allow users to write files

M: Allow users to execute commands

For example, if the perm parameter is set to 'elr', users can only log in, view directories, and download files. If you want to add more permissions to users, you can add them in the perm parameter.



# 2.Dependencies

pyftpdlib.handlers

pyftpdlib.servers

pyftpdlib.authorizers

configparser

os

If you are using a preview version or a non encapsulated version, you will need to manually install them. If it is a preview version, you may need some other modules



# 3.Credits

Codeing - Jing_jian

DBG - TingkeLee



