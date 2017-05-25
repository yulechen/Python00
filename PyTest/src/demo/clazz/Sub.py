# -*- coding: UTF-8 -*-
'''
Created on 2017年5月3日

@author: Huoyunren
'''
from demo.clazz.Parent import Parent

DEFAULT_ERROR_MESSAGE = '''\
<head>
<title>Error response</title>
</head>
<body>
<h1>Error response</h1>
<p>Error code %(code)d.
<p>Message: %(message)s.
<p>Error code explanation: %(code)s = %(explain)s.
</body>
'''

class Sub(Parent):
    '''
    classdocs
    '''      
# def __init__(self):
#     print 'sub cons'
          
    def b(self):
        print 'sub b '    
        
if __name__ == '__main__':
    print DEFAULT_ERROR_MESSAGE
