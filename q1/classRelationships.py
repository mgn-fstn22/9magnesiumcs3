class AvailableCompanions:
    def __init__(self, name: str, level:int, health: int, skills: str, exp: int):
        self.name = name
        self.health = health
        self.__level = level
        self.__skills = {}
        self.__exp = exp

    def gain_xp(self, amount:int):
        self.__exp += amount

        required_exp = self.__level * 100
        if self.__exp >= required_exp:
            self.__level += 1
            self.__exp -= required_exp
            return (f"{self.name} has leveled up to level {self.__level}.")

    def learn_skill(self,skill_name: str):
        self.__skills.append(skill_name)

    def take_damage(self, damage:int):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            return (f"{self.name} is unconscious and cannot continue the fight. Player must first defeat enemy.")

class Rogue:
    def __init__(self, name: str, level: int, health:int):
        self.name = name
        self.__level = level
        self.__health = health
        self,available_companions = []

    def add_available_companions(self, companion: AvailableCompanions):
        self.available_companions.append(companion)

player = Rogue("Ryella Leeds", 17, 1314)

grissenda = AvailableCompanions("Grissenda", 16, 1080, "Whirlwind", 215976)

adaon = AvailableCompanions("Adaon", 14, 899, "Stab", 138095)

hirge = AvailableCompanions("Hirge", 16, 1082, "Heal Wounds", 216745)

Rogue.add_available_companions(grissenda)
Rogue.add_available_companions(adaon)
Rogue.add_available_companions(hirge)


print("⊹₊˚‧︵‿₊⊱·✶·⊰₊‿︵‧˚₊⊹")
print("Exiled Kingdoms")