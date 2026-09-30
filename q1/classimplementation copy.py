class Rogue:
    def __init__(self, name, brs_skill_points, guild_name, equipped_gear, health_points, melee_damage, exp, basic_rogue_skills):
        self.name = name
        self.melee_damage = 1
        self.guild_name = guild_name
        self.equipped_gear = {}
        self.basic_rogue_skills = {"Archery": 0, "Evasion": 0, "Kick": 0, "Sneak Attack": 0, "Sprint": 0, "Stab": 0, "Stealth": 0, "Trap Master": 0}

        self.__melee_damage = 1
        self.__exp = 0
        self.__health_points = 30
        self.__brs_skill_points = 2

        
    def skills(self):
        return self.basic_rogue_skills

    def LevelUpAttributes(self, skill_name):
        
        if skill_name in self.basic_rogue_skills:

            if self.__brs_skill_points > 0:
                self.basic_rogue_skills[skill_name] += 1
                self.__brs_skill_points -= 1

                return f"{skill_name} has been leveled up to {self.basic_rogue_skills[skill_name]}."

            else:
                return "Not enough skill points to level up."

        else:
            return f"{skill_name} is not a valid skill of a rogue."

    def JoinGuild(self, guild_name):
        if self.guild_name is None:
            self.guild_name = guild_name
            return f"{self.name} has joined the guild {guild_name}."
        else:
            return f"{self.name} is already a member of the guild {self.guild_name}."

    def EquipGear(self, item_name, item_category):
        if item_category in self.equipped_gear:
            return f"{item_name} is already equipped."
        else:
            self.equipped_gear[item_category] = item_name
            return f"{item_name} has been equipped in the {item_category} category."

    def stab(self, target):
        if self.basic_rogue_skills["Stab"] > 0:
            damage = self.__melee_damage + self.basic_rogue_skills["Stab"]
            target._Rogue__health_points -= damage
            if target._Rogue__health_points < 0:
                target._Rogue__health_points = 0
            return f"{self.name} stabbed {target.name} for {damage} damage."
        else:
            return f"{self.name} does not have the Stab skill leveled up."

class RangedArcher:
    def __init__(self, name: str, hp: int, damage: int, arrow_count: int):
        self.name = name
        self.arrow_count = arrow_count
        self.__hp = hp
        self.__damage = damage

    def attack(self, target):
        if self.arrow_count > 0:
            target._RangedArcher__hp -= self.__damage
            self.arrow_count -= 1
            if target._RangedArcher__hp < 0:
                target._RangedArcher__hp = 0
                print(f"{target.name} has been defeated.")
        else:
            print(f"{self.name} has no arrows left to attack.")

    def reload_arrows(self, count):
        self.arrow_count += count
        print(f"{self.name} has reloaded {count} amount of arrows.\n Current arrow count: {self.arrow_count}")

    def aim(self, target):
        if self.arrow_count > 0:
            print(f"{self.name} is aiming at {target.name}")
        else:
            print(f"{self.name} has no arrows left to aim.")

