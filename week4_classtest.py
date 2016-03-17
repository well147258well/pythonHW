# -*- coding: utf-8 -*-

def isPrime(N):
	sum=0
	for y in range(1,N+1):   
		if N%y==0:
			sum=sum+1
	if sum==2:
		return 1
	else:
		return 0
num=0		
for x in range(2,1001):
	if isPrime(x)==1:
		num=num+x
print num