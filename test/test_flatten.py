import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):
    def test_2level_null(self):
        d = {
            "a": 1,
            "b": True,
            "x": None,
            "c": {
                "d": 3,
                "e": "test",
                "y": None
            }
        }
        self.assertEqual(flatten(d), {'a': 1, 'b': True, 'x': None, 'c.d': 3, 'c.e': 'test', 'c.y': None})

    def test_empty(self):
        self.assertEqual(flatten({}), {})

    def test_3level(self):
        d = {
            "a.t": 1,
            "b": True,
            "c": {
                "d": 3,
                "e": {
                    "f": "ab c  d",
                    "g": 42.24
                }
            }
        }
        self.assertEqual(flatten(d), {'a.t': 1, 'b': True, 'c.d': 3, 'c.e.f': 'ab c  d', 'c.e.g': 42.24})


    def test_nested_empty_dict(self):
        d = {
            "a": 1,
            "b": {},
            "date of": {
                "d": {},
                "birth": 7
            }
        }
        self.assertEqual(flatten(d), {'a': 1, 'b': None, 'date of.d': None, "date of.birth": 7})

    def test_null_key(self):
        d = {'a': 123, 'b': {None: 789}}
        with self.assertRaises(TypeError) as exc:
            flatten(d)