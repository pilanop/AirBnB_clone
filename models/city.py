#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.

    Attributes:
        name (str): The name of the city.
        state_id (str): The state ID of the city.
    """
    name = ""
    state_id = ""
