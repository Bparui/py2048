from getpass import getpass
import random, os, argparse, numpy as np

'''command line input of game size and winning value'''
parser = argparse.ArgumentParser()
parser.add_argument('--w', type=int, default=5,
                        help='What is the board size?')
parser.add_argument('--n', type=int, default=2048, 
                        help='What is the winning value?')
args=parser.parse_args()
width,limit,ck = args.w,args.n,args.n

if width<=0:
	print("Invalid game size. Game size set to default i.e 5")
	wid=5
else:
	wid=width

'''checks if winning value is correct or not'''
def limitcheck(n): 
    if n <= 0: 
        return "wrong",1
    elif n==1:
    	return False,2
    while n >= 2:
            if (n % 2 != 0): 
                return "wrong",2
            n = n // 2
    return "ryt",0

k,c=limitcheck(ck)
if k=="wrong":
	if c==1:
		print('Invalid winning value. Value set to default i.e 2048.')
		limit=2048
	else:
		print('Value is not a power of 2. Winning value set to the nearest power of 2 greater than entered value')
		v=1
		n=1
		while n<limit:
			n=2**v
			v=v+1
		limit=n

'''defines gameboard'''
game=np.zeros([wid,wid], dtype=int)

def format(curr_game):
    for a in curr_game:
        for elem in a:
            print("{}".format(elem).rjust(3), end="")
        print(end="\n")

'''spawns random two'''
def random_twos(curr_game):
	a = random.randint(0, len(game)-1)
	b = random.randint(0, len(game)-1)
	while(game[a][b] != 0):
		a = random.randint(0, len(game)-1)
		b= random.randint(0, len(game)-1)
	game[a][b] = 2
	return curr_game

'''ccode to define actions of wasd'''
def merge(curr_game):
	lnt=len(curr_game)
	for j in range(lnt):
		for i in range(lnt-1):
				if curr_game[j][i]==curr_game[j][i+1]:
					curr_game[j][i] *= 2
					curr_game[j][i+1]=0
	count=0
	while count<=lnt:
		for j in range(lnt):
			for i in range(lnt-1):
				if curr_game[j][i]==0:
					curr_game[j][i] = curr_game[j][i+1]
					curr_game[j][i+1]=0
		count=count+1
	return curr_game


def reverse(curr_game):
	l=k=len(curr_game)
	for j in range(l):
		if l%2!=0:
			k=l-1
		for i in range(int(k/2)):
			temp=curr_game[j][i]
			curr_game[j][i]=curr_game[j][l-i-1]
			curr_game[j][l-i-1]=temp
	return curr_game


def transpose(curr_game):
	l=len(curr_game)
	for j in range(l):
		for i in range(l):
			if i<j:
				temp=curr_game[j][i]
				curr_game[j][i]=curr_game[i][j]
				curr_game[i][j]=temp	
	return curr_game

'''checks winning situation'''
def win(curr_game):
	for i in range(len(curr_game)):
		for j in range(len(curr_game)):
			if curr_game[i][j]==limit:
				return "YOU WON"
	for i in range(len(curr_game)-1):
		for j in range(len(curr_game)-1):
			if curr_game[i][j]==curr_game[i][j+1] or curr_game[i][j]==curr_game[i+1][j]:
				return "ntover"
	for i in range(len(curr_game)-1):
		j=len(curr_game)-1
		if curr_game[i][j]==curr_game[i+1][j] or curr_game[j][i]==curr_game[j][i+1]:
			return "ntover"
	for i in range(len(curr_game)):
		for j in range(len(curr_game)):
			if curr_game[j][i]==0:
				return "ntover"
	return "YOU LOST"

'''playing of game'''
game=random_twos(game)
print(format(game))
r=win(game)
if r=="YOU WON":
	print(r)
else:
	while True:
		k=True
		while k:
			t=np.copy(game)
			move=getpass("enter w,a,s or d for movement ")
			os.system("cls")
			if move=='w':
				game=transpose(merge(transpose(game)))
				k=False
			elif move=='a':
				game=merge(game)
				k=False
			elif move=='d':
				game=reverse(merge(reverse(game)))
				k=False
			elif move=='s':
				game=transpose(reverse(merge(reverse(transpose(game)))))
				k=False
			else:
				print('Invalid key pressed')
				k=True
		if not (t==game).all():
			game=random_twos(game)
		print(format(game))
		result=win(game)
		if not result=="ntover":
			print(result)
			break
