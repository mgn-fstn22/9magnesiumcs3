# Computational Thinking Exercise
## Smart School Canteen Queue
**Name:** Megan Faustino 

**Section:** Magnesium 

**Last Name:** Faustino 

**Date Completed:** August 19, 2026 

---

## Step 1: Identify the Big Problem
### Main Problem
- The school canteen lunch service is inefficient and slow, resulting in long queues and a poor customer experience for PSHS students. The canteen's slow service is due to delays in ordering, manual payment processing, and a lack of inventory tracking.
---
## Step 2: Identify the Sub-Problems
1. Slow order decision-making
2. Slow and error-prone payment processing
3. Lack of real-time inventory and food tracking
4. Unorganized service flow
---
## Step 3: Apply Computational Thinking Skills
| Students take too long to decide what to order, causing delays in the queue. | Abstraction | Display a simple menu with the available food, prices, and a basic descriptions so students can quickly choose what to order.|
|---|---|---|
| Slow and error-prone payment processing | Algorithm Design | Create a step-by-step processs that automatically calculates the total, accepts the payment, and calculates the correct changes---just like a cashier register. |
|---|---|---|
| Lack of real-time inventory tracking | Pattern recognition | Track the quantity of each food item and set a warning when the quantity of a food item reaches a certain level, such as 5 items remaining. |
|---|---|---|
| Unorganized service flow | Decomposition | Assign separate stages for ordering, payment, and pickup so students move through the process in an organized sequence. |
|---|---|---|
---
## Step 4: Algorithmic Solution
### Sub-Problem No. 3
- Track the quantity of each food item and set a warning when the quantity of a food item reaches a certain level, such as 5 items remaining.

### Pseudocode
START
Set the warning level to 10 items

Check the quantity of each food item

IF quantity == 0 THEN

    Display food item name

    Display "OUT OF STOCK"

    Mark the food as unavailable and needs to be restocked

ELIF quantity <= 5 THEN

    Display food item name

    Display "LOW STOCK"

    Display the remaining quantity and label as low stock

ELSE

    Display food item name

    Display "AVAILABLE"

    Display the remaining quantitiy

END IF

When student buys a food item:

    Subtract the quantity purchased from the current stock

    Check the remaining stock

IF remaining quantity <= 5 THEN

    Display "WARNING: LOW STOCK"

ELIF remaining quantity > 5 THEN

    Display "STILL AVAILABLE"

ELSE

    remaining quantity = 0 THEN

    Display "OUT OF STOCK"

    Mark the food item as unavailable

END IF

Update the inventory

END
