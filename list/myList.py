
class myList():
	def __init__(self):
		self.capacity = 2	  # myList의 용량 (저장할 수 있는 원소 개수)
		self.n = 0          # 실제 저장된 값의 개수
		self.A = [None] * self.capacity # 실제 저장 자료구조 (python의 리스트 사용) 

	def __len__(self):
		return self.n
	
	def __str__(self):
		return f'  ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'

	def size(self):
		return self.capacity
	
	def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		return self.A[k]
		if k >= self.n:
			raise IndexError
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
	
	def __setitem__(self, k, x): # k번째 칸에 값 x 저장
		self.A[k] = x
		if k >= self.n:
			raise IndexError
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴

	def change_size(self, new_capacity):
		print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
		B = [None] * new_capacity
		for i in range(self.n):
			B[i] = self.A[i]
		del self.A
		self.A = B
		self.capacity = new_capacity

	
	def append(self, x):
		if self.n == self.capacity: 
			self.change_size(self.capacity*2)
		self.A[self.n] = x
		self.n += 1

	def pop(self, k=None): # A[k]를 제거 후 리턴. k 값이 없다면 가장 오른쪽 값 제거 후 리턴
		if self.n == 0 or k >= self.n or self.n < -k:# 빈 리스트이거나 올바른 인덱스 범위를 벗어나면: 
			raise IndexError
		if self.capacity >= 4 and self.n <= self.capacity//4: 
			self.change_size(self.capacity//2)
		if k == None or k == -1:
			x = self.A[self.n-1]
		else:
			x = self.A[k]
			for i in range(k, self.n-1):
				self.A[i] = self.A[i+1]
		self.n -= 1
		return x
		# 1. k 값이 주어진 경우와 주어지지 않은 경우 구별해야 함
		# 2. x = self.A[k]
		# 3. A[k]의 오른쪽의 값들이 한 칸씩 왼쪽으로 이동해 메꿈
		# 4. self.n -= 1
		# 5. return x

	def insert(self, k, x):
		if k >= self.n or self.n < -k:
			raise IndexError
		if self.n == self.capacity:
			self.change_size(self.capacity*2)
		for i in range(self.n, k, -1):
			self.A[i] = self.A[i-1]
		self.A[k] = x
		self.n += 1
		# 주의: k 값이 음수값일 수도 있음
		# k 값이 올바른 인덱스 범위를 벗어나면, raise IndexError
		# 1. k의 범위가 올바르지 않으면 IndexError 발생시킴
		# 2. self.n == self.capacity이면 self.change_size(self.capacity*2) 호출해 doubling
		# 3. self.A[k] = x
		# 5. self.n += 1
		
L = myList()
while True:
    cmd = input().strip().split()
    if cmd[0] == 'append':
        L.append(int(cmd[1]))
        print(f"  + {cmd[1]} is appended.")
    elif cmd[0] == 'pop':
        if len(cmd) == 1:
            idx = -1
        else:
            idx = int(cmd[1])
        try:
            x = L.pop(idx)
            print(f"  - {x} at {idx} is popped.")
        except IndexError:
            if len(L) == 0:
                print("  ! list is empty.")
            else:
                print(f"  ! {idx} is an invalid index.")
    elif cmd[0] == 'insert':
        try:
            L.insert(int(cmd[1]), int(cmd[2]))
            print(f"  + {cmd[2]} is inserted at index {cmd[1]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'get': # getitem A[k]
        try:
            L[int(cmd[1])]
            print(f"  @ L[{cmd[1]}] --> {L[int(cmd[1])]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'set': # setitem A[k] = x
        try:
            L[(int(cmd[1]))] = int(cmd[2])
            print(f"  ^ L[{cmd[1]}] <-- {cmd[2]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'size':
        print("  ? capacity =", L.size())
    elif cmd[0] == 'print':
        print(L)
    elif cmd[0] == 'exit':
        print('bye~')
        break
    else:
        print(" ? invalid command! Try again.")	
