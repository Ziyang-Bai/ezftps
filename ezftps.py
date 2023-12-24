from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import configparser
import os
import sys
config = configparser.ConfigParser()
if not os.path.exists('settings.ini'):
    print("settings file not found")
    print('Please refer to the readme.md file for more information')
    sys.exit()

config.read('settings.ini')


try:
    for section in ['Credentials']:
        uName = config[section]['username']
        Pwd = config[section]['password']
        pAth = config[section]['path']
        Perm_F = config[section]['perm']
    for section in ['Server']:
        file_encoding = config[section]['file_encoding']
        serve_port = config[section]['serve_port']
        server_ip = config[section]['server_ip']
    status = 1
except:
    print("Error reading settings file")
    print('Please refer to the readme.md file for more information')
    status = 0
if status == 0:
    sys.exit()
authorizer = DummyAuthorizer()
authorizer.add_user(uName, Pwd, pAth, perm=Perm_F)
handler = FTPHandler
handler.authorizer = authorizer
handler.encoding = file_encoding
server = FTPServer((server_ip, int(serve_port)), handler)
server.serve_forever()