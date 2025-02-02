# Uncommon Code Error: Handling Non-Numeric Values in Average Calculation
This repository demonstrates an uncommon code error in Python related to handling non-numeric values when calculating the average of a list.  The initial code handles empty lists gracefully but fails when encountering non-numeric data types within the list, resulting in a `TypeError`. The solution demonstrates robust error handling using a `try-except` block to prevent unexpected crashes.

## Bug Description
The `calculate_average` function correctly handles empty lists, returning 0. However, if the input list contains a string or other non-numeric element, the `sum()` function will raise a `TypeError`. This unexpected behavior is the bug.

## Solution
The solution adds a `try-except` block to gracefully handle potential `TypeError` exceptions. It filters out non-numeric values before performing the average calculation, ensuring the function remains robust and prevents application crashes.