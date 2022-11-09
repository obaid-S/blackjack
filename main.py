from blackjack import BLACKJACK
from replit import clear
from time import sleep
deck=['H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK','HA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK','CA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK','DA']#make deck a 6x for black jack meaning 312 cards in one deck
curCards=deck
curGame=None

  
def startUp(game):
  loop=True
  while(loop):#checks if a correct game number is inputed
    try:
      game=int(game)
    except:
      pass

    if(game==1):
      loop=False
      temp=True
      while temp:
        try: 
          return BLACKJACK(int(input('Enter NUMBER of Humans Playing: ')),curCards)
        except:
          pass

    elif(game==2):
      loop=False 
    else:
      game=input('Enter a NUMBER correspodning to game\n[1] Black Jack\n[2] EMPTY\n')
      


print('Welcome to our table! What would you like to play?\n[1] Black Jack\n[2] EMPTY\nEnter number corresponding to game: ')
curGame=startUp(input(''))
clear()
curGame.start()