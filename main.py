from blackjack import BLACKJACK_BET
from blackjack import BLACKJACK
from replit import clear
deck=['H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK','HA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK','CA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK','DA']#make deck a 6x for black jack meaning 312 cards in one deck
curCards=deck
curGame=None
def create_dict_from_string(str):
 import json
 dictionary = json.loads(str)
 return dictionary
  
def create_string_from_dict(dict):
 import json
 string = json.dumps(dict)
 return string
  
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
          return BLACKJACK(int(input('Enter NUMBER of Humans Playing: ')),curCards,1)
        except:
          pass
    elif(game==2):
      from os.path import getsize
      import json
      player={}
      def addNew(name,player):
       file=open('save.txt','w')
       player[name]=500
       file.write(json.dumps(player))
       file.flush()
       file.close()
      file=open('save.txt','r')
      name=input('Enter your name: ')
      if getsize('save.txt')>0:
       file=open('save.txt','r')
       player=json.loads(file.read())
      if name not in player:
       file.close()
       addNew(name,player)  
      return BLACKJACK_BET(1,curCards,0,player[name],name)
    else:
      
      game=input('Enter a NUMBER correspodning to game\n[1] Black Jack(Multi-Users)\n[2] Black Jack(Single Betting User)\n')
      
print('Enter a NUMBER correspodning to game\n[1] Black Jack(Multi-Users)\n[2] Black Jack(Single Betting User)')
curGame=startUp(input(''))
clear()
curGame.start()