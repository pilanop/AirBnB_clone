import cmd
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
