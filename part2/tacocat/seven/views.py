from django.shortcuts import render

from .forms import IntListForm
from .utils import ERR_BAD_INPUT, EMPTY_STRING, MINUS_INTEGER, is_comma, is_empty, is_minus_symbol, is_value

def find_sum_pairs(string_list, target_sum):
    """Returns a dict of unique pairs within a list of integers that add up to a given value.

    The integer list must be passed as a string, containing only: digits, minus symbols (-), commas.
    E.g. 1,3,2,-1,4,5,3,2,6,2,67,-21,6,3
    If the list if passed in a wrong format raises an error

    Parameters
    ----------
    string_list : str
        The integer list as csv
    target_sum : int
        The sum value the pairs should add up to
    
    Raises
    ------
    ValueError
        If the list contains illegal characters or if the characters are in an order that can not be parsed as ant integer list
    """
    found_pairs = {}
    if string_list is not EMPTY_STRING:
        possible_pairs = {}
        current_value = EMPTY_STRING

        # trailing comma to parse the last integer
        for char in string_list + ',':
            if char.isdigit():
                current_value += char
            elif is_minus_symbol(char):
                if is_empty(current_value):
                    current_value = MINUS_INTEGER
                else:
                    raise ValueError('misplaced minus symbol')
            elif is_comma(char):
                if not is_value(current_value):
                    raise ValueError('misplaced comma')

                integer = int(current_value)
                pair = target_sum - integer
                
                if integer in found_pairs or pair in found_pairs:
                    pass
                elif pair in possible_pairs and possible_pairs[pair] is None:
                    possible_pairs[pair] = integer
                    found_pairs[pair] = integer
                elif integer not in possible_pairs:
                    possible_pairs[integer] = None
                
                current_value = EMPTY_STRING
            else:
                raise ValueError(f'illegal character \'{char}\'')
            
    return found_pairs


def get_form(request):
    TARGET_SUM = 7

    int_list = request.GET.get('int_list', '')
    return_data = {
        'form' : IntListForm(data={'int_list' : int_list}),
        'result' : {}
        }
    
    try:
        return_data['result'] = find_sum_pairs(int_list, TARGET_SUM)
    except ValueError as err:
        return_data['result'] = ERR_BAD_INPUT.format(err)
    
    return render(request, 'form.html', return_data)