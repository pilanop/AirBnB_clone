#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the FileStorage class."""

    def test_no_args(self):
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_objects_is_private_dict(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)


class TestFileStorageMethods(unittest.TestCase):
    """Unit tests for testing methods of the FileStorage class."""

    def setUp(self):
        self.file_storage = FileStorage()
        self.base_model_instance = BaseModel()
        self.user_instance = User()
        self.state_instance = State()
        self.place_instance = Place()
        self.city_instance = City()
        self.amenity_instance = Amenity()
        self.review_instance = Review()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_new(self):
        self.file_storage.new(self.base_model_instance)
        self.assertIn("BaseModel." + self.base_model_instance.id, self.file_storage.all().keys())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            self.file_storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            self.file_storage.new(None)

    def test_save(self):
        self.file_storage.new(self.base_model_instance)
        self.file_storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + self.base_model_instance.id, save_text)

    def test_reload(self):
        self.file_storage.new(self.base_model_instance)
        self.file_storage.save()
        self.file_storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + self.base_model_instance.id, objects.keys())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            self.file_storage.reload(None)


if __name__ == "__main__":
    unittest.main()