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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
