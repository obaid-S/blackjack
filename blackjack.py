from player import Player
from replit import clear
import json
class BLACKJACK:
  playerVals={}
  players=[]
  ongoing=True
  def __init__(self,numPlayers,curCards,mode,curMoney=500):
    self.deck=curCards
    self.numPlayers=numPlayers
    self.mode=mode
    self.money=curMoney
  
    #deals 2 cards to each players + dealer(computer)
    for person in range(self.numPlayers+1):            
      person=Player([],self.players)
      self.players.append(person)
    for i in range(2):
      for plyr in self.players:
        plyr.deal(self.deck)
    self.players[-1].name='Dealer'
    
  def start(self):
    while(self.ongoing):#while game is ongoing see if all players are bust or have stayed, if not countine asking players for their play  
      if self.mode!=1:
        while(True):
          try:
            amount=int(input(f'Current Money [{self.money}]\nHow much would you like to bet?\n'))
          except:
            pass
          break
      else:    
        for player in self.players[:-1]:
          while (player.bust==False and player.stood==False):
            choice=-1
            if(player.hand_value()==21):
              clear()
              print(f'Dealers Hand: [{self.players[-1].hand[0]}, ?]\n{player.name}: {player.hand} (Value:{player.hand_value()})')
              input('NATURAL 21! (Enter to continue)')
              choice=3
            
            while(choice==-1):#checks if bust, stand or invalid input
              try:
                clear()
                print(f'Dealers Hand: [{self.players[-1].hand[0]}, ?]\n{player.name}: {player.hand} (Value:{player.hand_value()})')
  
                
                choice=int(input('What would you like to do (Enter # Corresponding to Action)\n[1] Hit\n[2] Fold(Dont press this)\n[3] Stand\n[4] Split(Dont press this)\n'))    
              except:
                pass
            if(choice==1):
              player.hit(self.deck)
            elif(choice==2):
              pass
            elif(choice==3):
              player.stand()
            elif(choice==4):
              pass
            else:
              pass
            self.playerVals[player.name]=player.hand_value()
        run=False
        for value in self.playerVals.values():
          if(value<22):
            run=True
        clear()
        if (run):
          self.ongoing=self.players[-1].dealers_turn(self.deck)
          winners=[]
          for person in self.players[:-1]:
            if(22>person.hand_value()):
              if(self.players[-1].hand_value()<22):
                if(person.hand_value()>self.players[-1].hand_value()):
                  winners.append(person.name)
              else: 
                winners.append(person.name)
          if(len(winners)>0):
            print('Players: ')
            print(*winners,sep=' ,')
            print('won the game!')
          else:
            print('All players lost!')   
            self.ongoing=False
        else:
          print('All players lost!')
          self.ongoing=False
          
class BLACKJACK_BET:
  amount=0
  playerVals={}
  players=[]
  ongoing=True
  
  def __init__(self,numPlayers,curCards,mode,curMoney=500,name='0'):
    self.name=name
    self.deck=curCards
    self.numPlayers=numPlayers
    self.mode=mode
    self.money=curMoney
  
    #deals 2 cards to each players + dealer(computer)
    for person in range(self.numPlayers+1):            
      person=Player([],self.players)
      self.players.append(person)
    for i in range(2):
      for plyr in self.players:
        plyr.deal(self.deck)
    self.players[-1].name='Dealer'
  def getPlayers(self):
    file=open('save.txt','r')
    player=json.loads(file.read())
    file.close()
    return player
  def addNew(self,name,player,amount,cond):
    file=open('save.txt','w')
    if cond=='+':
      player[name]=player[name]+amount
    else:
      player[name]=player[name]-amount
    file.write(json.dumps(player))
    file.flush()
    file.close()
    
  def start(self):
    while(self.ongoing):#while game is ongoing see if all players are bust or have stayed, if not countine asking players for their play  
      if self.mode!=1:
        while(True):
          try:
            amount=int(input(f'Current Money [{self.money}]\nHow much would you like to bet?\n'))
          except:
            pass
          if amount>0 and amount<=self.money:
            self.mode=1          
          break
      else:   
        for player in self.players[:-1]:
          while (player.bust==False and player.stood==False):
            choice=-1
            if(player.hand_value()==21):
              clear()
              if(amount>0):
                print(f'Dealers Hand: [{self.players[-1].hand[0]}, ?]\nBet amount: {amount}\n{player.name}: {player.hand} (Value:{player.hand_value()})')
                input('NATURAL 21! (Enter to continue)')
                choice=3
              else:
                print(f'Dealers Hand: [{self.players[-1].hand[0]}, ?]\n{player.name}: {player.hand} (Value:{player.hand_value()})')
                input('NATURAL 21! (Enter to continue)')
                choice=3
            
            while(choice==-1):#checks if bust, stand or invalid input
              try:
                clear()
                if amount>0:
                  print(f'Dealers Hand: [{self.players[-1].hand[0]}, ?]\nBet amount: {amount}\n{player.name}: {player.hand} (Value:{player.hand_value()})')
                else:
                  print(f'Dealers Hand: [{self.players[-1].hand[0]}, ?]\n{player.name}: {player.hand} (Value:{player.hand_value()})')
                #user choices  
                choice=int(input('What would you like to do (Enter # Corresponding to Action)\n[1] Hit\n[2] Fold(Dont press this)\n[3] Stand\n[4] Split(Dont press this)\n'))    
              except:
                pass
            if(choice==1):
              player.hit(self.deck)
            elif(choice==2):
              pass
            elif(choice==3):
              player.stand()
            elif(choice==4):
              pass
            else:
              pass
            self.playerVals[player.name]=player.hand_value()
        run=False
        for value in self.playerVals.values():
          if(value<22):
            run=True
        clear()
        if (run or amount>0):
          self.ongoing=self.players[-1].dealers_turn(self.deck)
          winners=[]
          if amount==0:
            for person in self.players:
              if(22>person.hand_value()):
                if(self.players[-1].hand_value()<22):
                  if(person.hand_value()>self.players[-1].hand_value()):
                    winners.append(person.name)
                else: 
                  winners.append(person.name)
            if(len(winners)>0):
              print('Players: ')
              print(*winners,sep=' ,')
              print('won the game!')
            else:
              print('All players lost!')
          else:#checks if player beat dealer on betting rnd
            if(self.players[0].hand_value()==self.players[-1].hand_value()):
              print('You Tied!')
            elif(22>self.players[0].hand_value()):
                if(self.players[-1].hand_value()<22):
                  if(self.players[0].hand_value()>self.players[-1].hand_value()):
                    player=self.getPlayers()
                    self.addNew(self.name,player,amount,'+')
                    print(f'You won!\nCurrent Balance: {player[self.name]}')
                  else:
                    player=self.getPlayers()
                    self.addNew(self.name,player,amount,'-')
                    print(f'You lost!\nCurrent Balance: {player[self.name]}')
                else: 
                  player=self.getPlayers()
                  self.addNew(self.name,player,amount,'+')
                  print(f'You won!\nCurrent Balance: {player[self.name]}')
            else:
              player=self.getPlayers()
              self.addNew(self.name,player,amount,'-')
              print(f'You lost!\nCurrent Balance: {player[self.name]}')
            self.ongoing=False
        else:
          print('All players lost!')   
