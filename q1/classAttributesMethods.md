# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)


## Design Revisions
### Properties
| **Original** | **Revisions** | **Reason** |
| --- | --- | --- |
| **Additional Property:** name | Added property | The rogue character must have a name. |
|**Additional Property:** brs_trait_points | Added property | Since the basic rogue skills level up, it is necessary to have a variable about the number of trait points allotted to the skills. |
|**Additional Property:** ars_trait_points | Added property | Since the advanced rogue skills also level up, it is necessary to have a variable that will store the amount of trait points that each advance rogue skills gets. |
| Health Points (HP) | **health_points** | The new variable name follows the Python snake_case convention; it is easier and more recognizable. |
| Melee Damage | **melee_damage** | Similar reason for variable health_points; the snake_case would create consistency in naming variables. | 
| Experience Points (exp) | **exp** | The variable name "exp" is often used in RPG games as an acronym for the word: experience. |
| Advanced Rogue Skills | **advance_rogue_skills** | Replace the spaces with underscores to create a valid variable name. |
| Basic Rogue Skills | **basic_rogue_skills** | Same as above. |

### Methods
| **Original** | **Revisions** | **Reason** |
| --- | --- | --- |
| Level Up | **LevelUp()** | A Python standard naming method that removes the space. |
| Join Guild | **JoinGuild()** | Consistent PascalCase for methods. |
| Equip Armor or Weapon | **EquipGear()** | A shorter version of equipping items, but still clear. |

-------
## Visibility Decisions

| **Attribute** | **Data Type** | **Visibility** | **Reason** |
| --- | --- | --- | --- |
| **health_points** | int | Private | Health point is an important survival statistics, and it must be modified only inside the class. This can prevent invalid values, cheating, and breaking the game. |
| **melee_damage** | int | Public | This property is necessary for combat calculation and UI display in Exiled Kingdoms, so it must be a public attribute that can be changed by external code. |
| **exp** | int | Private | Just like for health points, this attribute must be private so that there will be no modifications in the code that will affect how the character or rogue can level-up or how much exp they can gain per kill. |
| **advance_rogue_skills** | str | Public | Again, this property is often accessible only to players who have unlocked guilds. Personally, I think it's fine that it gets displayed and the public can read it because skills are and have a fixed level per point. |
| **basic_rogue_skills** | str | Public | This is the fixed basic set of skill that are already displayed, so it is safe to be a public attribute. |
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

### Which method changes the state of your object?

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagrama and your object diagram?
