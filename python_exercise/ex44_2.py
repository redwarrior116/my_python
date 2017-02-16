class Parent(object):
	
	def __init__(self,var_2):
		self.var_1 = "I'm parents,if you are child, you have one more to say"	
		self.var_2 = var_2
	def talk(self):
		print "it will be override"

class Child(Parent):
	
	def __init__(self,var_3,var_4):
		self.var_3 = var_3
		super(Child,self).__init__(var_4)
		

	def talk(self):
		print "I have override you. dummy."

Greg = Parent("dad")
John = Child("son","ToParents")

print Greg.var_1
print John.var_1
print Greg.var_2
print John.var_3
print John.var_2
