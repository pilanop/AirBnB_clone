#!/usr/bin/python3
"""
Defines the BaseModel class.
"""
import datetime
import uuid
import models


class BaseModel:
    """
    The `BaseModel` class is a base class that provides common functionality
    for other classes.

    Methods:
        - `__init__()`: Initializes a new instance of the `BaseModel` class and
                        sets instance variables.
        - `__str__()`: Returns a string representation of the object.
        - `save()`: Saves the object by updating the `updated_at` attribute.
        - `to_dict()`: Converts the object instance to a dictionary
                      representation.
    """

    def __init__(self, *args, **kwargs):
        """
        Args:
            *args: Additional positional arguments.
                This method does not utilize them.
            **kwargs: Additional keyword arguments.
                The class attributes are set based on these arguments.
        """
        if kwargs:
            new_kwargs = kwargs.copy()
            if "__class__" in new_kwargs:
                new_kwargs.pop("__class__")

            iso_format = "%Y-%m-%dT%H:%M:%S.%f"

            new_kwargs["updated_at"] = datetime.datetime.strptime(
                new_kwargs["updated_at"],
                iso_format)
            new_kwargs["created_at"] = datetime.datetime.strptime(
                new_kwargs["created_at"],
                iso_format)
            for key, value in new_kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Parameters:
            self: The object instance.

        Returns:
            str: The string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the object.

        assigns the current timestamp to the `updated_at` attribute.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()
        models.storage.new(self)

    def to_dict(self):
        """
        Converts the object instance to a dictionary representation.

        Returns:
            dict: The dictionary representation of the object instance,
                including the class name, updated_at datetime value in ISO
                format, and created_at datetime value in ISO format.

        Raises:
            None
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        return new_dict
