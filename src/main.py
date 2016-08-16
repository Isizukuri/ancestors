from ast import literal_eval


def _tree_to_dict(family_tree_str):
    """Convert family tree string to dictionary."""
    return literal_eval(family_tree_str)


def main(family_tree_str, first_person, second_person):
    family_tree = _tree_to_dict(family_tree_str)
    if first_person is second_person:
        return first_person
    first_person_ancestors = set()
    second_person_ancestors = set()
    for parent, children in family_tree.items():
        if all(person in children for person in(first_person, second_person)):
            print('sisters')
            return parent
            break
        elif first_person in children:
            if second_person == parent:
                print('second is mother')
                return second_person
                break
            else:
                first_person_ancestors.add(parent)
                first_person = parent
        elif second_person in children:
            if first_person == parent:
                print('first is mother')
                return first_person
                break
            else:
                second_person_ancestors.add(parent)
                second_person = parent
        common_ancestor = first_person_ancestors & second_person_ancestors
        if common_ancestor:
            print('common ancestors')
            return common_ancestor
        print('FIN:', 'P-', parent, 'FP-', first_person, 'SP-', second_person,
              'FPA-', first_person_ancestors, 'SPA-', second_person_ancestors)
