#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
print "�w��C���׷��K�X"
num=input('�п�J1-99���@�ӼƦr')
a=1
b=99
bomb=random.randint(1,99)

sum=0
for x in range(1,100):
	if num>bomb:
		print '�K�X����%d��%d��' %(a,num)
		b=num
		sum=sum+1
		num=input("�п�J�U�@�ӼƦr")
		
	elif num<bomb:
		print '�K�X����%d��%d��' %(num,b)
		a=num
		sum=sum+1
		num=input("�п�J�U�@�ӼƦr")
		
	else:
		print '�A��F'
		break
	


