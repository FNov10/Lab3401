#!/usr/bin/env python3
import cgi
import cgitb
from templates import *
import os

s = cgi.FieldStorage()
username = s.getfirst("username") 
password = s.getf

