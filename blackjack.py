# BlackJack
import random

class Deck():

  color = ['clubs','diamonds','hearts','spades']
  value = [2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']

  '''52 cards for BlackJack deck'''

  def __init__(self):
    cards = []
    for c in Deck.color:
      for v in Deck.value:
        cards.append(str(v) + ' of ' + c)
    self.cards = cards

class Player:

  '''player attributes -- name, money, hand'''

  def __init__(self,name = '',money = 0):
    self.name = name
    self.money = money

  def amount(self,bet,win):
    if win:
      self.money = self.money + bet
    elif win == False:
      self.money = self.money - bet
    return self.money

  def hand(self,hand,cards):
    while True:
      card = random.choice(cards)
      cards.remove(card)
      hand.append(card)
      if len(hand) < 2:
        pass
      else:
        break
    return hand

def check_value(hand):
  value = 0
  for item in hand:
    try:
      if int(item[0]) == 1:
        value += 10
      else:
        value += int(item[0])
    except:
      if item[0] == 'a':
        value += 11
        if 21 < value <= 31:
          value = value -10
      else:
        value += 10
  return value

def player_win(*args):
  if args[0] > 21 or (abs(args[0]-21) > abs(args[1]-21) and args[1]<= 21):
    return 'lose'
  elif args[1] > 21 or abs(args[0]-21) < abs(args[1]-21):
    return 'win'
  elif args[0] == args[1]:
    return 'push'

def play_again():
  return input('Want to play another round? [y or n]: ').lower() == 'y'

# here starts the game
name = input('Welcome to BlackJack! What is your name?\n')
money = 100
player = Player(name,money)
casino = Player()
print(f'\nHi {player.name}. The sum of your coins is {player.money}[USD].')

while True:
  game_over = False
  deck = Deck()
  # first cards dealt
  cas_hand = casino.hand([],deck.cards)
  print('\nCasino:',[cas_hand[0],'???'])
  bet = int(input(f'\n{player.name}, place your bet [USD]: '))
  play_hand = player.hand([],deck.cards)
  print(f'\n{player.name}:',play_hand)
  while check_value(cas_hand) < 17:
    cas_hand = casino.hand(cas_hand,deck.cards)
  if check_value(play_hand) == 21:
    print('\nCasino:',cas_hand,check_value(cas_hand))
    game_over = True

  while game_over == False:
    hit_stand = input('Stand [Enter] or Hit [Space+Enter]?')
    if hit_stand == ' ':
      play_hand = player.hand(play_hand,deck.cards)
      print(f'\n{player.name}:',play_hand,check_value(play_hand))
      if check_value(play_hand) >= 21:
        print('\nCasino:',cas_hand,check_value(cas_hand))
        game_over = True

    elif hit_stand == '':
      print(f'\n{player.name}:',play_hand, check_value(play_hand))
      print('\nCasino:',cas_hand, check_value(cas_hand))
      game_over = True

  if player_win(check_value(play_hand),check_value(cas_hand)) == 'win':
    
    print(f'\n{player.name} wins! You have {player.amount(bet,True)} dollars.')

  elif player_win(check_value(play_hand),check_value(cas_hand)) == 'lose':

    if player.amount(bet,False) == 0:
      
      print('You lost all your money! Game over!')
      break

    print(f'{player.name} loses! You have {player.money} dollars left.')

  else:

    print(f'Push! You have {player.money} dollars to play with.')

  if play_again():
    pass
  else:
    break
