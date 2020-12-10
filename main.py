from creatures import *
from heroes import *
from random import randint
phrases = []


def get_bobs_phrases():
    with open(r"C:\Users\админ\Desktop\ИТ(Ч)МО\Прога.Питон\lab4-main\bobik.txt", 'r', encoding='UTF-8') as file:
        for line in file:
            phrases.append(line[line.index('	')+1: len(line)])


def say_bobs_phrase():
    print('Bob: ', phrases[randint(0, len(phrases)-1)])


class Player:

    def __init__(self, tavern_tier, players_name):
        super().__init__()
        self.tavern_tier = tavern_tier
        self.players_name = players_name
        self.gold = 10
        self.minions = []
        self.hero = ''

    def buy_minion(self, minion):
        if self.gold >= 0:
            self.gold -= 3
            self.minions.append(str(minion))
        else:
            print('Not enough gold!')

    def sell_minion(self, minion_name):
        flag = 0
        for i in self.minions:
            temp = i.find(minion_name)
            if temp != -1:
                del self.minions[flag]
            flag += 1
        print('Минус одно существо, плюс один золотой!')
        self.gold += 1

    def get_text(self):
        print('////////////////////////////////////////////////////')
        say_bobs_phrase()
        print(f'Player: {self.players_name} Gold: {self.gold}\n{self.hero} \nTavern Tier:{self.tavern_tier} \nMinions:')
        for i in self.minions:
            print(i)
        print('////////////////////////////////////////////////////')

    def choose_hero(self, hero):
        self.hero = hero


get_bobs_phrases()
player1 = Player(5, 'argENTvm')
xBet = LordBarov()
player1.choose_hero(xBet)
player1.get_text()
khadgar = Khadgar()
player1.buy_minion(khadgar)
player1.get_text()
brann = BrannBronzebeard()
player1.buy_minion(brann)
player1.get_text()
player1.sell_minion('Khadgar')
player1.sell_minion('brann')
player1.get_text()
