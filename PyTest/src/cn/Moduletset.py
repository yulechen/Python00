# -*- coding: UTF-8 -*-
'''
Created on 2016年11月3日

@author: Huoyunren
'''
import com.ClassTest

def importTest():
 com.ClassTest.comTest()  
def main1():   
     emp1 = com.ClassTest.Employee("Zara", 2000)
     emp2 = com.ClassTest.Employee("Manni", 5000)
     emp1.displayEmployee()  
     emp2.displayEmployee()
     print "Total Employee %d" % com.ClassTest.Employee.empCount
     importTest()
if __name__ == '__main__':
        main1()
