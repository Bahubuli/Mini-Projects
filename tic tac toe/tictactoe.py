'''tic tac toe for two players by bahubuli'''
def wincheck(board):
	if(board['1']==board['2'] and board['2']==board['3']):
		print('player with turn '+turn+ ' won the match')
		return 1
	if(board['1']==board['5'] and board['5']==board['9']):
		print('player with turn '+turn+ ' won the match')
		return 1
		
	if(board['1']==board['4'] and board['4']==board['7']):
		print('player with turn '+turn +' won the match')
		return 1
	if(board['3']==board['5'] and board['5']==board['7']):
		print('player with turn '+turn+ ' won the match')
		return 1
	else:
		print('either match is tied or still running')
		
def isfull(board):
	if '  ' not in board.values():
		return True
	else:
		return False		



bord={'1':' 1 ','2':' 2 ','3':' 3 ','4':' 4 ','5':' 5 ','6':' 6 ','7':' 7 ','8':' 8 ','9':' 9 '}

def pb(board):
	print(board['1']+'|'+board['2']+'|'+board['3'])
	print('--+--+--')
	print(board['4']+'|'+board['5']+'|'+board['6'])
	print('--+--+--')
	print(board['7']+'|'+board['8']+'|'+board['9'])
	
turn='X'

while True:
	print('turn for  '+turn)
	move=input()
	if(int(move)>9):
		print('please enter appropriate place ')
		continue
	if(bord[move]!='X' and bord[move]!='O'):
		bord[move]=turn
	
	
	else:
		print('wrong place')
	pb(bord)
	wincheck(bord)
	if turn=='X':
		turn='O'
	else:
		turn='X'
	
	


		
		
	
	
	
	
	
	
	
	
	




