
from __future__ import print_function
import sys
import libvirt
conn1 = libvirt.open('qemu+ssh://antonio@lab0/system')
if conn1 == None:
 print('Failed to opne', file=sys.stderr)
 exit(1)
print('connection Successfull')
conn1.close()
print('conn1 Closed')
conn0 = libvirt.open('qemu+ssh://antonio@lab1/system')
if conn0 == None:
 print('Failed to opne', file=sys.stderr)
 exit(1)
print('connection Successfull')
conn0.close()
print('conn0 Closed')
exit(0)

