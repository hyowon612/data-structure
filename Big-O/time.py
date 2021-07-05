# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random, time

def unique_n(A):
	B = [0] * (2*n+1)
	for i in range(n):
		if B[A[i]+n] == 1:
			print("NO")
			return
		B[A[i]+n] = 1
	print("YES")
	
def unique_nlogn(A):
	A.sort()
	for i in range(n-1):
		if A[i+1] <= A[i]:
			print("NO")
			return
	print("YES")

def unique_n2(A):
	for i in range(n):
		for j in range(i+1, n):
			if A[i] == A[j]:
				print("NO")
				return
	print("YES")

n = 10000
result = []

while n <= 100000:
	A = random.sample(range(-n, n+1), n)
	
	s1 = time.process_time()
	unique_n(A)
	e1 = time.process_time()

	s2 = time.process_time()
	unique_nlogn(A)
	e2 = time.process_time()

	s3 = time.process_time()
	unique_n2(A)
	e3 = time.process_time()
    
	result.append([n, e1-s1, e2-s2, e3-s3])
	
	n +=10000
    
print(result)
