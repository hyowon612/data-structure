#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:55:28 2021

@author: hyowon
"""


class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None

	def __str__(self):
		return str(self.key)


class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def __len__(self):
		return self.size

	def printList(self):  # 변경없이 사용할 것!
		v = self.head
		while (v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")

	def pushFront(self, key):
		node = Node(key)
		node.next = self.head
		self.head = node
		self.size += 1

	def pushBack(self, key):
		if self.size == 0:
			self.head = Node(key)
		else:
			node = self.head
			while node.next != None:
				node = node.next
			node.next = Node(key)
		self.size += 1

	def popFront(self):
		if self.size == 0:
			return None
		else:
			key = self.head.key
			self.head = self.head.next
			self.size -= 1
			return key

	def popBack(self):
		if self.size == 0:
			return None
		elif self.size == 1:
			self.size -= 1
			key = self.head.key
			self.head = None
			return key
		else:
			node = self.head
			while node.next != None:
				prev = node
				node = node.next
			prev.next = None
			self.size -= 1
			return node.key

	def search(self, key):
		node = self.head
		while node != None and node.key != key:
			node = node.next
		if node == None:
			return None
		else:
			return node

	def remove(self, x):
		node = self.head
		prev = None
		while node != None and node != x:
			prev = node
			node = node.next
		if node == None:
			return False
		elif prev == None:
			self.head = node.next
		else:
			prev.next = node.next
		self.size -= 1
		return True

	def reverse(self, key):
		node = self.head
		prev = None
		while node.key != key:
			prev = node
			node = node.next
		if node == None:
			return
		rnode = None
		while node != None:
			oldrnode = rnode
			rnode = Node(node.key)
			rnode.next = oldrnode
			node = node.next
		if prev == None:
			self.head = rnode
		else:
			prev.next = rnode

	def findMax(self):
		node = self.head
		maxkey = self.head.key
		if self.size == 0:
			return None
		while node.next != None:
			node = node.next
			if node.key >= maxkey:
				maxkey = node.key
		return maxkey

	# self가 empty이면 None, 아니면 max key 리턴

	def deleteMax(self):
		if self.size == 0:
			return None
		else:
			maxkey = self.findMax()
			node = self.search(maxkey)
			self.remove(node)
			return maxkey

	# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴

	def insert(self, k, val):
		node = self.head
		newnode = Node(val)
		if self.size <= k:
			self.pushBack(val)
			return
		for i in range(k):
			prev = node
			node = node.next
		prev.next = newnode
		newnode.next = node

	def size(self):
		return self.size


# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1] + "-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")