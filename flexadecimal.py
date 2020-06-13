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

    

    
class Flexadecimal():
    def __init__(self,number):
        self.number=number
        self.flexadecimal=self.flexadecimal()
    
    def __str__(self):
        return "<"+self.flexadecimal+">"
    
    def __repr__ (self):
        return self.flexadecimal
    
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
        placing=1
        if len(f2)>len(f1):
            f1+="0"*(len(f2)-len(f1))
        elif len(f2)<=len(f1):
            f2+="0"*(len(f1)-len(f2))
        for i in range(0,len(f1)):
            if int(f1[i])+int(f2[i])+carry>placing:
                new.append(int(f1[i])+int(f2[i])+carry-placing-1)
                carry=1
                placing+=1
            else:
                new.append(int(f1[i])+int(f2[i])+carry)
                carry=0
                placing+=1
        string=""
        for j in range(len(new)-1,-1,-1):
            string+=str(new[j])
        return string
    
class Flex_to_Dec():
    def __init__ (self,number):
        self.flexadecimal=number
        
    def decimalise(self):
        n=0
        fact=1
        for i in range(len(self.flexadecimal)-1,-1,-1):
            n+= int(self.flexadecimal[i])*factorial(fact)
            fact+=1
        return n
    
    def __str__(self):
        return self.decimalise()
    
f=Flexadecimal(41)
print("41 in flexadecimal form is ",f.flexadecimal," otherwise: ",f)
g=Flexadecimal(13).flexadecimal
print("13 in flexadecimal form is ",g," otherwise: ",Flexadecimal(13))
result=f.addition(g)
print("The result of adding ",f.flexadecimal," and ",g," is ",result," otherwise: <",result,">")

print("The result is in turn : ",Flex_to_Dec(result).decimalise())

       
"""
Output:
41 in flexadecimal form is  1221  otherwise:  <1221>
13 in flexadecimal form is  201  otherwise:  <201>
The result of adding  1221  and  201  is  2100  otherwise: < 2100 >
The result is in turn :  54
"""
            
        
        
        
        
        

