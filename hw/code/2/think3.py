##3.1
'''repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()'''

##3.2
'''def repeat_lyrics():
    print_lyrics()
    print_lyrics()
	
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

repeat_lyrics()

##it runs normally'''

##3.3
'''def right_justify(s):
	no=70-len(s)
	print(" "*no),
	print(s)
	
right_justify("abc")'''

#3.4.1
'''def print_twice(x):
	print x
	print x

def print_spam(x):
    print_twice(x)

def do_twice(f,x):
    f(x)
    f(x)
	
do_twice(print_spam,"spam")'''

#3.4.2
'''def print_twice(x):
	print x
	print x

def do_four(f,x):
    f(x)
    f(x)
	
do_four(print_twice,"spam")'''

#3.5.1
'''def print_grid():
	for z in range(0,2):
		plus_minus()
		slash()
	plus_minus()

def plus_minus():
	for i in  range(0,2):
		print ' +',
		for k in range(0,4):
			print ' _',
		k=0
	print ' +'

def slash():
	for x in range(0,4):
		for j in range(0,2):
			print(' /'),
			print(' '*11),
		print(' /')

print_grid()'''

#3.5.2
def print_grid():
	for z in range(0,4):
		plus_minus()
		slash()
	plus_minus()

def plus_minus():
	for i in  range(0,4):
		print ' +',
		for k in range(0,4):
			print ' _',
		k=0
	print ' +'

def slash():
	for x in range(0,4):
		for j in range(0,4):
			print(' /'),
			print(' '*11),
		print(' /')

print_grid()
