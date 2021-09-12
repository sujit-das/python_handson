#!/usr/bin/env python
import os

if __name__ == "__main__":
   x=5
   assert(x==5), 'comparison failed.value received = {}'.format(x)
   print('OK: 1st comparison passed\n')

   assert(x==8), '2nd comparison failed.value received = {}'.format(x)
