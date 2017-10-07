
class BankAccount(object):
	def __init__(self):
		pass

	def open(self):
		self.balance = 0
		return self.balance

	def deposit(self, amount):
		self.lock.acquire()
		if (self.open == True and amount>0):
			self.balance += amount
			self.lock.release()
		else:
			self.lock.release()
			raise Exception


	def withdraw(self, amount):
		self.lock.acquire()
		if (self.open == True and self.balance >= amount and amount>0):
			self.balance -= amount
			self.lock.release()
		else:
			self.lock.release()
			raise Exception

	def close(self):
		self.lock.acquire()
		self.open = False
		self.lock.release()
