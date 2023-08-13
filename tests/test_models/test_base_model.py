#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel

    This is a unit test class for the BaseModel class.

    """

    def setUp(self):
        """
        Set up method for the TestBaseModel class.

        This method initializes an instance of the BaseModel class and assigns
        it to the `base_model` attribute of the TestBaseModel instance.
        """
        self.base_model = BaseModel()

    def test_BaseModel(self):
        """
        Test case to verify the behavior of the BaseModel class.
        """
        self.assertEqual(type(self.base_model.id), str)
        self.assertEqual(type(self.base_model.created_at), datetime.datetime)
        self.assertEqual(type(self.base_model.updated_at), datetime.datetime)

    def test_str(self):
        """
        Test case for test_str method in BaseModel class
        """
        string_repr = self.base_model.__str__()
        self.assertEqual(type(string_repr), str)
        self.assertIn(self.base_model.id, string_repr)

    def test_save(self):
        """
        Test the save method of the BaseModel class.
        """
        updated_time_before_save = self.base_model.updated_at
        self.base_model.save()
        updated_time_after_save = self.base_model.updated_at
        self.assertNotEqual(updated_time_before_save, updated_time_after_save)

    def test_to_dict(self):
        """
        This method tests if the to_dict method of the BaseModel class
        returns the expected dictionary representation of the object.
        """
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(type(base_model_dict), dict)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertEqual(base_model_dict["id"], self.base_model.id)
        self.assertEqual(base_model_dict["created_at"],
                         self.base_model.created_at)
        self.assertEqual(base_model_dict["updated_at"],
                         self.base_model.updated_at)


class Test_Base_Model_From_Dict(unittest.TestCase):
    """
    Test_Base_Model_From_Dict

    This is a unit test class for the BaseModel class when it is being
    instantiated from a dictionary.
    """

    def setUp(self):
        """
        This method initializes a BaseModel instance and a dictionary
        representation of it. Then it creates a new BaseModel instance
        from this dictionary.
        """
        self.my_model = BaseModel()
        self.my_model_dict = self.my_model.to_dict()
        self.base_model_from_dict = BaseModel(**self.my_model_dict)

    def test_Base_Model_From_Dict(self):
        """This method tests the BaseModel instance created from a
        dictionary."""
        self.assertEqual(self.base_model_from_dict.id,
                         self.my_model_dict["id"])
        self.assertEqual(type(self.base_model_from_dict.created_at),
                         datetime.datetime)
        self.assertEqual(type(self.base_model_from_dict.updated_at),
                         datetime.datetime)

    def test_str(self):
        """This method tests string representation of the BaseModel."""
        string_repr = self.base_model_from_dict.__str__()
        self.assertIn(self.base_model_from_dict.id, string_repr)

    def test_save(self):
        """This method tests the 'save' method of the BaseModel instance."""
        updated_time_before_save = self.base_model_from_dict.updated_at
        self.base_model_from_dict.save()
        updated_time_after_save = self.base_model_from_dict.updated_at
        self.assertNotEqual(updated_time_before_save, updated_time_after_save)

    def test_to_dict(self):
        """This method tests 'to_dict' method of the BaseModel instance."""
        base_model_dict = self.base_model_from_dict.to_dict()
        self.assertEqual(type(base_model_dict), dict)
        self.assertEqual(base_model_dict["__class__"],
                         self.my_model_dict["__class__"])
        self.assertEqual(base_model_dict["id"],
                         self.my_model_dict["id"])
        self.assertEqual(base_model_dict["created_at"],
                         self.my_model_dict["created_at"])
        self.assertEqual(base_model_dict["updated_at"],
                         self.my_model_dict["updated_at"])


if __name__ == '__main__':
    unittest.main()
