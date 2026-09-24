# Advanced Class Relationships
## Name : Christine Joyce S. Astillero
## Section : 9 - Magnesium
## Date : 09/24/2026
## School Year : 2026-2027

## Previous Activities
[classAttrib](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/classAttributesMethods.md)
[classRel](classRelationships.md)

## Existing System Description:
The classes that already exist in my system are Song_Compiler and Pop_Songs. The limitation that i can think of is unclear ownership. Once i analyzed the classes i realized that it is suitable for association but not inheritance. Since i used a list, i couldn't find a concrete attribute that a child class can inheret, i also found it hard to determine a parent class that could have an attribute that is suitable for inheritance. I also realized that the attributes are not suitable for Aggregation or rather there is no class where you can create an object and utilize that object to store in another.

## Inheritance Relationship
Parent: Singer
Child: Pop_Songs
Explanation: The Singer is a parent class because it is a generalized term, and the attribute that the child class will inheret is the attribute called singer. The extra attributes of the child will be based on the inherited trait such as the collaborator and the title of the song made by the chosen singer.

## Inheritance UML
![Inheritance](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/inheritanceDiagram.jpg)

## Composition/Aggregation
Relationship: Aggregation (weak HAS-A relationship)
Explanation: I chose Aggregation because an object can be created from the class called Singer, and that object can be stored in a variable inside another specific object. However, once that specific object is removed, the Singer object will remain unaffected and its values will still be intact. Thus, showing Aggregation.

Class containing another object: Pop_Songs
Contained object: Singer
Why? Since the object singer can be stored inside an object from Pop_Songs. Even though Singer is the parent class, it can still act as the contained object because it will already be created before it is cotained and it won't be unaffected or also removed once the object that is containing is deleted.

## Advanced UML Diagram
![Advanced UML](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/advancedClassDiagram.jpg)

## Python Implementation
[Source Code](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/advancedRelationships.py)

## Test Run
![Test](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/advancedTestRun1.png)
![Test](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/advancedTestRun2.png)

## Object Diagram
![Objects](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/advancedObjectDiagram1.jpg)
![Objects](https://github.com/cjsastillero-hub/9magnesiumcs3/blob/main/q1/images/advancedObjectDiagram2.jpg)

## Reflection
Answer in 3–5 sentences each.
1.Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.
The child class is a type of my parent class because the child class has an inherited attribute from the parent class. The child class is also based off of the parent class, which means that the extra data fields of the sub class depends on the inherited attribute it contains which also acts as the base.

2.How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
It reduced duplicated code by preventing the same use attribute from being typed or recreated into various classes. It instead created a parent class that holds a very commonly used attribute that other sub classes can inherit and reuse rather than create again. The attribute that was reused was the singer attribute, it made things simpler and made the code shorter.

3.Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.
I chose Aggregation because i believe it is more convenient. Because instead of creating an object made inside of an object, i instead used an already existing one. It is more convenient because multiple other new objects can still utilize the previous object, it is not like Composition that once you remove the object containing another, the contained object will also be removed. I think it also prevents code from repeating, since you can just use the already existing object to create multiple other ones instead of recreating it everytime you make an object.

4.What is the difference between Association from Part III and the advanced relationship you
implemented?
The difference between Association and the advanced relationship i implemented is that inheritance implies that one class is a subclass of another, while Association implies that objects simply interact or use the values of different objects. Inheritance has a IS-A relationship while Association has more of a USES-A or HAS-A relationship. This means that inheritance has a child class that acts as the sub type of a parent class, which shows actions such as inheriting the data fields of the parent class. Meanwhile, Association is just the interaction between two objects, sharing and utilizing each others values.

5.How does your design follow the DRY principle? 
It follows the DRY principle because instead of the child classese repeating the same attributes in their data fields, it instead inherets the attribute of a parent class. It makes it versatile and prevents the code from always repeating. It also follows the DRY principle because instead of inputting the same repeating value onto different objects, it can instead be taken from a seperate already existing object which is also convenient and simplifies the code.
