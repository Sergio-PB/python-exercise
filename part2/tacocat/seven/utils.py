ERR_BAD_INPUT = 'The input is in a bad format:{}'
MINUS_INTEGER = '-'
EMPTY_STRING = ''

def is_comma(char):
    return char == ','

def is_minus_symbol(char):
    return char == '-'

def is_empty(string):
    return string == ''

def is_value(string):
    return string != '' and string != '-'

def int_list_to_str(int_list):
    return str(int_list)[1:-1].replace(',', '%2C').replace(' ','')