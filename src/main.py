"""Olympiad task."""
from ast import literal_eval
import sys


def _tree_to_dict(family_tree_str):
    """Convert family tree string to dictionary."""
    return literal_eval(family_tree_str)


def _get_all_ancestors(family_tree_dict, name):
    """Yield every ancestor of a person from down to up."""
    person_ancestors = {name, }
    have_ancestors = True
    while have_ancestors:
        for parent, children in family_tree_dict.items():
            if name in children:
                person_ancestors.add(parent)
                name = parent
                yield person_ancestors
                break
            else:
                continue
        else:
            yield person_ancestors


def _is_direct_relatives(first_person, second_person,
                         first_person_ancestors, second_person_ancestors):
    """Return ancestor if persons are direct relatives."""
    try:
        if first_person in second_person_ancestors:
            return first_person
        elif second_person in first_person_ancestors:
            return second_person
    except TypeError:
        pass


def _ancestors_check(family_tree_dict, first_person, second_person):
    """Return first common ancestor in family tree."""
    if first_person == second_person:
        return first_person
    first_person_ancestors = _get_all_ancestors(
        family_tree_dict,
        first_person
    )
    second_person_ancestors = _get_all_ancestors(
        family_tree_dict,
        second_person
    )
    ancestors_pairs = zip(
        first_person_ancestors,
        second_person_ancestors,
    )
    for fp_ancestors, sp_ancestors in ancestors_pairs:
        if _is_direct_relatives(first_person, second_person,
                                fp_ancestors, sp_ancestors):
            return _is_direct_relatives(
                first_person, second_person,
                fp_ancestors, sp_ancestors)
        try:
            return (fp_ancestors & sp_ancestors).pop()
        except KeyError:
            pass
        except TypeError:
            root_ancestor = [i for i in (fp_ancestors, sp_ancestors)
                             if isinstance(i, str)].pop()
            return root_ancestor


def main(family_tree_str, first_person, second_person):
    """Convert family tree from string and return the first common ancestor."""
    family_tree = _tree_to_dict(family_tree_str)
    return _ancestors_check(family_tree, first_person, second_person)


if __name__ == '__main__':
    antecedent = main(*sys.argv[1:4])
    print(antecedent)
