from functools import partial
import unittest

from main import main, _tree_to_dict, _get_all_ancestors


class TestAncestor(unittest.TestCase):
    """Test suite for ancestor module."""
    def setUp(self):
        self.family_tree_str = '{"Ann": ["Betty", "Clare"], "Betty": ["Donna", \
            "Elizabeth", "Flora"], "Clare": ["Gloria", "Hazel"], \
            "Bekka": ["Ann"], "Carla": ["Bekka"]}'
        self.family_tree_dict = {
            "Carla": ["Bekka", ],
            "Bekka": ["Ann", ],
            "Ann": ["Betty", "Clare"],
            "Betty": ["Donna", "Elizabeth", "Flora"],
            "Clare": ["Gloria", "Hazel"],
        }
        self.get_all_ancestors_func = partial(
            _get_all_ancestors,
            self.family_tree_dict,
        )
        self.main_func = partial(main, self.family_tree_str)

    def test__tree_to_dict(self):
        converted_family_tree = _tree_to_dict(self.family_tree_str)
        self.assertDictEqual(converted_family_tree, self.family_tree_dict)
        self.assertRaises(ValueError, _tree_to_dict, {'family_tree_str': 1})
        self.assertRaises(ValueError, _tree_to_dict, {'family_tree_str': None})

    def test_same_person(self):
        self.assertEqual(self.main_func('Hazel', 'Hazel'), 'Hazel')

    def test_sisters(self):
        self.assertEqual(self.main_func('Hazel', 'Gloria'), 'Clare')

    def test_mother(self):
        self.assertEqual(self.main_func('Clare', 'Hazel'), 'Clare')

    def test_strict_ancestor(self):
        self.assertEqual(self.main_func('Bekka', 'Hazel'), 'Bekka')


if __name__ == '__main__':
    unittest.main()
