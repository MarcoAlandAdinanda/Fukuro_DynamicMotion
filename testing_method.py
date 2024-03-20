# import numpy as np

# test = np.array([[ 542.22537442, 758.99494949, 768.81522181, 1356.39208012, 1428.59805267, 1730.73726387, 1947.25972187, 1975        ],
#                  [ 460.03701037,  544.54040404,  530.57669457,  579.81497878,  353.36620101, 333.67120058,  682.24322938,  500       ]])

# for x, y in zip(test[0], test[1]):
#     print(x)
#     print(y)
    
mario_dict = {}
for information in ["name", "age", "auto"]:      #(1)
    mario_dict[information] = eval(information)  #(2)print (mario_dict)