# -*- coding: utf-8 -*-

print u'輸入一個數字'
num=input()
sum=0
for y in range(1,num+1):
    if num%y==0:
	sum=sum+1	 
if sum==2:
	print u'%d為質數' %num
else:
	print u'%d不是質數' %num
 