class Rogue:
    def __init__(self, name, brs_skill_points, guild_name, equipped_gear, health_points, melee_damage, exp, basic_rogue_skills):
        self.name = name
        self.guild_name = guild_name
        self.equipped_gear = {}
        self.basic_rogue_skills = {"Archery": 0, "Evasion": 0, "Kick": 0, "Sneak Attack": 0, "Sprint": 0, "Stab": 0, "Stealth": 0, "Trap Master": 0}

        self.__melee_damage = 1
        self.__exp = 0
        self.__health_points = 30
        self.__brs_skill_points = 2

    
