# Class Attributes and Methods

## Name: Christine Joyce S. Astillero
## Section: 9 - Magnesium
## Date: 09/12/2026
## School Year: 2026-2027

## Previous Design
Link to my previous activity:
[classObjectUML.md](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/classObjectUML.md)

## Design Revision
Changes from my previous design:
-instead of play(), it will become ChangeSinger(ChangeSingerOfSong:string)
-this method will change the original value of singer
-instead of stop(), it will become ReturnTitle()
-this method will return or display the title of the song of a chosen object

## Visibility Decisions
| Attribute     | Data Type | Visibility | Reason                                                                            |
|---------------|-----------|------------|-----------------------------------------------------------------------------------|
|title          |string     |public      |so that the user can know what song they are working with                          |
|release year   |integer    |private     |it is not relevant, and does not affect the quality of the class if it is private  |
|length of song |integer    |private     |it is not relevant, and most users don't pay attention to the length of the songs  |
|singer         |string     |public      |it gives the user proper context on who sang the song, as it could be a song cover |

## Updated UML Class Diagram
![Class Diagram](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/classDiagramSG5.jpg)

## Python Implementation
[View Python Source](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/classImplementation.py)

## Test Run
![Test Run](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/classTestRun.png)

## Object Diagram
![Object Diagram](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/objectDiagram.jpg)

## Analysis
### Why did you make your chosen attribute private?
Because in my opinion, it does not hold that much influence over the overall class, and users don't pay attention to it regardless if it is public or not.
### Which method changes the state of your object?
The method that changes the state of my object is ChangeSinger() as it changes the original assigned singer of the song.
### How did your two objects demonstrate that instances are independent?
By declaring a method that changes the singer of an object, however it is only applied to one object. So when we display the before and after attributes of the two objects, it will show that only one actually changed. Thus demonstrating that instances are independent.
### What is the difference between your class diagram and your object diagram?  
The class diagram shows the blue print or template without assigning values to the attributes, while my object diagram has assigned specific values that belong to that object alone.

