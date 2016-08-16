from functools import partial
import unittest

from main import main, _tree_to_dict


class TestAncestor(unittest.TestCase):
    """Test suite for ancestor module."""
    def setUp(self):
        self.family_tree_str = '{"Ann": ["Betty", "Clare"], "Betty": ["Donna", \
            "Elizabeth", "Flora"], "Clare": ["Gloria", "Hazel"], \
            "Bekka": ["Ann"]}'
        self.main_func = partial(main, self.family_tree_str)

    def test_family_tree_to_str(self):
        family_tree_dict = {
            "Ann": ["Betty", "Clare"],
            "Betty": ["Donna", "Elizabeth", "Flora"],
            "Clare": ["Gloria", "Hazel"],
            "Bekka": ["Ann"],
        }
        converted_family_tree = _tree_to_dict(self.family_tree_str)
        self.assertIsInstance(converted_family_tree, dict)
        self.assertDictEqual(converted_family_tree, family_tree_dict)
        self.assertRaises(ValueError, _tree_to_dict, {'family_tree_str': 1})
        self.assertRaises(ValueError, _tree_to_dict, {'family_tree_str': None})

    def test_same_person(self):
        print('spt')
        self.assertEqual(self.main_func('Hazel', 'Hazel'), 'Hazel')

    def test_sisters(self):
        print('st')
        self.assertEqual(self.main_func('Hazel', 'Gloria'), 'Clare')

    def test_mother(self):
        print('mt')
        self.assertEqual(self.main_func('Clare', 'Hazel'), 'Clare')

    def test_strict_ancestor(self):
        print('sat')
        self.assertEqual(self.main_func('Ann', 'Hazel'), 'Ann')


if __name__ == '__main__':
    unittest.main()
