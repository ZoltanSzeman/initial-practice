import os

def play_again():
  play = ''
  while play != 'I' and play != 'N':
    play = input('\nAkartok újra játszani? I vagy N: ').upper()
  return play == 'I'

# check for winner
def check_for_win(xo, shape):
  return (xo[0:3] == [shape]*3) or (xo[3:6] == [shape]*3)\
  or (xo[6:9] == [shape]*3) or (xo[0:7:3] == [shape]*3)\
  or (xo[1:8:3] == [shape]*3) or (xo[2:9:3] == [shape]*3)\
  or (xo[0:9:4] == [shape]*3) or (xo[2:7:2] == [shape]*3)\

# draw the game board every round
def board(xo):
  os.system('cls') #use 'clear' for linux
  print(f'{xo[6]}|{xo[7]}|{xo[8]}')
  print('- - -')
  print(f'{xo[3]}|{xo[4]}|{xo[5]}')
  print('- - -')
  print(f'{xo[0]}|{xo[1]}|{xo[2]}')
  if xo == demo_list:
    ok = 'Wait for user input'
    while not ok == '':
      print('\n2játékos 3X3 tic-tac-toe')
      ok = input('\nFentebb látható a pozíció kiosztás.'
      '\nA játék során be kell ütni a pozíciónak megfelelő számot,'
      '\nhogy elhelyezd a formát a táblán.'
      '\n\nHa érthető, akkor nyomj Enter-t és kezdődjön a játék!')

# global game counter set to 0
count = 0
# player input management
while True:
  demo_list = list(range(1,10))
  if count == 0: # intro to the game
    board(demo_list)
  count += 1 # counting each game
  play_list = [' '] * 9 # clear the board
  free_space = demo_list

  player1 = input('\n1-es játékos, írd be a neved: ')
  player2 = input('\n2-es játékos, írd be a neved: ')
  shape1 = ' '
  while not shape1 in ['X','O']:
    shape1 = input(f'\n{player1}, X vagy O: ').upper()
  if shape1 == 'X':
    print(f'\n{player2}, tiéd az O')
    shape2 = 'O'
  else:
    print(f'\n{player2}, tiéd az X')
    shape2 = 'X'

# start 1st round and check for win
  game_round = 0
  while not game_round == 9:
    if game_round%2 == 0:
      pos = int(input(f'\n{player1}, válassz pozíciót [1-9]:'))
      while not pos in free_space:
        pos = int(input(f'\nTéves, {player1}! Válassz szabad pozíciót [1-9]:'))
      play_list[pos-1] = shape1
      free_space.remove(pos)
      board(play_list)
      if check_for_win(play_list, shape1):
        print(f'{player1} nyert!\n\n{count}. játéknak vége!')
        break
    else:
      pos = int(input(f'\n{player2}, válassz pozíciót [1-9]:'))
      while not pos in free_space:
        pos = int(input(f'\nTéves, {player2}! Válassz szabad pozíciót [1-9]:'))
      play_list[pos-1] = shape2
      free_space.remove(pos)
      board(play_list)
      if check_for_win(play_list, shape2):
        print(f'{player2} nyert!\n\n{count}. játéknak vége!')
        break
    game_round += 1
  # is it a tie?
  if not check_for_win(play_list, shape1) and not check_for_win(play_list,shape2):
    print(f'{player1} és {player2}, ez biza döntetlen.\n\n{count}. játéknak vége!')
  # play again?
  if play_again():
    pass
  else:
    break
