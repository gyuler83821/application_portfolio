"""Assignment 3-3 Candy Crush"""
with open("candy_input.txt") as currentfile:
	table,booltable,newtable=[],[],[]
	def check(height,width):
		current_x,current_y,process=0,0,False
		#horizontal direction(find the same candy)
		for current_y in range(height):
			for current_x in range(width-2):
				if(table[current_y][current_x]==table[current_y][current_x+1] 
					and table[current_y][current_x+1]==table[current_y][current_x+2] 
					and table[current_y][current_x]!=0 ):
					process=True
					booltable[current_y][current_x]=True
					booltable[current_y][current_x+1]=True
					booltable[current_y][current_x+2]=True
		#vertical direction
		current_x,current_y=0,0
		for current_x in range(width):
			for current_y in range(height-2):
				if(table[current_y][current_x]==table[current_y+1][current_x] 
					and table[current_y+1][current_x]==table[current_y+2][current_x]
					and table[current_y][current_x]!=0):
					process=True
					booltable[current_y][current_x]=True
					booltable[current_y+1][current_x]=True
					booltable[current_y+2][current_x]=True
		return process  #process(boolean) stands for whether there are same candies
	def move(height,width):
		#allow blanks to be filled
		x,y=0,0
		for x in range(width):
			collect=[]  #collect non-zero number
			for y in range(height-1,-1,-1):
				if booltable[y][x]==False:
					collect+=[table[y][x]]
			num=0
			for y in range(height-1,-1,-1):
				if num<len(collect):
					table[y][x]=collect[num]
					booltable[y][x]=False
					num+=1
				else:
					table[y][x]=0
					booltable[y][x]='No' #upper positions set 'No'
			
	#defalut the table 
	table=currentfile.read().split('\n')
	table.remove('')
	temp=0
	for temp in range(len(table)):
		newtable+=[table[temp].split(',')]
	table=newtable[:]
	#the size of the input data
	width=len(table[0])
	height=len(table)
	a=0
	#set the boolean table to check that which is deleted laterly
	for a in range(height):
			booltable+=[[False]*width]
	count=0
	#if there are still same cndies, do while loop continuously
	while check(height,width):
		move(height,width)

	#there is no same candy, so we output the answer
	with open("candy_ouput.txt",'w') as writefile:
		x,t=0,0
		for y in range(0,height):
			temp=''
			for x in range(0,width):
				temp+=str(table[y][x])
				if x !=width-1:
					temp+=','
			writefile.write(temp+'\n')