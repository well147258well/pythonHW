#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
print "歡迎遊玩終極密碼"
num=input('請輸入1-99中一個數字')
a=1
b=99
bomb=random.randint(1,99)

sum=0
for x in range(1,100):
	if num>bomb:
		print '密碼介於%d到%d間' %(a,num)
		b=num
		sum=sum+1
		num=input("請輸入下一個數字")
		
	elif num<bomb:
		print '密碼介於%d到%d間' %(num,b)
		a=num
		sum=sum+1
		num=input("請輸入下一個數字")
		
	else:
		print '你輸了'
		break
	


