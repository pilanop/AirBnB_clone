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

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End-of-File (EOF) signal """
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
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) == 1 and arg_list[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(arg_list) == 1 and arg_list[0] in class_dict:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            found = False
            with open("file.json", 'r', encoding="utf8") as file:
                file_data = json.load(file)
                for val in file_data.values():
                    if (arg_list[1] == val["id"] and
                            arg_list[0] == val["__class__"]):
                        new_instance = class_dict[arg_list[0]](**val)
                        print(new_instance)
                        found = True
                        break
            if not found:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
