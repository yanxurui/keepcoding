#!/usr/bin/env
# coding=utf-8

import subprocess
p = subprocess.Popen(['python', 'cmd.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print('stdout: %s\nstderr: %s' % p.communicate())
print('return code: %d' % p.returncode)
