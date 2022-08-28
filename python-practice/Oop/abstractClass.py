#abstract class
from abc import ABC,abstractmethod

class test(ABC):
	@abstractmethod
	def __init__(self):
		self.name="abstract class"
	@abstractmethod
	def firstMethod(self):
		pass
		
	def secondMethod(self):
		pass
		
class demo(test):
	print("without calling class but this line executed")
	def __init__(self):
		super().__init__()
		print("class name:",self.name)
	def firstMethod(self):
		print("this is required method")
		
		
classdemo=demo()
classdemo.firstMethod()
classdemo.secondMethod()
