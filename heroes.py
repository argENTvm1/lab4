class Hero:
    def __init__(self):
        self.health = 40
        self.heropower_name = ''
        self.heropower_ability = ''
        self.name = ''
        self.hero = f'\nHero: {self.name} Health:{self.health},' \
                    f' \nHero Power: {self.heropower_name} ({self.heropower_ability})'

    def __repr__(self):
        return f'\nHero: {self.name} Health:{self.health},' \
               f' \nHero Power: {self.heropower_name} ({self.heropower_ability})'


class ArchVillainRafaam(Hero):
    def __init__(self):
        super().__init__()
        self.health = 13
        self.heropower_name = "I'll take that!"
        self.heropower_ability = 'Next combat, add a plain copy of the minion you kill to your hand'
        self.name = 'Arch-Villian Rafaam'


class Galakrond(Hero):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.heropower_name = "Galakrond's greed"
        self.heropower_ability = "Replace a minion in Bob's Tavern with one from a higher Tavern Tier"
        self.name = 'Galakrond'


class LordBarov(Hero):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.heropower_name = "Friendly Wager"
        self.heropower_ability = "Guess which player will win next combat. If they win, get 3 coins"
        self.name = 'Lord Barov'


class Ragnaros(Hero):
    def __init__(self):
        super().__init__()
        self.health = 31
        self.heropower_name = "DIE, INSECTS!"
        self.heropower_ability = "After you kill 25 enemy minions, get Sulfuras."
        self.name = 'Ragnaros, The firelord'


class RenoJackson(Hero):
    def __init__(self):
        super().__init__()
        self.health = 38
        self.heropower_name = "Gonna be rich!"
        self.heropower_ability = "Make a Friendly minion Golden.(Once per game.)"
        self.name = 'Reno Jackson'


class TheCurator(Hero):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.heropower_name = "Menagerist"
        self.heropower_ability = "Start the game with a 1/2 Amalgam with all minion types"
        self.name = 'The Curator'


class Yogg(Hero):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.heropower_name = "Puzzle Box"
        self.heropower_ability = "Add a random minion in Bob's Tavern to your hand. Give it +1/+1"
        self.name = "Yogg-Saron, Hope's End"


class LichKing(Hero):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.heropower_name = "Reborn Rites"
        self.heropower_ability = "Give a friendly minion Reborn for the next combat only"
        self.name = "The Lich King"
