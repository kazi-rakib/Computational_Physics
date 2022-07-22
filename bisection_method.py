#import time		# used for debugging purpose (TDD approach)


class Solve:

	# Initialization
	def __init__(self, a, b, c, d, precision=1e-15):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		# default value = 1e-15
		self.precision = precision

		# keeps track of the steps
		self.count = 0

		# shows the equation
		print(self.__str__())
	
	
	# This function solve an equation
	# 		for a specific value 
	def solveFor(self, x):
		# This is an optional task that
		# counts how many times the function was called.	
		self.count = self.count + 1
		
		# This formula can calculate upto cubic power terms
		# which can further be extended for higher powers if necessary
		eqn = (self.a*x*x*x + self.b*x*x + self.c*x + self.d)
		#print(eqn) 	# used for debugging purpose

		return eqn
	
	# ============= Bisection Method =============
	# The actual algorithm for "Bisection Method"
	#  has been implemented in this function
	def solve(self):
		
		# Let's start with the range [L, R]
		# 	where L = -(co-efficient of the highest power term)*(constant term)
		# 	 and  R = (co-efficient of the highest power term)*(constant term)
		#			since the root must lie in between them
		L, R= -abs(self.a*self.d), abs(self.a*self.d)

		# The bisection of the range is given by
		X = (L+R)/2

		# print(L, R) 	# used for debugging purpose

		# Let's set the precision for 
		# solving the equation
		# 1e-15 is the lowest possible accuracy
		#		that can be achieved for my machine(64bit)
		epsilon =  self.precision

		while abs(R-L) > epsilon :
			
			# time.sleep(0.01) 	# used for debugging purpose
			
			if self.solveFor(X) > 0.0 :
				# look for root in the first half
				R = X
			else:
				# look for root in the last half
				L = X
			
			print(self.count, end="\r")		# shows steps required to solve the equation in real time
			
			# at each step the range [L, R]
			#		will be reduced by half
			X = (L+R)/2
			
		# This shows total number of steps needed
		print(str(self.count) ," operations performed to solve.")
		
		return X
	
	def __str__(self):
		
		# show the eqn
		eqn = 'f(x) = (' + str(self.a) + ')x^3 + (' + str(self.b) + ')x^2 + (' + str(self.c) + ')x + (' + str(self.d) + ')\n'
		
		return eqn
		
	def __repr__(self):
		eqn = 'f(x) = (' + str(self.a) + ')x^3 + (' + str(self.b) + ')x^2 + (' + str(self.c) + ')x + (' + str(self.d) + ')\n'
		
		return eqn
	
	
				
if __name__ == "__main__":
	
	# Test for a known equation
	s = Solve(1, 0, -2, -5)
	print('\nx = ', s.solve())
	
	
	# user input
	print("\n\nPlease input the co-efficients the desired equation:\n")
	a = float(input("\ta="))
	b = float(input("\tb="))
	c = float(input("\tc="))
	d = float(input("\td="))

	s2 = Solve(a, b, c, d)

	print("x = ", s2.solve())
