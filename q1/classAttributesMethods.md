# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)


## Design Revisions
### Properties
| **Original** | **Revisions** | **Reason** |
| --- | --- | --- |
| **Additional Property:** name, string | Added property | The rogue character must have a name. |
|**Additional Property:** brs_skill_points, integer | Added property | Since the basic rogue skills level up, it is necessary to have a variable about the number of trait points allotted to the skills. |
|**Additional Property:** guild_name, string | Added property | The guild the character/rogue joined. |
|**Additional Property:** equipped_gear, string | Added property | What weapons and armors the rogue has equipped. |
| Health Points (HP) | **health_points** | The new variable name follows the Python snake_case convention; it is easier and more recognizable. |
| Melee Damage | **melee_damage** | Similar reason for variable health_points; the snake_case would create consistency in naming variables. | 
| Experience Points (exp) | **exp** | The variable name "exp" is often used in RPG games as an acronym for the word: experience. |
| Basic Rogue Skills | **basic_rogue_skills** | Same as above. |

- Added other properties, but removed the advanced rogue skills.

### Methods
| **Original** | **Revisions** | **Reason** |
| --- | --- | --- |
| Level Up | **LevelUpAttribute()** | A Python standard naming method that removes the space. Moreover, the definition of Level Up is only adding points to the basic rogue skills. |
| Join Guild | **JoinGuild()** | Consistent PascalCase for methods. |
| Equip Armor or Weapon | **EquipGear()** | A shorter version of equipping items, but still clear. |
- Add the method skill which will display all rogue skills.
-------
## Visibility Decisions

| **Attribute** | **Data Type** | **Visibility** | **Reason** |
| --- | --- | --- | --- |
| **name** | str | Public | This variable can be edited by external source it isn't a major component of the character. It's more on identification rather than skills, money, and experience. |
| **health_points** | int | Private | Health point is an important survival statistics, and it must be modified only inside the class. This can prevent invalid values, cheating, and breaking the game. |
| **melee_damage** | int | Public | This property is necessary for combat calculation and UI display in Exiled Kingdoms, so it must be a public attribute that can be changed by external code. |
| **exp** | int | Private | Just like for health points, this attribute must be private so that there will be no modifications in the code that will affect how the character or rogue can level-up or how much exp they can gain per kill. |
| **basic_rogue_skills** | str | Public | This is the fixed basic set of skill that are already displayed, so it is safe to be a public attribute. |
| **brs_skill_points** | int | Private | Trait points should only be in the class so it won't be edited by external codes to add or minus trait points to certain character. |
| **guild_name** | str | Public | This property does not need strict monitoring becaus this is just guild name. |
| **equipped_gear** | str | Public | This property also can be public because this only contains what gear the character currently have right now. |


--- 
## Updated UML Class Diagram
- View my Update UML Diagram

## Python Implementation
[View Python Source](classimplementation.py)

## Test Run
- Link

## Object Diagram
- Link

---
## Analysis

### Why did you make your chosen attribute private?
- Certain attributes are meant to private because external codes must not be able to access them to make the game fair. The whole purpose of an RPG game is to roleplay, not to create modifications that would make it unfair. The private attributes are health_points, exp, brs_skill_points, and ars_skill_points because personally these properties are the foundation of the game and if one of them got corrupted then the whole game will lose its purpose.

### Which method changes the state of your object?

- The method that changes the state of the object is LevelUpAttributes because after leveling up each attribute. The rogue will enhance their skills and they will be able to do much more than melee damage and basic combat.

### How did your two objects demonstrate that instances are independent?
- Both objectes demonstrate that the instances are independent through

### What is the difference between your class diagrama and your object diagram?
- My class diagram is the blueprint for the object diagram. The class diagram will discuss the necessary parts, while the object diagrams will give the values for the said variables.


# Declaration of Use of AI:
- I used Google Gemini to further understand Object-Oriented Programming. I asked Gemini to give me an example of a .py about classes and object. Moreover, here in VSCode the autofill feature was used, but I modified some of the autofilled codes. 