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