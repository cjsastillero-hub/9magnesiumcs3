# Class Relationships: Association and Multiplicity
## Name: Christine Joyce S. Astillero
## Section: 9 - Magnesium
## Date: 9/19/2026
## School Year: 2026-2027
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Pop Songs
Description: A class that represents or stores all kind of given pop songs.

## New Related Class
Class: Playlist
Description: A class that generally stores songs and disregards its assigned genre/type.

## Association
Relationship: specific to general
Explanation: The two classes are related because the existing class is specific or is focused on one type of category, while the new class can be a mosaic of different type of genres/classes. i like to think of the new class as an empty canvas, the past class represents one brush stroke and if more classes are created, it could create one beautiful picture.

## Multiplicity
Multiplicity: One-to-Many
Explanation: Many objects can be related to the new class due to the fact that there are countless songs from varying genres that were composed for the past 100 years.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
The first class focuses on a specific field/category while the second class is a combination of the first and possibly other classes.
### What multiplicity did you choose and why?
i chose one to many because i believe that a playlist needs many and a diverse set of objects/options for it to be entertaining and to not be too simple.
### How did you implement the relationship in Python?

### Why did you store an object reference instead of copying its data?

### If your relationship uses many, why is a list appropriate?