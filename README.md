# Dino
Node library for Dynamo visual programming.

---
## Objective
To simplify common workflow in Dynamo namely
* Retrieving the elements
* Sorting the elements
* Filtering the elements
* Generating data

---
## Installation
Folder Structure
```
C:\ProgramData\Dynamo\Dynamo Revit\1.3\definitions\
    | dino
    |--- dino_core
    |--- dino_nodes
```

---
## Modules
1. Dino.Data Module

    Contains node that are related to generating and manipulating data.

    * Dino.COBie Module

        Contains node related to COBie data.

2. Dino.Elements Module

    Contains nodes related to elements.

    * Dino.Elements.Filter Module

        Contains nodes for filtering elements.
        
    * Dino.Elements.Sort Module
       
        Contains nodes for sorting elements.

    * Dino.Elements.Wall Module
       
        Contains nodes for collecting wall types.
---
## Limitations
* Tested only for Revit 2019 with Dynamo 1.3 version.
