#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:23:56 2021

@author: hyowon
"""


class HashOpenAddr:

	def __init__(self, size=10):
		self.size = size
		self.keys = [None] * self.size
		self.values = [None] * self.size

	def __str__(self):
		s = ""
		for k in self:
			if k == None:
				t = "{0:5s}|".format("")
			else:
				t = "{0:-5d}|".format(k)
			s = s + t
		return s

	def __iter__(self):
		for i in range(self.size):
			yield self.keys[i]

	def find_slot(self, key):
		i = self.hash_function(key)
		start = i
		while self.keys[i] is not None and self.keys[i] != key:
			i = (i + 1) % self.size
			if i == start:
				return "Full"
		return i

	def set(self, key, value=None):
		i = self.find_slot(key)
		if i == "Full":
			return None
		elif self.keys[i] is not None:
			self.values[i] += 1
			# self.values[i] = value
		else:
			self.keys[i] = key
			self.values[i] = 1
			# self.values[i] = value
		return key

	def hash_function(self, key):
		return key % self.size


	def remove(self, key):
		# print("remove({0})".format(key))
		i = self.find_slot(key)
		# print("i = {0}".format(i))
		if self.keys[i] == None:
			return None
		j = i
		while True:
			self.keys[i] = None
			while True:
				j = (j + 1) % self.size
				# print("j = {0}".format(j))
				# print("self.keys[{0}] == {1}".format(j, self.keys[j]))
				if self.keys[j] == None:
					return key
				k = self.hash_function(self.keys[j])
				# print("k = {0} : k i j = {1} {2} {3}".format(k, k, i, j))
				if k <= i <= j or (k > 0 and j == 0 and i == self.size - 1) or i < j < k:
					# if k <= i <= j or j <= k <= i or i < j < k:
					break
			# print("######## {0} <- {1}".format(i, j))
			self.keys[i] = self.keys[j]
			i = j

	def search(self, key):
		i = self.find_slot(key)
		if self.keys[i] == None:
			return None
		else:
			return key

	def __getitem__(self, key):
		return self.search(key)

	def __setitem__(self, key, value):
		self.set(key, value)


H = HashOpenAddr()


# while True:r
#	 cmd = input().split()
def runCommand(str):
	cmd = str.split(' ')
	if cmd[0] == 'set':
		key = H.set(int(cmd[1]))
		if key == None:
			print("* H is full!")
		else:
			print("+ {0} is set into H".format(cmd[1]))
	elif cmd[0] == 'search':
		key = H.search(int(cmd[1]))
		if key == None:
			print("* {0} is not found!".format(cmd[1]))
		else:
			print(" * {0} is found!".format(cmd[1]))
	elif cmd[0] == 'remove':
		key = H.remove(int(cmd[1]))
		if key == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			print("- {0} is removed".format(cmd[1]))
	elif cmd[0] == 'print':
		print(H)
	# elif cmd[0] == 'exit':
	#	 break
	else:
		print("* not allowed command. enter a proper command!")


runCommand("set 5")
runCommand("set 3")
runCommand("set 13")
runCommand("set 23")
runCommand("set 23")
runCommand("set 33")
runCommand("set 43")
runCommand("set 36")
runCommand("set 55")
runCommand("set 65")
runCommand("set 75")
runCommand("set 85")
runCommand("print")
runCommand("remove 3")
runCommand("print")
runCommand("remove 13")
runCommand("print")
runCommand("remove 43")
runCommand("print")
runCommand("remove 65")
runCommand("print")
runCommand("search 2")
runCommand("search 22")
runCommand("search 65")
runCommand("search 55")
runCommand("search 75")
runCommand("set 10")
runCommand("print")
runCommand("set 23")
runCommand("print")
runCommand("set 123")
runCommand("print")
runCommand("set 223")
runCommand("print")
runCommand("set 13")
runCommand("print")
runCommand("remove 10")
runCommand("print")

