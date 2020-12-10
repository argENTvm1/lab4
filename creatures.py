class Minion:

    def __init__(self):
        self.health = 0
        self.attack = 0
        self.type = ''
        self.tier = 0
        self.ability = ''
        self.name = ''
        self.minion = f'\n{self.name} \nHealth: {self.health}, Attack: {self.attack}, Type: {self.type}, ' \
                      f' Tier: {self.tier}, Ability: {self.ability}'

    def attack(self, enemy):
        pass

    def __repr__(self):
        return f'\n{self.name} \nHealth: {self.health}, Attack: {self.attack}, Type: {self.type}, ' \
               f' Tier: {self.tier}, Ability: {self.ability}'


class MurlockTidehunter(Minion):

    def __init__(self):
        super().__init__()
        self.health = 1
        self.attack = 2
        self.type = 'Murlock'
        self.tier = 1
        self.ability = 'Battlecry: Summon a 1/1 Murlock Scout.'
        self.name = 'Murlock Tidehunter'


class BrannBronzebeard(Minion):

    def __init__(self):
        super().__init__()
        self.health = 4
        self.attack = 2
        self.type = 'None'
        self.tier = 5
        self.ability = 'Your battlecries trigger twice.'
        self.name = 'Brann Bronzebeard'


class Khadgar(Minion):

    def __init__(self):
        super().__init__()
        self.health = 2
        self.attack = 2
        self.type = 'None'
        self.tier = 3
        self.ability = 'Your cards that summon minions summon twice as many.'
        self.name = 'Khadgar'


class MamaBear(Minion):

    def __init__(self):
        super().__init__()
        self.health = 4
        self.attack = 4
        self.type = 'Beast'
        self.tier = 5
        self.ability = 'Whenever you summon a beast, give it +4/+4.'
        self.name = 'Mama Bear'


class LightfangEnforcer(Minion):

    def __init__(self):
        super().__init__()
        self.health = 2
        self.attack = 2
        self.type = 'None'
        self.tier = 5
        self.ability = 'At the end of your turn, give a friendly minion of each type +2/+2.'
        self.name = 'Lightfang Enforcer'
