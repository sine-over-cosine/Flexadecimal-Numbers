#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:28:07 2020

@author: russell_tan
"""


def factorial(n):
    number=1
    if n == 0 or n ==1 :
        return 1
    else:
        while(n>1):
            number*=n
            n-=1
    return number

    
class Number:
    def __init__(self,number):
        self.number=number
        
    def __str__(self):
        return "<"+self.number+">"
    
    def decimal(self):
        number=0
        for i in range(len(self.number)-1,-1,-1):
            number+=factorial(int(self.number[i])+1)
        return number
    
class Flexadecimal(Number):
    def __init__(self,number):
        self.number=number
        self.flexadecimal=self.flexadecimal()
    
    def __str__(self):
        return "<"+self.flexadecimal()+">"
    
    def __repr__ (self):
        return "<"+self.flexadecimal()+">"
    
    def flexadecimal(self):
        flexadecimal=[]
        quotient=int(self.number)
        divisor=2
        while(quotient != 0):
            remainder=quotient%divisor
            quotient=quotient//divisor
            divisor+=1
            flexadecimal=[remainder]+flexadecimal
        string_format=""
        for i in range(0,len(flexadecimal)):
            string_format+=str(flexadecimal[i])
            
        return string_format
    
    def addition(self,other):
        carry=0
        new=[]
        f1=self.flexadecimal[::-1]
        f2=other[::-1]
        placing=max(len(f1),len(f2))
        if len(f2)>len(f1):
            f1+=[0]*(len(f2)-len(f1))
        elif len(f2)<=len(f1):
            f2+=[0]*(len(f1)-len(f2))
        for i in range(0,len(f1)):
            if int(f1[i])+int(f2[i])+carry>placing:
                new.append(int(f1[i])+int(f2[i])+carry-placing-1)
                carry=1
                placing
            else:
                new.append(int(f1[i])+int(f2[i])+carry)
                carry=0
            
        
        
        
        
        

