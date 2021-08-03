


#problem0
'''a=[1,2,3,4,5]
b=(123,456,)
c=(7,8,21)
d=(23,345)
e=(222,4000,33)
a.append(e)
a.append(d)
a.append(c)
a.append(b)
a.append(777)
a.append(9999)
print(a)'''

#problem1

'''a=(444,333,222,)
print(a.index(333))
print(a.index(222))
print(a.index(444))'''

#problem2
'''
a=[111]
b=[777]
c='привет'
d='Jimmy'
e='как дела?'

a.append(e)
a.append(d)
a.append(c)
a.append(b)
print(a)
'''
#problem3

'''d = ['Jack','Jimmy','Jackson','Jhon','Jackson']
b = ' '
c = b.join(d)
print(c)'''

#problem4

'''a=['привет']
b=['333']
c= a+b
print(c)'''

#problem5

'''a=['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy','Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
b=a.count('Jhon')
print(b)'''

#problem6
'''a = ['Jack', 'Jimmy','Oskar', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 
'Jimmy', 'Jack', 'Jackson', 'Jhon']
b=a.remove('Oskar')
print(a)'''

#problem7


'''a=[]
b=('Ulan')
c=(2005)
m=('python')
a.append(m)
a.append(c)
a.append(b)
print(a)'''

#problem8

  '''a= ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", 'True', 'False']
'''

#problem10
a='wwwww 333 ttttd'
b=[]
c=[]
for i in a:
	if i.isnamberic():
			b.append(int(i))
	else:
			c.append(i)
			print(b, '\n', c)
