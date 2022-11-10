from game_structure import Dice, Hand, Player, Bank, get_score
from set_rules import rules, scores

if __name__ == "__main__":
  name1 = input("Player 1 ? ")
  name2 = input("Player 2 ? ")
  
  referee = Bank(fishes = 11)

  player1 = Player(name=name1,hand=Hand(Dice(),Dice(),Dice()))
  player2 = Player(name=name2,hand=Hand(Dice(),Dice(),Dice()))

while referee.fishes > 0 :
  
  score1 = player1.play()
  score2 = player2.play()

  if rules.index(score1)<rules.index(score2):
      print(f"{score1}>{score2} {player1.name} win")
      referee.withdraw(value = get_score(score1,scores), player = player2)
  elif rules.index(score1)>rules.index(score2):
      print(f"{score2}>{score1} {player2.name} win") 
      referee.withdraw(value = get_score(score2,scores),player = player1)    
  else:
      print("Photo")

  print(f"Bank : {referee.fishes}, {name1} : {player1.balance}, {name2} : {player2.balance}")
  

  

