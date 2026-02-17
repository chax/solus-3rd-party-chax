#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("tar xf libfprint-2-tod1-goodix_0.0.6.orig.tar.gz")

def install():
    pisitools.insinto("/usr/lib/libfprint-2/tod-1/", "usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/*.so")
    pisitools.insinto("/usr/lib/udev/rules.d/", "lib/udev/rules.d/*.rules")
