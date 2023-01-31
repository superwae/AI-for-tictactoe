from asyncio.windows_events import INFINITE
import imp
from json.encoder import INFINITY
from msilib.schema import IniFile
import random
from operator import truediv


board =["-","-","-",
        "-","-","-",
        "-","-","-",]
currplayer="X"
winner=None
gamerunning=True


def print_board(board):
    print(board[0]+ " | "+board[1]+ " | "+board[2])
    print("---------")
    print(board[3]+ " | "+board[4]+ " | "+board[5])
    print("---------")
    print(board[6]+ " | "+board[7]+ " | "+board[8])



def player_input(board):
    Pmove=int(input("Enter a number 1-9:"))
    if Pmove>9 or Pmove<1:
	     player_input(board)
    elif Pmove >=1 and Pmove<=9 and board[Pmove-1]=="-":
        board[Pmove-1]=currplayer
    elif board[Pmove-1]!="-":
	     player_input(board)
        

def checkHorizontake(board):
    global winner
    if board[0]==board[1]==board[2]and board[1]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5]and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8]and board[6]!="-":
        winner=board[6]
        return True
    else :
        return False

        
def check_rows(board):
    global winner
    if board[0]==board[3]==board[6]and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7]and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8]and board[2]!="-":
        winner=board[2]
        return True
    else :
        return False


def check_diag(board):
    global winner
    if board[0]==board[4]==board[8]and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6]and board[2]!="-":
        winner=board[2]
        return True
    else :
        return False


def checkTie(board):
    global gamerunning,winner
    if "-" not in board:
        winner='tie'
        return True


def switch_player():
    global currplayer
    if(currplayer=="X"):
        currplayer="O"
    else:
        currplayer="X"


def check_win():
    global winner
    winner=None
    global gamerunning
    if check_diag(board) or check_rows(board) or checkHorizontake(board): 
        return winner
    elif checkTie(board):
           return"tie"
    else:
        return winner


scores={'X':-1,'O':1,'tie':0}

def minimax(board,depth,isPc):
    resultt=check_win()
    if resultt!=None:
      return scores[resultt]
    if isPc:
        bestscore=-INFINITY
        for x in range(0,9):
            if board[x]=="-":
               board[x]="O" 
               score=minimax(board,depth+1,False)
               board[x]="-" 
               bestscore=max(bestscore,score)
        return bestscore
    else:
        bestscore=INFINITY
        for x in range(0,9):
            if board[x]=="-":
               board[x]="X" 
               score=minimax(board,depth+1,True)
               board[x]="-" 
               bestscore=min(bestscore,score)
        return bestscore
    


def computer(board):
    bestscore=-INFINITE
    bestmove=0
    while currplayer=="O":
        for x in range(0,9):
            if board[x]=="-":
             board[x]="O"
             score = minimax(board,0,False)  
             board[x]="-"
             if score>bestscore:
                bestscore=score
                bestmove=x
        board[bestmove]="O"
        switch_player()


        
                
def games():
  global gamerunning,winner,board
  while gamerunning:
    print_board(board)
    player_input(board)
    if check_win()!=None:
        gamerunning=False
        print_board(board)
        print("winner is :"+winner)
        break
    switch_player()
    computer(board)
    if check_win()!=None:
        gamerunning=False
        print_board(board)
        print("winner is :"+winner)
        break
  print("press 1 to play again (press any other key to exit)")
  x=int(input())
  if x==1:
    board =["-","-","-",
        "-","-","-",
        "-","-","-",]
    winner=None
    currplayer="X"
    gamerunning=True
    games()


games()
