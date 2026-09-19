class AvailableCompanions:
    def __init__(self, name: str, level:int, health: int, skills: str, exp: int):
        self.name = name
        self.health = health
        self.__level = level
        self.__skills = []
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
        self.available_companions = []

    def add_available_companions(self, companion: AvailableCompanions):
        self.available_companions.append(companion)

player = Rogue("Ryella Leeds", 17, 1314)

grissenda = AvailableCompanions("Grissenda", 16, 1080, "None" ,215976)

adaon = AvailableCompanions("Adaon", 14, 899, "None" ,138095)

hirge = AvailableCompanions("Hirge", 16, 1082,"None", 216745)

player.add_available_companions(grissenda)
player.add_available_companions(adaon)
player.add_available_companions(hirge)


print("\n⊹₊˚‧︵‿₊⊱·✶·⊰₊‿︵‧˚₊⊹")
print("「 Exiled Kingdoms 」")
print("₊˚ ✧ ━━━━⊱⋆⊰━━━━ ✧ ₊˚")

print(f"\n*ੈ✩‧₊˚༺ Journey of {player.name}  ༻*ੈ✩‧₊˚")
print(f"\nAs {player.name} continuess to progress through the Exiled Kingdoms, they met three adventurers with the same goal of protecting the four kingdoms:")
for companion in player.available_companions:
    print(f"\n{companion.name} (Level {companion._AvailableCompanions__level}) - Health: {companion.health}, Skills: {companion._AvailableCompanions__skills}, Experience: {companion._AvailableCompanions__exp}")

print(f"\n*ੈ✩‧₊˚༺ {player.name} recruits companions ༻*ੈ✩‧₊˚")
for companion in player.available_companions:
    print(f"\n{player.name} recruits {companion.name} to join their party and help them in their journey to uncover\n the secrets of the Exiled Kingdoms and protect the four kingdoms.")

print(f"\n--- {player.name} and companions' level and experience ---")
print(f"\n{player.name} (Level {player._Rogue__level}) - Health: {player._Rogue__health}")
for companion in player.available_companions:
    print(f"\n{companion.name} (Level {companion._AvailableCompanions__level}) - Health: {companion.health}")

print(f"\n*ੈ✩‧₊˚༺ {player.name} and party's next quest is to defeat the main villains ༻*ੈ✩‧₊˚")
print(f"\nAs {player.name} and their companions continue their journey, they now have to face the main villains, the Muud'ari, headed by the Magister. \n \n---The Muud'ari are advanced, space-faring, technological species from the plaent Noutamet who crashed in our planet and became stranded in Varannar, \nafter a failed attempt to go back to their home through the original land of the Exiled Kingdoms, Andoria.---")

print(f"\n---{player.name} and part prepares for battle---")
grissenda.learn_skill("Bash")
adaon.learn_skill("Kick")
hirge.learn_skill("Nivaria's Barrier")
grissenda.gain_xp(100)
adaon.gain_xp(300)
hirge.gain_xp(100)
grissenda.take_damage(20)
adaon.take_damage(25)
hirge.take_damage(15)

print(f"\n {player.name} teaches their companions new skills and they gain experience from training, \nHowever, due to intense practice, they take some damage.")
print(f"\n--- {player.name} and companions' level and experience after training ---")
print(f"\n{player.name} - Level {player._Rogue__level}")
for companion in player.available_companions:
    print(f"\n{companion.name} - Level {companion._AvailableCompanions__level}, Health: {companion.health}, Skills: {companion._AvailableCompanions__skills}, Experience: {companion._AvailableCompanions__exp}")

print(f"\n*ੈ✩‧₊˚༺ {player.name} and party will now face the Muud'ari at the Ark of Lothasan ༻*ੈ✩‧₊˚")
print(f"\nBest of Luck to {player.name} and their companions. \n\nMay they succeed in protecting the four kingdoms and uncover the secrets of the Exiled Kingdoms.\n")