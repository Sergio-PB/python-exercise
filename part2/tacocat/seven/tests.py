import unittest
from django.test import Client

from .utils import ERR_BAD_INPUT, int_list_to_str

class IntListTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_modus_example(self):
        int_list = [1,3,2,1,4,5,3,2,6,2,67,21,6,3]
        list_param = int_list_to_str(int_list)
        response = self.client.get(f'/seven/?int_list={list_param}')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'3: 4', response.content)
        self.assertIn(b'2: 5', response.content)
        self.assertIn(b'1: 6', response.content)
    
    def test_negative(self):
        int_list = [100,-93,-0,7,0,1,0,0]
        list_param = int_list_to_str(int_list)
        response = self.client.get(f'/seven/?int_list={list_param}')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'100: -93', response.content)
        self.assertIn(b'0: 7', response.content)

    # --- BAD INPUTS ---
    
    def test_bad_white_spaces(self):
        int_list = [100,-93,-0,7,0,1,0,0]
        list_param = str(int_list)[1:-1].replace(',', '%2C')
        response = self.client.get(f'/seven/?int_list={list_param}')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(ERR_BAD_INPUT.format('').encode(), response.content)

    def test_bad_str(self):
        int_list = [100,'-93',-0,7,0,1,0,0]
        list_param = int_list_to_str(int_list)
        response = self.client.get(f'/seven/?int_list={list_param}')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(ERR_BAD_INPUT.format('').encode(), response.content)

    def test_bad_alpha(self):
        int_list = [100,'-93a',-0,7,0,1,0,0]
        list_param = int_list_to_str(int_list).replace('\'', '')
        response = self.client.get(f'/seven/?int_list={list_param}')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(ERR_BAD_INPUT.format('').encode(), response.content)

    def test_bad_minus(self):
        int_list = [100,'9-3',-0,7,0,1,0,0]
        list_param = int_list_to_str(int_list).replace('\'', '')
        response = self.client.get(f'/seven/?int_list={list_param}')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(ERR_BAD_INPUT.format('').encode(), response.content)