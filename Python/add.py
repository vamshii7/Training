print('\nSimple Calculator\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n')

def add():
	s=num1+num2
	print(num1,'+',num2,'=',s,sep='')
def sub():
	s=num1-num2
	print(num1,'-',num2,'=',s,sep='')
def mul():
	s=num1*num2
	print(num1,'*',num2,'=',s,sep='')
def div():
	s=float(num1)/float(num2)
	print(num1,'/',num2,'=',s,sep='')

while True:

	try:
		choice=int(input('Enter your choice (1,2,3,4): '))
	
		if choice in (1,2,3,4):
			num1 = int(input("Enter first number: "))
			num2 = int(input("Enter second number: "))
	
			if choice == 1:
				add()
			elif choice == 2:
				sub()
			elif choice == 3:
				mul()
			elif choice == 4:
				div()
			else:
				print('Invalid Input, please select from above choices')
	except ValueError:
		print('Invalid input. Please enter a number.')
	next_calc = input("Let's do next calculation? (yes/no): ")
	if next_calc == 'no':
		break
