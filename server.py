#/***************************************************************************
# Filename        : server.py
# Author          : Jishnu M Thampan
# Description     : Simple script to host your workspace into an ftp server.
#					Server could be accessible by navigating to locaalhost:80
#***************************************************************************/

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port   = 80    
os.chdir(webdir)                                       
srvraddr = ("", port)                                  # hostname and portnumber
srvrobj  = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()                                # run until user closes
