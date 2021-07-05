class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None
		self.height = 0  # 높이 정보도 유지함에 유의!!

	def __str__(self):
		return str(self.key)


class BST:
	def __init__(self):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def preorder(self, v):
		if v:
			print(v.key, end=' ')
			self.preorder(v.left)
			self.preorder(v.right)

	def inorder(self, v):
		if v:
			self.inorder(v.left)
			print(v.key, end=' ')
			self.inorder(v.right)

	def postorder(self, v):
		if v:
			self.postorder(v.left)
			self.postorder(v.right)
			print(v.key, end=' ')

	def find_loc(self, key):
		if self.size == 0: return None
		p = None
		v = self.root
		while v:
			if v.key == key:
				return v
			else:
				if v.key < key:
					p = v
					v = v.right
				else:
					p = v
					v = v.left
		return p

	def search(self, key):
		p = self.find_loc(key)
		if p and p.key == key:
			return p
		else:
			return None

	def insert(self, key):
		v = Node(key)
		if self.size == 0:
			self.root = v
		else:
			p = self.find_loc(key)
			if p and p.key != key:
				if p.key < key:
					p.right = v
				else:
					p.left = v
				v.parent = p
			q = v
			if p.height == 0:
				while p.height == q.height:
					p.height += 1
					if p == self.root:
						break
					q = p
					p = p.parent
		self.size += 1
		return v
	# 노드들의 height 정보 update 필요

	def deleteByMerging(self, x):
		if x == None:
			return None
		a, b, pt = x.left, x.right, x.parent
		if a == None:
			c = b
			q = pt
			if b == None:
				p = x
				if q.height - p.height == 1:
					q.height = 0
					while q.parent.height - q.height == 2:
						p = q
						q = q.parent
						if q.left and q.right and q.height - q.left.height ==1 or q.height - q.right.height == 1:
							break
						if q == self.root:
							break
						q.height = p.height + 1
					q.height = p.height + 1

			else:
				if q.height - x.height == 1:
					while q.height - b.height == 2:
						if q.left and q.right and q.height - q.left.height ==1 or q.height - b.height == 1:
							break
						q.height = b.height + 1
						if q == self.root:
							break
						b = q
						q = q.parent
					if q.left and q.right and q.height - q.left.height == 1 or q.height - b.height == 1:
						pass
					else:
						q.height = b.height + 1


		else:
			c = m = a
			while m.right:
				m = m.right
			m.right = b
			if b:
				b.parent = m
			while m.parent.height - m.height == 1:
				if not b:
					break
				m.height = b.height + 1
				b = m
				m = m.parent
				if m == self.root:
					break
			if b:
				m.height = b.height + 1
			if pt and pt.height - x.height == 1:
				pt.height = c.height + 1

		if self.root == x:
			if c:
				c.parent = None
			self.root = c
		else:
			if pt.left == x:
				pt.left = c
			else:
				pt.right = c
			if c:
				c.parent = pt
		self.size -= 1
	# 노드들의 height 정보 update 필요

	def deleteByCopying(self, x):
		if x == None:
			return None
		pt, L, R = x.parent, x.left, x.right
		if L: # L이 있음`
			y = x.left
			while y.right:
				y = y.right
			x.key = y.key
			if y.left:
				y.left.parent = y.parent
				q = y.parent
				p = y.left
				y.height = 0
				while q.height - p.height == 2:
					if q.left and q.right and q.height - q.left.height == 1 or q.height - q.right.height == 1:
						break
					if q == self.root:
						q.height = p.height + 1
						break
					q.height = p.height + 1
					p = q
					q = q.parent
			else:
				q = y.parent
				p = y
				if q.height - p.height == 1:
					q.height = 0
					while q.parent.height - q.height == 2:
						p = q
						q = q.parent
						if q.left and q.right and q.height - q.left.height == 1 or q.height -q.right.height == 1:
							break
						if q == self.root:
							q.height = p.height + 1
							break
						q.height = p.height + 1
			if y.parent.left is y:
				y.parent.left = y.left
			else:
				y.parent.right= y.left
			del y

		elif not L and R: # R만 있음
			y = R
			while y.left:
				y = y.left
			x.key = y.key
			q = y.parent
			p = y.right
			if y.right:
				y.right.parent = y.parent
			if y.parent.left is y:
				y.parent.left = y.right
				if p:
					while q.height - p.height == 2:
						if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
							break
						if q == self.root:
							break
						q.height = p.height + 1
						p = q
						q = q.parent
					q.height = p.height + 1
				else:
					q.height = 0
					p = q
					q = q.parent
					while q.height - p.height == 2:
						if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
							break
						if q == self.root:
							q.height = p.height + 1
							break
						q.height = p.height + 1
						p = q
						q = q.parent
			else:
				y.parent.right = y.right
				if p:
					while q.height - p.height == 2:
						if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
							break
						if q== self.root:
							break
						q.height = p.height + 1
						p = q
						q = q.parent
					q.height = p.height + 1
				else:
					q.height = 0
					p = q
					q = q.parent
					while q.height - p.height == 2:
						if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
							break
						if q == self.root:
							q.height = p.height + 1
							break
						q.height = p.height + 1
						p = q
						q = q.parent
			del y

		else: # L도 R도 없음
			p = x
			if pt == None: # x가 루트노드인 경우
				self.root = None
			else:
				if pt.left is x:
					pt.left = None
				else:
					pt.right = None
			del x
			q = pt
			if q.height - p.height == 1:
				q.height = 0
				while q.parent.height - q.height == 2:
					p = q
					q = q.parent
					if q.left and q.right and q.height - q.left.height == 1 or q.height - q.right.height == 1:
						break
					if q == self.root:
						break
					q.height = p.height + 1
				q.height = p.height + 1
	# 노드들의 height 정보 update 필요

	def height(self, x):  # 노드 x의 height 값을 리턴
		if x == None:
			return -1
		else:
			return x.height

	def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
		if x == None:
			return None
		p = x.parent
		if x.right:
			y = x.right
			while y.left:
				y = y.left
			return y
		else:
			if p.left == x:
				return p
			else:
				y = p
				z = x
				while y.right == z:
					if not y.parent or y.parent.right != y:
						break
					z = y
					y = y.parent
				if not y.parent:
					return None
				else:
					return y.parent
	# x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴

	def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
		if x == None:
			return None
		p = x.parent
		if x.left:
			y = x.left
			while y.right:
				y = y.right
			return y
		else:
			if p.right == x:
				return p
			else:
				y = p
				z = x
				while y.left == z:
					if not y.parent or y.parent.left != y:
						break
					z = y
					y = y.parent
				if not y.parent:
					return None
				else:
					return y.parent
		pass
	# x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴

	def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		if x == None:
			return
		z = x.right
		if z == None:
			return
		b = z.left
		z.parent = x.parent
		if x.parent:
			if x.parent.left == x:
				x.parent.left = z
			else:
				x.parent.right = z
		z.left = x
		x.parent = z
		x.right = b
		if b:
			b.parent = x
		if self.root == x:
			self.root = z
		if b:
			q = x
			p = b
			while q.height - p.height != 1:
				if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
					break
				if q == self.root:
					q.height = p.height + 1
					break
				q.height = p.height + 1
				p = q
				q = q.parent
		if z.right:
			q = z
			p = z.right
			while q.height - p.height != 1:
				if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
					break
				if q == self.root:
					q.height = p.height + 1
					break
				q.height = p.height + 1
				p = q
				q = q.parent
		if x.left:
			q = x
			p = x.left
			if q.height - p.height == 1:
				p = q
				q = q.parent
			while q.height - p.height != 1:
				if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
					break
				if q == self.root:
					q.height = p.height + 1
					break
				q.height = p.height + 1
				p = q
				q = q.parent
		if not x.left and not x.right:
			x.height = 0
			q = z
			p = x
			while q.height - p.height != 1:
				if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
					break
				if q == self.root:
					break
				q.height = p.height + 1
				p = q
				q = q.parent


	def rotateRight(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
		if x == None:
			return
		z = x.left
		if z == None:
			return
		b = z.right
		z.parent = x.parent
		if x.parent:
			if x.parent.left == x:
				x.parent.left = z
			else:
				x.parent.right = z
		z.right = x
		x.parent = z
		x.left = b
		if b:
			b.parent = x
		if self.root == x:
			self.root = z
		if b:
			q = x
			p = b
			while q.height - p.height != 1:
				if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
					break
				if q == self.root:
					q.height = p.height + 1
					break
				q.height = p.height + 1
				p = q
				q = q.parent
		if z.left:
			q = z
			p = z.left
			while q.height - p.height != 1:
				if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
					break
				if q == self.root:
					q.height = p.height + 1
					break
				q.height = p.height + 1
				p = q
				q = q.parent
		if x.right:
			q = x
			p = x.right
			if q.height - p.height == 1:
				p = q
				q = q.parent
			while q.height - p.height != 1:
				if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
					break
				if q == self.root:
					q.height = p.height + 1
					break
				q.height = p.height + 1
				p = q
				q = q.parent
		if not x.left and not x.right:
			x.height = 0
			q = z
			p = x
			while q.height - p.height != 1:
				if q.left and q.height - q.left.height == 1 or q.right and q.height - q.right.height == 1:
					break
				if q == self.root:
					break
				q.height = p.height + 1
				p = q
				q = q.parent


T = BST()
# while True:
# 	cmd = input().split()


def runCommand(str):
	cmd = str.split(' ')
	if cmd[0] == 'insert':
		v = T.insert(int(cmd[1]))
		print("+ {0} is inserted".format(v.key))
	elif cmd[0] == 'deleteC':
		v = T.search(int(cmd[1]))
		T.deleteByCopying(v)
		print("- {0} is deleted by copying".format(int(cmd[1])))
	elif cmd[0] == 'deleteM':
		v = T.search(int(cmd[1]))
		T.deleteByMerging(v)
		print("- {0} is deleted by merging".format(int(cmd[1])))
	elif cmd[0] == 'search':
		v = T.search(int(cmd[1]))
		if v == None:
			print("* {0} is not found!".format(cmd[1]))
		else:
			print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'height':
		h = T.height(T.search(int(cmd[1])))
		if h == -1:
			print("= {0} is not found!".format(cmd[1]))
		else:
			print("= {0} has height of {1}".format(cmd[1], h))
	elif cmd[0] == 'succ':
		v = T.succ(T.search(int(cmd[1])))
		if v == None:
			print("> {0} is not found or has no successor".format(cmd[1]))
		else:
			print("> {0}'s successor is {1}".format(cmd[1], v.key))
	elif cmd[0] == 'pred':
		v = T.pred(T.search(int(cmd[1])))
		if v == None:
			print("< {0} is not found or has no predecssor".format(cmd[1]))
		else:
			print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
	elif cmd[0] == 'Rleft':
		v = T.search(int(cmd[1]))
		if v == None:
			print("@ {0} is not found!".format(cmd[1]))
		else:
			T.rotateLeft(v)
			print("@ Rotated left at node {0}".format(cmd[1]))
	elif cmd[0] == 'Rright':
		v = T.search(int(cmd[1]))
		if v == None:
			print("@ {0} is not found!".format(cmd[1]))
		else:
			T.rotateRight(v)
			print("@ Rotated right at node {0}".format(cmd[1]))
	elif cmd[0] == 'preorder':
		T.preorder(T.root)
		print()
	elif cmd[0] == 'postorder':
		T.postorder(T.root)
		print()
	elif cmd[0] == 'inorder':
		T.inorder(T.root)
		print()
	# elif cmd[0] == 'exit':
	# 	break
	else:
		print("* not allowed command. enter a proper command!")


# runCommand("insert 10")
# runCommand("insert 5")
# runCommand("insert 20")
# runCommand("insert 7")
# runCommand("insert 6")
# runCommand("insert 15")
# runCommand("insert 13")
# runCommand("insert 17")
# runCommand("insert 16")
# runCommand("insert 22")
# runCommand("preorder")
# runCommand("inorder")
# runCommand("Rleft 15")
# runCommand("preorder")
# runCommand("Rright 15")
# runCommand("preorder")


# runCommand("insert 10")
# runCommand("insert 20")
# runCommand("insert 30")
# runCommand("insert 40")
# runCommand("insert 50")
# runCommand("insert 52")
# runCommand("insert 54")
# runCommand("insert 55")
# runCommand("insert 60")
# runCommand("preorder")
# runCommand("deleteM 10")

runCommand("insert 10")
runCommand("deleteM 10")
