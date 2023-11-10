import sys
sys.path.append("DeepINN/geometry/spaces")

from space import Space, R1, R2, R3

space1 = Space({'x': 1})
space2 = Space({'x': 2, 'y': 3})

# Support for multiple spaces has been dropped
# result = space1 * space2
# print(result) 

# #print(space1.__contains__(space2))

# space_obj = Space({'a': 1, 'b': 2, 'c': 3, 'd': 4})
# sub_space = space_obj['a':'c']  # returns a Space with {'a': 1, 'b': 2, 'c': 3}

