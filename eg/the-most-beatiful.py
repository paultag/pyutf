#!/usr/bin/env pyutf

print "e^πi + 1", "≠" if round((e**(π*1j)+1).imag) else "=", "0"
