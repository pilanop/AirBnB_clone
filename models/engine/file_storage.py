#!/usr/bin/python3
"""
Defines the FileStorage class.
"""
import json
import os.path

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "Review": Review,
    "City": City,
    "Place": Place,
    "Amenity": Amenity
    # insert other classes here
}


class FileStorage:
    """
    The FileStorage class manages the storage and retrieval of objects in
    a file.

    Attributes:
        __file_path (str): The file path to store the objects.
        __objects (dict): A dictionary to store the objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all objects in the file storage.

        Returns:
            A dictionary containing all the objects in the file storage.
        """
        return self.__objects

    def new(self, obj):
        """
        Stores the obj in the `__objects` dictionary with a key in the format
        of '<obj class name>.id'

        Args:
            obj (object): The object to be stored in the __objects dictionary.
        """
        key_name = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key_name] = obj

    def save(self):
        """
        Saves the objects in the FileStorage instance to a file.
        """
        with open(self.__file_path, 'w', encoding='utf8') as file:
            new_dict = {key: values.to_dict() for key, values in
                        self.__objects.items()}
            file.write(json.dumps(new_dict))

    def reload(self):
        """
        Reloads the file storage by reading the JSON file and instantiating
        objects.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf8') as file:
                file_data = json.load(file)
                for obj in file_data.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    if cls_name in class_dict:
                        self.new(class_dict[cls_name](**obj))