
class AdaptedHeap: # min_heap으로 정의함!
	def __init__(self):
		self.A = []
		self.D = {}  # dictionary D[key] = index

	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)

	def insert(self, key):
		self.A.append(key)
		self.D[key] = len(self.A)-1
		self.heapify_up(len(self.A)-1)
		return self.D[key]

	def heapify_up(self, k):
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
		while k > 0 and k<len(self.A):
			m = (k-1)//2
			if self.A[k] < self.A[m]:
				self.A[k], self.A[m] = self.A[m], self.A[k]
				self.D[self.A[k]] = k
				self.D[self.A[m]] = m
				k = m
			else:
				break

	def heapify_down(self, k):
		# code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
		while 2*k+1<len(self.A):
			L, R = 2*k+1, 2*k+2
			if L < len(self.A) and self.A[k] > self.A[L]: m = L
			else: m = k
			if R < len(self.A) and self.A[R] < self.A[m]: m = R
			if k != m:
				self.A[k], self.A[m] = self.A[m], self.A[k]
				self.D[self.A[k]] = k
				self.D[self.A[m]] = m
				k = m
			else:
				break

	def find_min(self):
		if len(self.A) == 0:
			return None
		else:
			return self.A[0]

	def delete_min(self):
		if len(self.A) == 0: 
			return None
		key = self.A[0]
		self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
		self.A.pop()
		del self.D[key]
		self.heapify_down(0)
		return key

	def update_key(self, old_key, new_key):
		# old_key가 힙에 없으면 None 리턴
		if old_key not in self.D:
			return None
		else:
			k = self.D[old_key] 
		# 아니면, new_key 값이 최종 저장된 index 리턴
			if old_key > new_key:
				self.A[k] = new_key
				self.D[new_key] = k
				del self.D[old_key]
				self.heapify_up(k)
			elif old_key < new_key:
				self.A[k] = new_key
				self.D[new_key] = k
				del self.D[old_key]
				self.heapify_down(k)
			return self.D[new_key]

# 아래 명령 처리 부분은 수정하지 말 것!
H = AdaptedHeap()


# while True:
# 	cmd = input().split()
def runCommand(str):
	cmd = str.split(' ')
	if cmd[0] == 'insert':
		key = int(cmd[1])
		loc = H.insert(key)
		print(f"+ {int(cmd[1])} is inserted")
	elif cmd[0] == 'find_min':
		m_key = H.find_min()
		if m_key != None:
			print(f"* {m_key} is the minimum")
		else:
			print(f"* heap is empty")
	elif cmd[0] == 'delete_min':
		m_key = H.delete_min()
		if m_key != None:
			print(f"* {m_key} is the minimum, then deleted")
		else:
			print(f"* heap is empty")
	elif cmd[0] == 'update':
		old_key, new_key = int(cmd[1]), int(cmd[2])
		idx = H.update_key(old_key, new_key)
		if idx == None:
			print(f"* {old_key} is not in heap")
		else:
			print(f"~ {old_key} is updated to {new_key}")
		print(H.D)
	elif cmd[0] == 'print':
		print(H)
	# elif cmd[0] == 'exit':
	# 	break
	else:
		print("* not allowed command. enter a proper command!")



runCommand("insert 50")
runCommand("insert 40")
runCommand("insert 30")
runCommand("insert 20")
runCommand("update 40 5")
runCommand("print")
runCommand("update 40 5")
runCommand("print")


