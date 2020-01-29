import argparse
import yaml
import json
from .utils import reversed_name

def palindrome():
    """Parser action for checking whether a name is a palindrome"""

    def is_palindrome(name):
        return name == reversed_name(name)
        
    class CheckPalindromeAction(argparse.Action):
        def __call__(self, parser, namespace, name, option_string=None):
            namespace.__setattr__(self.dest, name)
            namespace.__setattr__('is_palindrome', is_palindrome(name))

    return CheckPalindromeAction

FINDINMAP_TAG = '!FindInMap'
FINDINMAP_KEY = 'Fn::FindInMap'
REF_TAG = '!Ref'
REF_KEY = 'Ref'
DEFAULT_INT_TAG = 'tag:yaml.org,2002:int'

def findinmap_constructor(loader, node):
    return { FINDINMAP_KEY : loader.construct_sequence(node) }

def ref_constructor(loader, node):
    return { REF_KEY : loader.construct_scalar(node) }

def int_overload(loader, node):
    '''Converts int scalar node to str'''
    return loader.construct_scalar(node)

class CustomAwsLoader(yaml.Loader):
    pass

CustomAwsLoader.add_constructor(FINDINMAP_TAG, findinmap_constructor)
CustomAwsLoader.add_constructor(REF_TAG, ref_constructor)
CustomAwsLoader.add_constructor(DEFAULT_INT_TAG, int_overload)

def yaml_to_json():
    """Parser action for converting an YAML file into JSON"""
    class YamlToJsonAction(argparse.Action):
        def __call__(self, parser, namespace, in_file, option_string=None):
            if not in_file.name.endswith('.yaml'):
                parser.error('file input must be YAML')
            else:
                work_dir = parser.work_dir
                try:
                    out_file = f'{work_dir}/{namespace.project_name}_cf.json'
                    json.dump(yaml.load(in_file, Loader=CustomAwsLoader), open(out_file,'w+'), indent=4)
                    print(f'Successfully generated\n{out_file}\n')
                except yaml.YAMLError as err:
                    parser.error(f'Error while converting, {err}')

    return YamlToJsonAction