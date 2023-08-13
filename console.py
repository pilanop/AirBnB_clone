#!/usr/bin/python3
"""command line interpreter for HBNB."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
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


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End-of-File (EOF) signal """
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of a given class"""
        if not arg:
            print("** class name missing **")
        elif arg not in class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = class_dict[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        """
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) == 1 and arg_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1 and arg_list[0] in class_dict:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            found = False
            all_objects = storage.all()
            for obj in all_objects.values():
                if (arg_list[1] == obj.id and
                        arg_list[0] == obj.__class__.__name__):
                    print(obj)
                    found = True
                    break
            if not found:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) == 1 and arg_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1 and arg_list[0] in class_dict:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            all_objects = storage.all()
            try:
                all_objects.pop(f"{arg_list[0]}.{arg_list[1]}")
            except KeyError:
                print("** no instance found **")
            for obj in all_objects.values():
                storage.new(obj)
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        arg_list = arg.split()

        if len(arg_list) == 1 and arg_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 0:
            all_objects = storage.all()
            for obj in all_objects.values():
                print(obj)

        elif len(arg_list) == 1:
            all_objects = storage.all()
            for obj in all_objects.values():
                if arg_list[0] == obj.__class__.__name__:
                    print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and ID"""
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) == 1 and arg_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1 and arg_list[0] in class_dict:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        elif len(arg_list) == 4:
            found = False
            all_objects = storage.all()
            for obj in all_objects.values():
                if (arg_list[1] == obj.id and
                        arg_list[0] == obj.__class__.__name__):
                    dict_obj = obj.to_dict()
                    dict_obj[arg_list[2]] = arg_list[3][1:-1]
                    update_instance = class_dict[arg_list[0]](**dict_obj)
                    update_instance.save()
                    found = True
            if not found:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
