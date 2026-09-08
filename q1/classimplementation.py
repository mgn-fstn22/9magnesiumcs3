class Rogue: 
    def __init__ (self, name,  health_points, melee_damage, exp, basic_rogue_skills, brs_skill_points):
        self.name = name
        self.__health_points = 30
        self.melee_damage = 1
        self.__exp = 0
        self.basic_rogue_skills = {"Stab": 0, "Stealth": 0, "Trap Master" : 0, "Kick": 0, "Evasion":0, "Sneak Attack": 0, "Sprint": 0}
        self.__brs_skill_points = 2

    def skills(self):
        return self.basic_rogue_skills
    def LevelUpAttribute(self):

    def JoinGuild(self, guild_name):

    def EquipGear(self, item_name, item_category):

    def stab(self, target):

