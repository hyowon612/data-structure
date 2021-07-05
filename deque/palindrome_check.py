#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 18:45:34 2021

@author: hyowon
"""


class deque:
	items = []
	
	def __init__(self, s):
		self.items = list(s)
	
	def append(self, c):
		self.items.append(c)

	def appendleft(self, c):
		self.items.appendleft(c)

	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty")

	def popleft(self):
		try:
			return self.items.popleft()
		except IndexError:
			print("Stack is empty")

	def __len__(self):
		return len(self.items)
	
	def right(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")

	def left(self):
		try:
			return self.items[0]
		except IndexError:
			print("Stack is empty")
		

def check_palindrome(s):
	dq = deque(s)
	palindrome = True
	while len(dq) > 1:
		if dq.popleft() != dq.pop():
			palindrome = False
	return palindrome


A = input()

print(check_palindrome(A))
