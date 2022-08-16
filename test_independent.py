# import torch
# a = torch
# if 'api' in torch.__dict__.keys():
#     print('true')
# else:
#     print('false')

# print(a.__dict__.keys())

# import sys
# thismod = sys.modules[__name__]
# print(thismod)

import deepxde as dde
print(dde.backend.__dict__.keys())
#print(dde.)