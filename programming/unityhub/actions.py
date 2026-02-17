#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf UnityHubSetup-%s-amd64.deb" % Version)
    shelltools.system("tar xf data.tar.*")

def install():
    shelltools.system("sed -e '/TryExec=unityhub/d' -i usr/share/applications/unityhub.desktop")

    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")

    pisitools.dosym("/opt/unityhub/unityhub", "/usr/bin/unityhub")
