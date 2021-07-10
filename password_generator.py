#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

"""
Password Generator - A program that generates weak and strong passwords
Copyright (C) 2020 Compass 
Websites:
    https://8kun.top/slackware/
    https://github.com/compassnet
IRC Channels:
    #slackware@irc.rizon.net
    ##python@irc.rizon.net
    ##linux@irc.rizon.net

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""

# Import the necessary python modules.
import unittest
import random
import secrets
import string

def instructions():
    """Instructions of the password generator program."""
    # Print the program instructions.
    instructions = (
            "\nWelcome to the Password Generator!"
            "\n1. You can choose a weak or strong password."
            "\n2. You can choose the password length."
            "\n3. Whitespaces and newlines will be removed."
            )
    print(instructions)

def strength():
    """Ask the user for the password strength:
    'w' for a weak password;
    's' for a strong password;
    'q' to quit.
    """
    # Print the instructions for the password strength.
    message = (
            "\nPlease choose the password strength:"
            "\n'w' for a weak password (random module);"
            "\n's' for a strong password (secrets module);"
            "\n'q' to quit the program: "
            )
    # while loop asking the user for the password strength.
    while True:
        ask = input(message)
        if ask == 'q':
            print("Quitting the Password Generator...")
            exit()
        elif ask == 'w':
                print("Weak password generation selected")
                generate_weak()
        elif ask == 's':
                print("Strong password generation selected")
                generate_strong()

def length():
    """Ask the user for the password length."""
    # Print the instructions for the password length.
    message = (
            "\nPlease type the password length."
            "\nThere is no length limit, but longer passwords"
            "\nwill take more time to generate (you might have"
            "\nto force quit the program (ctrl + c)."
            "\n'0' to quit the program: "
            )
    # while loop asking the user for a valid password length.
    while True:
            try:
                number = int(input(message))
            except ValueError:
                print("An integer number is required!")
                continue
            else:
                if number == '0':
                    print("Quitting the Password Generator...")
                    exit()
                else:
                    return number
                    exit()

def generate_weak():
    """Generate a weak password."""
    # Read about the join() method and translate() function to do this.
    passwd = ''.join(random.choice(string.printable) for i in range(length()))
    # Did a copy/paste this time in regards to translate().
    # translate() removes whitespaces and newlines.
    passwd_ = passwd.translate({ord(c): None for c in string.whitespace})
    print(f"Weak Password:\n{passwd_}")

def generate_strong():
    """Generate a strong password."""
    # Read about the join() method and translate() function to do this.
    passwd = ''.join(secrets.choice(string.printable) for i in range(length()))
    # Did a copy/paste this time in regards to translate().
    # translate() removes whitespaces and newlines.
    passwd_ = passwd.translate({ord(c): None for c in string.whitespace})
    print(f"Strong Password:\n{passwd_}")

instructions()
strength()

if __name__ == '__main__':
    unittest.main()
