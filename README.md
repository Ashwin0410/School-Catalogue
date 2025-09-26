# School Catalogue

A Python project that models a digital school catalog for the  
New York City Department of Education using **object-oriented programming**.

## Features
- **School (Parent Class)**  
  - Properties: `name`, `level` (`primary`, `middle`, or `high`), `numberOfStudents`  
  - Getters for all properties  
  - Setter for `numberOfStudents`  
  - `__repr__` method to display school details
- **Primary (Child Class)**  
  - Adds `pickupPolicy` property
- **Middle (Child Class)**  
  - No additional properties
- **High (Child Class)**  
  - Adds `sportsTeams` property (list of strings)

## How to Run
```bash
python school_catalogue.py
