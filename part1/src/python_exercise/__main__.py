"""Modus part 1 exercise module

A CLI project to create a Django project.
Asserts for only palindrome-named project
May receive in the future a Cloud Formation file. If the file is an YAML file, it is converted to JSON.

For usage information, use help tags -h, --help
"""
import argparse
import subprocess
from pathlib import Path
from .parser_actions import palindrome, yaml_to_json

def main():
    parser = argparse.ArgumentParser(description="Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.")
    parser.add_argument('name', metavar='project_name', action=palindrome(), type=str, help='The project name. Must be a palindrome (e.g. tacocat).')
    parser.add_argument('-f', '--filename', action=yaml_to_json(), type=argparse.FileType('r'), help='Project\'s Cloud Formation file. YAML files will be converted to JSON.')
    parser.add_argument('-e', '--execute', default=False, action='store_true', help='With validation, creates a Django project with the given name.')
    args = parser.parse_args()
    
    print('True. The project name is indeed a palindrome.')
    print("This is our Django project generator tool set.")

    if args.execute:
        print('Building a Django project')
        project_path = f'../part2/{args.name}'
        Path(project_path).mkdir(parents=True, exist_ok=True)
        subprocess.call(['django-admin', 'startproject', args.name, project_path])

if __name__ == '__main__':
    main()