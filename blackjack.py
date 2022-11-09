from player import Player
from replit import clear
class BLACKJACK:
  playerVals={}
  players=[]
  ongoing=True
  def __init__(self,numPlayers,curCards):
    self.deck=curCards
    self.numPlayers=numPlayers
  
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
        for person in self.players:
          if(22>person.hand_value() and person.hand_value()>self.players[-1].hand_value()):
            winners.append(person.name)
        if(len(winners)>0):
          print('Players: ')
          print(*winners,sep=' ,')
          print('won the game!')
        else:
          print('No human winners!')            
      else:
        print('All players lost!')
        self.ongoing=False
        
          
           #here put stuff here to aks the players what they want to do type beat
        
     
      
    