from objects import Dice, Hand, Player
from rules import rules

if __name__ == "__main__":
  name1 = input("Player 1 ? ")
  name2 = input("Player 2 ? ")

  player1 = Player(name=name1,hand=Hand(Dice(),Dice(),Dice()))
  player2 = Player(name=name2,hand=Hand(Dice(),Dice(),Dice()))


  score1 = player1.play()
  score2 = player2.play()

  if rules.index(score1)<rules.index(score2):
      print(f"{score1}>{score2} {player1.name} win")
  elif rules.index(score1)>rules.index(score2):
      print(f"{score2}>{score1} {player2.name} win")      
  else:
      print("Photo")
