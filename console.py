import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End-of-File (EOF) signal"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
