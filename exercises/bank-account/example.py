import threading


class BankAccount(object):
    def __init__(self):
        self.lock = threading.Lock()

    def getBalance(self):
        self.lock.acquire()
        if (self.open is True):
            self.lock.release()
            return self.balance
        else:
            self.lock.release()
            raise Exception

    def open(self):
        self.lock.acquire()
        self.balance = 0
        self.open = True
        self.lock.release()

    def deposit(self, amount):
        self.lock.acquire()
        if (self.open is True and amount > 0):
            self.balance += amount
            self.lock.release()
        else:
            self.lock.release()
            raise Exception

    def withdraw(self, amount):
        self.lock.acquire()
        if (self.open is True and self.balance >= amount and amount > 0):
            self.balance -= amount
            self.lock.release()
        else:
            self.lock.release()
            raise Exception

    def close(self):
        self.lock.acquire()
        self.open = False
        self.lock.release()
