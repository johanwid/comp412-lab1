"""
file for testing code for lab1
"""

class Scanner:
	def __init__(self, source_code):
		self.source = source_code.read() 
	def __repr__(self):
		pass
	def nextChar(self, i):
		return self.source[i]
	
		
class Token:
	def __init__(self):
		pass
