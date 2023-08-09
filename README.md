# AirBnB clone - The console
![alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230809T080643Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ae0a0c8d25decc3028d2f3f37cc14721747036ffd7b90c718d8cb7ff178d899c)

## Welcome to the AirBnB clone project!
Before starting, please read the **AirBnB** concept page. 

### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the **AirBnB clone**. 

This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine


### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object


## More Info
### Execution
Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

![alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230809T080643Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=023022f10fe6c7b8da4196f533a88c1aa1189f98062b2a8ebe1c6c3dd85f55ce)

## Files and Directories

```bash

AirBnB_clone/
├── models/
│   ├── engine/
│   │   ├── __init__.py
│   │   └── file_storage.py
│   ├── __init__.py
│   └── base_model.py
├── tests/
│   ├── test_engine/
│   │   ├── __init__.py
│   │   └── test_file_storage.py
│   └── test_models/
│       ├── __init__.py
│       └── test_base_model.py
├── .gitignore
├── AUTHORS
├── console.py
└── README.md

```

#### Authors

- Khalid Mohammed
  GitHub: [https://github.com/pilanop](https://github.com/pilanop)

- Paulos Lendado
  GitHub: [https://github.com/Pauloslemma](https://github.com/Pauloslemma)
