#stdout test

import sys
print 'hello, world'
print 'The quick brown fox', 'jumps over', 'the lazy dog'
print '100 + 200 =', 100 + 200

#stdin test
#name = raw_input()
#print 'read name is',name

name = raw_input('please enter your name: ')
print 'hello,', name

print dir(sys)