a='wwwww 333 ttttd'
b=[]
c=[]
for i in a:
	if i.isnumeric():
			b.append(int(i))
	else:
			c.append(i)
			print(b, '\n', c)
