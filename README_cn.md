# ezftps

A FTP server based Python3

简体中文 [English](README.md "The English version of this manual")。
# 1.使用说明

需要注意的是，即使是发行版也不支持即时使用，您需要进行某些配置

如果程序不能正确读取配置文件，程序将无法启动。

通常，配置文件应该这样编写

[Credentials]

username = Jing

password = jian

path = ./ftp/

perm = elradfmwM

[Server]

file_encoding = utf-8

serve_port = 8888

server_ip = 0.0.0.0


perm 参数为可选参数。如果未提供，默认值为 "elradfmwM"。该字符串表示用户拥有的权限，如下所示：

e: 允许用户登录

l: 允许用户查看目录

r: 允许用户下载文件

d: 允许用户创建目录

f: 允许用户上传文件

m: 允许用户删除文件

w: 允许用户写入文件

M： 允许用户执行命令

例如，如果 perm 参数设置为 "elr"，用户只能登录、查看目录和下载文件。如果要为用户添加更多权限，可以在 perm 参数中添加。

# 2.依赖关系

pyftpdlib.handlers

pyftpdlib.servers

pyftpdlib.authorizers

configparser

os

如果您使用的是预览版或非封装版本，则需要手动安装它们。如果是预览版，可能还需要一些其他模块

# 3.贡献

代码编写 - Jing_jian

除虫 - TingkeLee
