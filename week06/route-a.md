My template: ---
name: facebook-marketplace
description: create a facebook marketplace description based on given information.
argument hint: ITEM CONDITION DETAILS
---
Inputs

SKILL.md: Microsoft Word 2007+
Facebook-post
Inputs
ITEM (The item being posted)
CONDITION (New, like new, fair, good)
DETAILS (A few supporting details to enhance description)
Steps
Generate a short description of the item. Things to include are measurements where relevant, specifications, who might enjoy the item, year manufactured if available, anything from DETAILS.
Find a fair price for the item based on description and condition.
Output
Exactly this shape, and nothing else:
Item: ITEM (and nothing else)
Price: ANSWER (And nothing else. Use DETAILS and CONDITION to help determine a fair price.)
Condition: CONDITION (and nothing else)
Description: ANSWER (Nothing else. Use DETAILS and CONDITION to help support your output.)

Both claude and Opencode were able to  keep the output shape, using the condition and details I added to generate a good price and description
