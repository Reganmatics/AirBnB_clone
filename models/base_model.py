#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines common attributes or methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes a new Basemodel.

        Args:
            *args (any): Not used.
            **kwargs (dict): key/value pairs of attributes.
    """
        t_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

     def __str__(self):
        """Returns the str representation of the Basemodel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance.
        Includes the key/value pair __class__ representing the class name of the object.
        """
        cl_dict = self.__dict__.copy()
        cl_dict["created_at"] = self.created_at.isoformat()
        cl_dict["updated_at"] = self.updated_at.isoformat()
        cl_dict["__class__"] = self.__class__.__name__
        return cl_dict
