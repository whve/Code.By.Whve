#import pkg0.m1
#pkg0.m1.echo()

#from pkg0 import m1
#m1.echo()

import sys
sys.path += ['./', 'pkg2']

import pkg1.m1
import pkg1.m2
import pkg1.m3

pkg1.m1.echo()
pkg1.m2.echo()
pkg1.m3.echo()
