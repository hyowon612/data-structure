#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 17:59:48 2021

@author: hyowon
"""


# 1. class Node 선언 부분
class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self
    def __str__(self):
        return str(self.key)

# 2. class DoublyLinkedList 선언부분
class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # create an empty list with only dummy node

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
    def __str__(self):
        return " -> ".join(str(v.key) for v in self)
    def printList(self):
        v = self.head.next
        print("h -> ", end="")
        while v != self.head:
            print(str(v.key)+" -> ", end="")
            v = v.next
        print("h")

    def strList(self):
        s = "";
        v = self.head.next
        s += "h -> "
        while v != self.head:
            s += str(v.key) + " -> "
            v = v.next
        s += "h"
        return s

    def splice(self, a, b, x):
        v = a
        while v != self.head:
            v = v.next
            if v == b:
                ap = a.prev
                bn = b.next
                xn = x.next
                ap.next = bn
                bn.prev = ap
                x.next = a
                a.prev = x
                xn.prev = b
                b.next = xn
                break

    def moveAfter(self, a, x):
        self.splice(a, a, x)

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)

    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def deleteNode(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x

    def popFront(self):
        if self.head.next == None:
            return None
        frontnode = self.head.next
        self.deleteNode(self.head.next)
        return frontnode

    def popBack(self):
        if self.head.prev == None:
            return None
        backnode = self.head.prev
        self.deleteNode(self.head.prev)
        return backnode

    def search(self, key):
        v = self.head.next
        while v != self.head:
            if v.key == key:
                return v
            v = v.next
        return None

    def first(self):
        return self.head.next.key

    def last(self):
        return self.head.prev.key

    def isEmpty(self):
        return self.head.next == self.head




L = DoublyLinkedList()
# while True:
#     cmd = input().split()
def runCommand(command, result):
    cmd = command.split(' ')
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    # elif cmd[0] == 'exit':
    #     break
    else:
        print("* not allowed command. enter a proper command!")

    if (L.strList() != result):
        print("############# Error found {0} ##############".format(command))
        print("expect {0}".format(result))
        print("result {0}".format(L.strList()))


runCommand("print", "h -> h")
runCommand("pushF 2", "h -> 2 -> h")
runCommand("pushF 1", "h -> 1 -> 2 -> h")
runCommand("pushB 3", "h -> 1 -> 2 -> 3 -> h")
runCommand("pushB 4", "h -> 1 -> 2 -> 3 -> 4 -> h")
runCommand("popF", "h -> 2 -> 3 -> 4 -> h")
runCommand("popB", "h -> 2 -> 3 -> h")
runCommand("popF", "h -> 3 -> h")
runCommand("popB", "h -> h")
runCommand("popF", "h -> h")
runCommand("popB", "h -> h")
runCommand("first", "h -> h")
runCommand("last", "h -> h")
runCommand("pushF 2", "h -> 2 -> h")
runCommand("pushF 1", "h -> 1 -> 2 -> h")
runCommand("pushB 3", "h -> 1 -> 2 -> 3 -> h")
runCommand("pushB 4", "h -> 1 -> 2 -> 3 -> 4 -> h")
runCommand("first", "h -> 1 -> 2 -> 3 -> 4 -> h")
runCommand("last", "h -> 1 -> 2 -> 3 -> 4 -> h")
runCommand("insertA 1 11", "h -> 1 -> 11 -> 2 -> 3 -> 4 -> h")
runCommand("insertA 3 13", "h -> 1 -> 11 -> 2 -> 3 -> 13 -> 4 -> h")
runCommand("insertA 4 14", "h -> 1 -> 11 -> 2 -> 3 -> 13 -> 4 -> 14 -> h")
runCommand("insertB 1 91", "h -> 91 -> 1 -> 11 -> 2 -> 3 -> 13 -> 4 -> 14 -> h")
runCommand("insertB 2 92", "h -> 91 -> 1 -> 11 -> 92 -> 2 -> 3 -> 13 -> 4 -> 14 -> h")
runCommand("insertB 14 94", "h -> 91 -> 1 -> 11 -> 92 -> 2 -> 3 -> 13 -> 4 -> 94 -> 14 -> h")
