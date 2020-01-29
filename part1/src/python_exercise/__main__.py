"""Modus part 1 exercise module

A CLI project to create a Django project.
Checks for palindrome-named projects, and asserts for such if the project is to be created.
Outputs the project in a /part2 directory.

May receive a future a Cloud Formation YAML file and converts it to JSON.
The converted output will be {input_file}_cf.json .

May also receive apps names for creating the initial Django app files.

If using a virtual env, the outputs will be outside de virtual env root.
If not using a virtual env, the outputs will be in the current dir.

For further usage information, use help tags -h, --help
"""
import argparse
import subprocess
from pathlib import Path
from .parser_actions import palindrome, yaml_to_json
from .utils import get_work_dir, reversed_name

def main():
    print("\nThis is our Django project generator tool set.\n")

    work_dir = get_work_dir()

    parser = argparse.ArgumentParser(description="Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.")
    
    parser.__setattr__('work_dir', work_dir)
    parser.add_argument('project_name', action=palindrome(), type=str, help='The project\'s name. Must be a palindrome (e.g. tacocat).')
    parser.add_argument('-c', '--check-palindrome', default=False, action='store_true', help='Informs if the project\'s name is a palindrome.')
    parser.add_argument('-f', '--filename', action=yaml_to_json(), type=argparse.FileType('r'), help='Project\'s YAML Cloud Formation file. Converts it to JSON.')
    parser.add_argument('-e', '--execute', default=False, action='store_true', help='With validation, creates a Django project with the given name.')
    parser.add_argument('-a', '--app', nargs='*', help='If a Django project is created, also creates Django apps with the given names. (e.g. --app taco cat -> creates two apps, \'taco\' and \'cat\').')
    args = parser.parse_args()

    project_name = args.project_name
    
    if args.check_palindrome:
        if args.is_palindrome:
            print('True. The project name is indeed a palindrome.\n')
        else:
            print(f'False. The project name is not a palindrome. {project_name} reversed is {reversed_name(project_name)}, they must be equal.\n')

    if args.execute:
        if not args.is_palindrome:
            parser.error(f'The project name must be a palindrome. {project_name} reversed is {reversed_name(project_name)}, they must be equal.')

        print(f'- Creating Django project {project_name}')
        
        project_path = work_dir + f'/part2/{project_name}'

        Path(project_path).mkdir(parents=True, exist_ok=True)
        subprocess.call(['django-admin', 'startproject', project_name, project_path])
        if args.app is not None:
            for app_name in args.app:
                print(f'-- Creating Django app {app_name}')
                app_path = f'{project_path}/{app_name}'
                Path(app_path).mkdir(parents=True, exist_ok=True)
                subprocess.call(['django-admin', 'startapp', app_name, app_path])


if __name__ == '__main__':
    main()