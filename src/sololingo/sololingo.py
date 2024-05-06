import random
import os

class Sololingo:
    def __init__(self):
        self.cards = []
        self.streak = 0
        self.bestStreak = 0
        self.loadCards('cards.txt')
        self.newCard()

    def saveCards(self, filename):
        with open(filename, 'w') as f:
            for card in self.cards:
                f.write(f"{card.korean},{card.english},{card.pronunciation},{card.lvl},{card.score}\n")
    def loadCards(self, filename):
        with open(filename, 'r') as f:
             for line in f:
                if line.startswith('bestStreak'):
                    self.bestStreak = int(line.strip().split('=')[1])
                else:
                    korean, english, pronunciation, lvl, score = line.strip().split(',')
                    self.cards.append(Card(korean, english, pronunciation, int(lvl), int(score)))
    def newCard(self):
        self.currentCard = random.choice(self.cards)
        self.choices = random.sample(self.cards, 3)
        while self.choices.count(self.currentCard) != 1:
            self.choices = random.sample(self.cards, 3)

class Card:
    def __init__(self, korean, english, pronunciation, lvl, score=0):
        self.korean = korean
        self.english = english
        self.pronunciation = pronunciation
        self.lvl = lvl
        self.score = 0
