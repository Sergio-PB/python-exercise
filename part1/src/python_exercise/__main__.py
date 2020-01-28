"""Modus part 1 exercise module

Asserts for a palindrome-named project
"""

import argparse

def reversed_name(name):
    return name[::-1]

def is_palindrome(name):
    return name == reversed_name(name)

def main():
    parser = argparse.ArgumentParser(description="Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.")
    parser.add_argument('name', metavar='project-name', type=str, help='The project name. Must be a palindrome (e.g. tacocat).')
    
    args = parser.parse_args()
    assert is_palindrome(args.name), f'False. The project name is not a palindrome. {args.name} reversed is {reversed_name(args.name)}, they must be equal.'

    print('True. The project name is indeed a palindrome.')
    print("This is our Django project generator tool set.")

if __name__ == '__main__':
    main()