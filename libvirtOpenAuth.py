
from __future__ import print_function
import sys
import libvirt

SASL_USER = "antonio"
SASL_PASS = "lg775n"

def request_cred(credentials, user_data):
 for credential in credentials:
  if credential[0] == libvirt.VIR_CRED_AUTHNAME:
   credential[4] == SALS_USER
  elif credential[0] == libvirt.VIR_CRED_PASSPHRASE:
   credential[4] == SALS_PASS
 return 0

auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE], request_cred, None]

conn1 = libvirt.openAuth('qemu+ssh://antonio@lab0/system', auth, 0)
if conn1 == None:
 print('Failed to opne', file=sys.stderr)
 exit(1)
print('connection Successfull')
conn1.close()
print('conn1 Closed')
conn0 = libvirt.openAuth('qemu+ssh://antonio@lab1/system', auth, 0)
if conn0 == None:
 print('Failed to opne', file=sys.stderr)
 exit(1)
print('connection Successfull')
conn0.close()
print('conn0 Closed')
exit(0)

