#!/usr/bin/python

import os
import re
import sys

try:
   raw_kernel = sys.argv[1]
except:
   raw_kernel = "./zImage"

try:
   output_dir = sys.argv[2]
except:
   output_dir = "./kernel.img"

try:
   supfile_loc = sys.argv[3]
except:
   supfile_loc = "./"

re_line = re.compile(r"0x(?P<value>[0-9a-f]{8})")

mem = [0 for i in range(32768)]

def load_to_mem(name, addr):
   f = open(name)

   for l in f.readlines():
      m = re_line.match(l)

      if m:
         value = int(m.group("value"), 16)

         for i in range(4):
            mem[addr] = int(value >> i * 8 & 0xff)
            addr += 1

   f.close()

load_to_mem("%s/bcm2835-boot-uncompressed.txt" % supfile_loc, 0x00000000)
load_to_mem("%s/bcm2835-args-uncompressed.txt" % supfile_loc, 0x00000100)

f = open("%s/bcm2835-kernel-first32k.bin" % supfile_loc, "wb")
for m in mem:
   f.write(chr(m))
f.close()

os.system("cat %s/bcm2835-kernel-first32k.bin %s > %s/kernel.img" %(supfile_loc, raw_kernel, output_dir))

f = open("%s/cmdline.txt" % output_dir, "w")
f.write("root=/dev/mmcblk0p2 rootfstype=ext4 rootwait")
f.close()
