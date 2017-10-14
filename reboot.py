#!/usr/bin/env python

# Agent Scripts
#
# Copyright (C) 2004-2017 Primate Labs Inc.  All rights reserved.

import os, subprocess, sys

def reboot_linux():
  subprocess.call(['sudo', 'reboot'])

def reboot_macosx():
  subprocess.call(['sudo', 'reboot'])

def reboot_windows():
  subprocess.call([
    'reg.exe', 'ADD', 'HKCU\Software\Sysinternals\PsShutdown',
    '/v', 'EulaAccepted',
    '/t', 'REG_DWORD',
    '/d', '1',
    '/f'])
  subprocess.call([
    'windows\\psshutdown.exe', '-r'
  ])


def main():
  platforms = {
    'darwin' : 'macosx',
    'linux2' : 'linux',
    'win32' : 'windows',
  }

  print "reboot"
  platform = platforms[sys.platform]
  globals()[ 'reboot_%s' % (platform,) ]()

if __name__ == '__main__':
  main()
