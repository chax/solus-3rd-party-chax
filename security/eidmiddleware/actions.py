#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()
Release = get.srcRELEASE()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf certiliamiddleware_%s-%s_amd64.deb" % (Version, Release))
    shelltools.system("zstd -d data.tar.zst")
    shelltools.system("tar xf data.tar")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "opt")
