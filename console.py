import cmd
import json

from models import storage
from models.base_model import BaseModel

class_dict = {
    "BaseModel": BaseModel
    # insert other classes here
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """End-of-File (EOF) signal"""
        return True

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
        """Prints the string representation of an instance based on class and ID
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
