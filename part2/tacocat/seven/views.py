from django.shortcuts import render

from .forms import IntListForm
from .utils import BAD_INPUT, EMPTY_STRING, MINUS_INTEGER, is_comma, is_empty, is_minus, is_value

def get_form(request):
    int_list = request.GET.get('int_list', '')
    return_data = {}
    if int_list is not EMPTY_STRING:
        possible_pairs = {}
        found_pairs = {}
        current_value = EMPTY_STRING

        for char in int_list + ',':
            if char.isdigit():
                current_value += char
            elif is_minus(char):
                if is_empty(current_value):
                    current_value = MINUS_INTEGER
                else:
                    found_pairs = BAD_INPUT
                    break
            elif is_comma(char) and is_value(current_value):
                integer = int(current_value)
                pair = 7 - integer
                if integer in found_pairs or pair in found_pairs:
                    pass
                elif pair in possible_pairs and possible_pairs[pair] is None:
                    possible_pairs[pair] = integer
                    found_pairs[pair] = integer
                elif integer not in possible_pairs:
                    possible_pairs[integer] = None
                current_value = EMPTY_STRING
            else:
                found_pairs = BAD_INPUT
                break
            
        return_data['result'] = found_pairs
    
    return_data['form'] = IntListForm(data={'int_list' : int_list})
    return render(request, 'form.html', return_data)