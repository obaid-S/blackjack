from random import randint
from time import sleep
class Player:
  bust=False
  stood=False
  finalVal=0
  
  def __init__(self,hand,players):
    self.hand=hand
    self.name=f'Player {len(players)+1}'

  def hit(self,curCards):
    temp=randint(0,(len(curCards)-1))
    self.hand.append(curCards[temp])#random card and inserted into hand
    temp1=curCards[temp]
    del curCards[temp]   
    if(self.hand_value()>21):
      input(f'{self.name} pulled a {temp1} and Busted! (Enter to continue)')
      self.bust=True
    else:
      input(f'{self.name} pulled a {temp1}! (Enter to continue)')

      
  def deal(self,curCards):
    temp=randint(0,(len(curCards)-1))
    self.hand.append(curCards[temp])#random card and inserted into hand
    del curCards[temp] 

  def hand_value(self):
    value=0
    ace=0
    for card in self.hand:
      try:
        value=value+int(card[1:])
      except:
        if(card[1:]=='J'):
          value=value+10
        elif(card[1:]=='Q'):
          value=value+10
        elif(card[1:]=='K'):
          value=value+10
        elif(card[1:]=='A'):
          ace=ace+1
        else:
          print(f'Error {card[1:]}')
    for num in range(ace):
      if((value+11)<22):
        value=value+11
      else:
        value=value+1
    return value
      
  def fold(self):
    pass

  def split(self):
    pass

  def stand(self):
    self.stood=True
    self.finalVal=self.hand_value()

  def dealers_turn(self,curCards):
    print('DEALERS TURN')
    sleep(0.5)
    print(f'Dealers Hand: {self.hand}')
    sleep(0.5)
    while(self.hand_value()<17):
      temp=randint(0,(len(curCards)-1))
      self.hand.append(curCards[temp])#random card and inserted into hand
      temp1=curCards[temp]
      del curCards[temp]   
      if(self.hand_value()>21):
        print(f'{self.name} pulled a {temp1} and Busted!')
        self.ongoing=False
        self.bust=True
      else:
        print(f'{self.name} pulled a {temp1}!')
      sleep(1)
    print(f'Dealers Hand: {self.hand} (Hand Value:{self.hand_value()})')
    return False
