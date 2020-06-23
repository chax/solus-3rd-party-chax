#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("tar xzvf imagescan-bundle-*.x64.deb.tar.gz")
    shelltools.system("ar x imagescan-bundle-*.x64.deb/plugins/imagescan-plugin-networkscan_*_amd64.deb data.tar.xz")
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/usr/lib64/utsushi", "usr/lib/utsushi/networkscan")
