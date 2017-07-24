#!/usr/bin/env python

# Agent Scripts
#
# Copyright (C) 2004-2017 Primate Labs Inc.  All rights reserved.

import os, subprocess, sys

def sleep_linux():
  # TODO
  pass

def sleep_macosx():
  subprocess.call(['pmset', 'sleepnow'])

def sleep_windows():
  subprocess.call([
    'reg.exe', 'ADD', '"HKCU\Software\Sysinternals\PsShutdown"',
    '/v', 'EulaAccepted',
    '/t', 'REG_DWORD',
    '/d', '1',
    '/f'])
  subprocess.call([
    'windows\\psshutdown.exe', '-d', '-t', '0'
  ])


def main():
  platforms = {
    'darwin' : 'macosx',
    'linux2' : 'linux',
    'win32' : 'windows',
  }

  force = True

  if force or (os.environ.has_key('AGENT_SLEEP') and int(os.environ['AGENT_SLEEP'])):
    print "shutdown"
    platform = platforms[sys.platform]
    globals()[ 'sleep_%s' % (platform,) ]()

if __name__ == '__main__':
  main()
