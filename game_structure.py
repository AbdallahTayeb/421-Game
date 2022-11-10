import random

class Dice:

    def __init__(self):
        self.value = None

    def __str__(self):
        return f"Dice value : {self.value}"

    def roll(self):
        self.value = random.randint(1,6)
        return self.value

    
class Hand:
    def __init__(self,d1,d2,d3):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        
    
    
    def throw(self,k=['d1','d2','d3']):
        if 'd1' in k:
            self.d1.roll()
        if 'd2' in k:
            self.d2.roll()
        if 'd3' in k:
            self.d3.roll()
        print((self.d1.value,self.d2.value,self.d3.value))
        
    def get_score(self):
        return tuple(sorted((self.d1.value,self.d2.value,self.d3.value),reverse=True))
        
class Player():
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
        self.balance = 0

    def play(self):
        print(f"{self.name} turn ...")
        self.hand.throw()
        for i in range(2):
            answer = input("Do you want to roll again ?").strip()
            if answer == "stop":
                break
            else:
                self.hand.throw(answer)
        print(f"{self.name} final's score {self.hand.get_score()}")
        return self.hand.get_score()

    def deposit(self, amount):
        self.balance += amount

class Bank():
    def __init__(self,fishes):
        self.fishes = fishes

    def withdraw(self,value,player):
        player.deposit(min(self.fishes,value))
        self.fishes = max(0,self.fishes-value)


def get_score(value,scores):
    if value in scores.keys():
        score = scores[value]
    else:
        score = 1
    return score
