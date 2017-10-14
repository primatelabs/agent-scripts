#!/usr/bin/env python

# Agent Scripts
#
# Copyright (C) 2004-2017 Primate Labs Inc.  All rights reserved.

import os, subprocess, sys

def shutdown_linux():
  subprocess.call(['sudo', 'shutdown', '-h', '+1'])

def shutdown_macosx():
  subprocess.call(['sudo', 'shutdown', '-h', '+1'])

def shutdown_windows():
  subprocess.call([
    'reg.exe', 'ADD', 'HKCU\Software\Sysinternals\PsShutdown',
    '/v', 'EulaAccepted',
    '/t', 'REG_DWORD',
    '/d', '1',
    '/f'])
  subprocess.call([
    'windows\\psshutdown.exe', '-k'
  ])


def main():
  platforms = {
    'darwin' : 'macosx',
    'linux2' : 'linux',
    'win32' : 'windows',
  }

  force = False
  if force or (os.environ.has_key('AGENT_SHUTDOWN') and int(os.environ['AGENT_SHUTDOWN'])):
    print "shutdown"
    platform = platforms[sys.platform]
    globals()[ 'shutdown_%s' % (platform,) ]()

if __name__ == '__main__':
  main()
