import argparse
import yaml
import json

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

def palindrome():
    """Parser action for checking whether a name is a palindrome"""
    def reversed_name(name):
        return name[::-1]

    def is_palindrome(name):
        return name == reversed_name(name)
        
    class CheckPalindromeAction(argparse.Action):
        def __call__(self, parser, namespace, name, option_string=None):
            if not is_palindrome(name):
                parser.error(f'False. The project name is not a palindrome. {name} reversed is {reversed_name(name)}, they must be equal.')
            else:
                namespace.__setattr__(self.dest, name)
    return CheckPalindromeAction

def yaml_to_json():
    """Parser action for converting, if needed, an YAML file into JSON"""
    class YamlToJsonAction(argparse.Action):
        def __call__(self, parser, namespace, file, option_string=None):
            if not file.name.endswith('.yaml') and not file.name.endswith('.json'):
                parser.error('file must be either YAML or JSON')
            else:
                filename = file.name[:-5]
                try:
                    json.dump(yaml.load(file, Loader=CustomAwsLoader), open(f'{filename}.json','w+'), indent=4)
                except yaml.YAMLError as err:
                    print(f'Error while converting, {err}')

    return YamlToJsonAction