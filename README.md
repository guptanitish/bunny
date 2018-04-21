A simple class representing a bunny hopping in a garden and eating carrots. hop. hop. hop.

## Assumptions

Bunny can look only right, down, left, and up, from any given  position.
In case of tie for the number of carrots, bunny will choose one
position to hop to - in this order of preference - right, down, left and up. In such 
a case, bunny could have eaten more carrots had it hopped to a different
location when breaking ties. This implies that 
solution may be suboptimal, due to bunny hopping to the next position in a
greedy manner.

## Requirements

Python 2.7

## To run

> python test_bunny.py 


bunny.py contains implementation.

test_bunny.py contains test cases.

