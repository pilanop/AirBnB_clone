#!/usr/bin/python3
"""command line interpreter for HBNB."""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program (Ctrl+D or Ctrl+Z)."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line (pressing ENTER)."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
