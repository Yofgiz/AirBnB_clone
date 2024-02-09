#!usr/bin/python3
"""Defining the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defining the attributes for other classes."""
    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class.
        """
        # public instance attributes
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs):
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    # public instance methods
    def save(self):
        """Updates the public instance attribute."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary"""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__

        return (dict_copy)

    def __str__(self):
        """Return the string representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
