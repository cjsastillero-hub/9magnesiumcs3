# Class Relationships: Association and Multiplicity
## Name: Christine Joyce S. Astillero
## Section: 9 - Magnesium
## Date: 9/19/2026
## School Year: 2026-2027
## Previous Work
[Part I - Classes and Objects](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/classObjectUML.md)

[Part II - Class Attributes and Methods](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/classAttributesMethods.md)
## Existing Class
Class: Pop Songs
Description: A class that represents or stores all kind of given pop songs.

## New Related Class
Class: Song Compiler
Description: A class that generally stores songs and accepts all songs from carying genres.

## Association
Relationship: contains
Explanation: The two classes are related because the existing class is specific or is focused on one type of category, while the new class can be a mosaic of different type of genres/classes. i like to think of the new class as an empty canvas, the past class represents one brush stroke and if more classes are created, it could create one beautiful picture of the new class.

## Multiplicity
Multiplicity: One-to-Many
Explanation: Many objects can be related to the new class due to the fact that there are countless songs from varying genres that were composed in the span of a long time.

## UML Class Relationship Diagram
![Class Relationship Diagram](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/classRelationshipDiagram.jpg)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
The first class represents the songs who are under a specific genre/category, and in this case that genre is pop. Meanwhile, the second class compiles those songs under one object. The class is not limited to one genre, there could be multiple compiled songs with different genres, the only condition is that each object must compile songs with the same genre. So you have to create a new object under Song_Compiler if the new song does not match with the genre of rest of the stored songs in an already existing object.
### What multiplicity did you choose and why?
i chose one to many because i believe that a song compiler needs many and a diverse set of objects for it to be entertaining and to not be too simple. The class Song_Compiler needs multiple objects/songs for it to reach its full potential anf for it to be utilized properly. This is because the class is created for the purpose of organizing songs from different genres in an systematic and simple manner. 
### How did you implement the relationship in Python?
i implemented it by calling a method from an object created from the class Song_Compiler, with an object from the class PopSongs as the parameter. The method will input the parameter into a list called compiled_songs, and since the method was implemented from the object CompiledSongs1, the song/object that became a parameter will be stored in the compiler list under CompiledSongs1. So now, the objects from two different classes are connected and have access to the same information.

### Why did you store an object reference instead of copying its data?
Storing an object reference reduces the length of the data and simplifies it, it is like a box inside a box. The list is the bigger box while the object reference is the smaller box, inside the smaller box are blocks that represent the data fields and methods of that object. However, if we just copy the data there would be no smaller box, it would instead be many blocks from different objects which becomes unorganized and very hard to debug.

### If your relationship uses many, why is a list appropriate? Explain what the list actually contains.
it is appropriate because it prevents the code from being long and unorganized. The list encapsulates the data in an orderly manner, which reduces the length and complexity of the code. The list contains the objects created from the class PopSongs, while those objects contain data fields such as the title and singer of the song.
