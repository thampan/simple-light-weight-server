#!/usr/bin/env python3

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port   = 80    
os.chdir(webdir)                                       
srvraddr = ("", port)                                  # hostname and portnumber
srvrobj  = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()                                # run until user closes
