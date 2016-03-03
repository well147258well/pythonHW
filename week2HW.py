# -*- coding: utf-8 -*-
#coding=utf-8
a=5000
print u'您的存款有%d' %a
print u'請問要領多少錢'
money=input()
num=int(money)
if num>5000:
  print u'您的存款不足'
  f=open("ATM.txt","a")
  f.write("您的存款不足")
if num==5000:
  print u'您存款剩餘為0'
  f=open("ATM.txt","a")
  f.write("您存款剩餘為0")
if num<5000: 
  print u'您的存款剩下%d' %(5000-money)
  b=5000-money
  f=open("ATM.txt","a")
  f.write("您的存款剩下%s"%(b))
  
