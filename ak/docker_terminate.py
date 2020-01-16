#!/usr/bin/python36
print("content-type: text/html")


import subprocess as sp
import cgi

form = cgi.FieldStorage()
cname=form.getvalue("s")
cmd="sudo docker rm -f {}".format(cname)
x=sp.getoutput(cmd)
print("location: http://192.168.43.172/cgi-bin/ak/docker_live_menu.py")
print()

