"""Modus part 1 exercise module

Asserts for a palindrome-named project
May receive in the future a Cloud Formation file. If the file is an YAML file, it is converted to JSON.
"""

import argparse
from .parser_actions import palindrome, yaml_to_json

def main():
    parser = argparse.ArgumentParser(description="Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.")
    parser.add_argument('name', metavar='project-name', action=palindrome(), type=str, help='The project name. Must be a palindrome (e.g. tacocat).')
    parser.add_argument('--filename', action=yaml_to_json(), type=argparse.FileType('r'), help='Project\'s Cloud Formation file. YAML files will be converted to JSON.')
    args = parser.parse_args()
    
    print('True. The project name is indeed a palindrome.')
    print("This is our Django project generator tool set.")

if __name__ == '__main__':
    main()