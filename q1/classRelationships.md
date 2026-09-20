# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

---

## Existing Class
**Class:** Rogue - Exiled Kingdoms

**Description**: 
- Rogues are often called as thieves in the game, **Exiled Kingdom**. These characters possess unique abilities such as Stab, Trap, and Sprint. Moreover, to further enhance the Rogue, they can join guilds to learn a new set of advanced skills.

## New Class
**Class:** Available Companion

**Description:** In **Exiled Kingdom,** there are companions that are NPC's that can join the rogue on the journey or storyline of the game. Companions will follow and assist the rogue in attacking enemies. Companions have four types: Main Companions, Hired Mercenaries, Summond Creatures, and Quest NPC's. In this class, I wll focus on Main Companions

## Association 
**Relationship:** A rogue has companions.
**Explanation:** Again, the game contains companions which has only one goal---to help the main character (rogue). Moreover, the main companions have quests that can help the rogue to level up and gain new armor and weapon.

## Multiplicity
**Multiplicity:** *one-to-many*
**Explanation**: Since there are four types of companions, I chose to focus on the main companions, and the rogue has 3 available companions, but can only have one at a time. (1 Rogue : 3 Available Companions)

---

## UML Class Relationship Diagram
[Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
[Object Relationship Diagram]()

--- 

## Analysis

### What is the association between your two classes?
- 
### What multiplicity did you choose and why?
- 
### How did you implement the relationship in Python?
- 
### Why did you store an object reference instead of copying its data?
- 
### If your relationship uses many, why is a list appropriate?
- 

## Declaration of AI
- During the preparation of this activity, I used Gemini 3.6 Flash and Chat GPT-6 Astra to improve my code through identifying errors. Moreover, I used these LLMs to further understand the concepts. After using the said tools, I reviewed and edited the content as needed.

## Reference:
Companions - Exiled Kingdoms Wiki. (n.d.). https://www.exiledkingdoms.com/wiki/index.php?title=Companions
