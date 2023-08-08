#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class FileStorageTestCase(unittest.TestCase):
    """Tests the FileStorage class"""

    def setUp(self):
        """
        Sets up the tests
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Deletes the test json file
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Tests the `all` method
        """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """
        Tests the `new` method
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        key = f"BaseModel.{my_model.id}"
        all_objects = self.storage.all()
        self.assertIn(key, all_objects.keys())

    def test_save_reload(self):
        """
        Tests the `save` and `reload` methods
        """
        my_model = BaseModel()
        my_model.name = "My_Second_Model"
        my_model.my_number = 45
        my_model.save()

        key = f"BaseModel.{my_model.id}"
        all_objects1 = self.storage.all()
        self.assertIn(key, all_objects1.keys())

        storage2 = FileStorage()
        storage2.reload()

        all_objects2 = storage2.all()
        self.assertIn(key, all_objects2.keys())

        self.assertEqual(len(all_objects1), len(all_objects2))

        self.assertEqual(my_model.name, all_objects2[key].name)
        self.assertEqual(my_model.my_number, all_objects2[key].my_number)


if __name__ == '__main__':
    unittest.main()
