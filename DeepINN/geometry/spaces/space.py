from collections import Counter, OrderedDict

"""
* A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
* An OrderedDict is a dictionary subclass that remembers the order in which items are inserted.
"""

class Space(Counter, OrderedDict):
    """
    Base class to define the dimensions of the variables in the differential equation.
    
    Parameters
    ----------
    variables_dims: dict
        A dict containing name of variables and the dimension of each variable.
    """
    def __init__(self, variables_dims):
        # set counter of variable names and their dimensionalities
        # Since the Counter is inherited first, if the super().__init__ is consumed by Counter then the second super class won't receive the call.
        super().__init__(variables_dims)

    # # Adding a magic method to overload the multiply operator using __mul__ 
    # def __mul__(self, additional_space):
    #     """
    #     Combine two spaces to create higher dimension spaces.
    #     E.g R1('x')*R1('y') is a two dimensional space where one axis is 'x'
    #     and the other stands for 'y'.
    #     """
    #     assert isinstance(additional_space, Space), "The additional dimension isn't an instance of Space"
    #     # Since we haven't defined __add__. Python will use Counter's __add__ method
    #     return Space(self + additional_space)
    
    # # __contains__ is a predefined method checks if the key (a string) is present in the counter.
    # # whenever we use `in` keyword with if condition involving instances of Space object, this self.__contains__ will run be override python's default __contains__.
    # # here we override this functionpython's default __contains__
    # # So if we do addition  __add__ we will end up executing self.__contains__
    # def __contains__(self, space):
    #     """
    #     Check if the variables of other space are container in this space.
    #     There are two possibilities. 
    #     * method executed for internal dictionary operations such as addition
    #     * method executed when checking if intersection of space and self is space.
    #     That is why we need to modify python default __contains__ for instances of Space.

    #     ChatGPT's description:
    #     Override the membership test (in) for the Space class.
    #     - If `space` is a string: Checks if the variable name (key) exists in this Space.
    #     This is useful for both direct membership tests and internal operations 
    #     (e.g., during dictionary-style key checking in addition).
        
    #     - If `space` is another Space object: Determines if the provided Space is 
    #     entirely contained within the current Space (i.e., if it's a subset).
    #     """
    #     if isinstance(space,str):
    #         #print("Flag: string")
    #         # check if the space already contains the variable names.
    #         return super().__contains__(space)
    #     if isinstance(space, Space):
    #         #print("Flag: Space")
    #         return (self & space) == space
    #     else:
    #         return False
    
    # # This is a special method in Python which is invoked when we try to access items from containers like array or dictionary.
    # # It's what gets called when you use square bracket notation to access elements, such as with lists, dictionaries, and strings.
    # def __getitem__(self, val):
    #     """
    #     Since __getitem__ is used to retrieve items. There are three ways to retrieve items. str, slice, list or tuple.

    #     1. In the case of a slice.
    #     space_obj = Space({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    #     sub_space = space_obj['a':'c']  # returns a Space with {'a': 1, 'b': 2, 'c': 3}
        
    #     2. In the case of a tuple or a list
    #     space_obj = Space({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    #     sub_space = space_obj[['a', 'c']]  # returns a Space with {'a': 1, 'c': 3}
        
    #     3. In all other cases then use Counter's __getitem__.
    #     space_obj = Space({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    #     value = space_obj['a']  # returns 1

    #     Parameters
    #     ----------
    #     val : str, slice, list or tuple
    #         The keys that correspond to the variables that should be used in the 
    #         subspace.
    #     """
    #     if isinstance(val, slice): # if val is a slice
    #         keys = list(self.keys())
    #         new_slice = slice(keys.index(val.start) if val.start is not None else None,
    #                           keys.index(val.stop) if val.stop is not None else None,
    #                           val.step)
    #         new_keys = keys[new_slice]
    #         return Space({k: self[k] for k in new_keys})
    #     if isinstance(val, list) or isinstance(val, tuple):
    #         return Space({k: self[k] for k in val})
    #     else:
    #         return super().__getitem__(val)
    
    # # To promote encapsulation, @property decorator allows you to print internal read-only attributes of choice.
    # # @property also allows you to call a function without the parentheses. This is useful when these isn't any input attribute.
    # @property
    # def dim(self):
    #     """
    #     Return the dimension of the space.
    #     """
    #     # self is the class Space inheriting Counter, which inherits dict, so values() will return list of values for each key of variables_dims. then sum will sum them up.
    #     return sum(self.values())
    
class R1(Space):
    """
    Space to define 1D domain.
    
    Parameters
    ----------
    variable_name: str
        The name of the variable that belongs to this space.
        It can be any string for coordinate axes.
    """
    def __init__(self, variable_name):
        super().__init__(variable_name, 1)

class R2(Space):
    """
    Space to define 2D domain.
    
    Parameters
    ----------
    variable_name: str
        The name of the variable that belongs to this space.
        It can be any string for coordinate axes.
    """
    def __init__(self, variable_name):
        super().__init__(variable_name, 2)

class R3(Space):
    """
    Space to define 3D domain.
    
    Parameters
    ----------
    variable_name: str
        The name of the variable that belongs to this space.
        It can be any string for coordinate axes.
    """
    def __init__(self, variable_name):
        super().__init__(variable_name, 3)