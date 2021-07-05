#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:46:26 2021

@author: hyowon
"""


class Stack:
	def __init__(self):
		self.items = []
		
	def push(self, val):
		self.items.append(val)
			
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty")
			
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty")
			
	def __len__(self):
		return len(self.items)

	def isEmpty(self):
		return self.__len__() == 0
		

def get_token_list(expr):
	a = []
	token_list = []
	for token in expr:
		if token in '+-*/^()':
			if len(a) != 0:
				token_list.append(float(''.join(a)))
				a = []
			token_list.append(token)
		elif token == " ":
			continue
		else:
			a.append(token)
	if len(a) != 0:
		token_list.append(float(''.join(a)))

	return token_list
	
def infix_to_postfix(token_list):
	opstack = Stack()
	outstack = []
	
	prec = {}
	prec['('] = 0
	prec['+'] = 1
	prec['-'] = 1
	prec['*'] = 2
	prec['/'] = 2
	prec['^'] = 3

	for token in token_list:
		if type(token) == float:
			outstack.append(token)
		elif token == '(':
			opstack.push(token)
		elif token == ')':
			while not opstack.top() == '(':
				outstack.append(opstack.pop())
			opstack.pop()
		elif token in '+-/*^':
			if opstack.isEmpty() or prec[token] > prec[opstack.top()]:
				opstack.push(token)
			elif prec[token] <= prec[opstack.top()]:
				while prec[token] <= prec[opstack.top()]:
					outstack.append(opstack.pop())
					if len(opstack) == 0:
						break
				opstack.push(token)
#		elif type(token) == float: # operand일 때
#			outstack.append(token)

	while not opstack.isEmpty():
		outstack.append(opstack.pop())
	
	return list(outstack)

def compute_postfix(token_list):
	opstack = Stack()
	for token in token_list:
		if token == '+':
			a = opstack.pop()
			b = opstack.pop()
			opstack.push(b+a)
		elif token == '-':
			a = opstack.pop()
			b = opstack.pop()
			opstack.push(b-a)	
		elif token == '*':
			a = opstack.pop()
			b = opstack.pop()
			opstack.push(b*a)
		elif token == '/':
			a = opstack.pop()
			b = opstack.pop()
			opstack.push(b/a)
		elif token == '^':
			a = opstack.pop()
			b = opstack.pop()
			opstack.push(b^a)
		elif token == ' ':
			continue
		else:
			opstack.push(token)
	return opstack.pop()

	
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
