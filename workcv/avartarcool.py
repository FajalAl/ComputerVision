import numpy as np
import matplotlib.pyplot as plt

x = np.array(   [  [ [0,0,0],[0,150,150], ]        ,
                        [   [255,255,0],[255,255,255],]   ]     )
#x = np.array(   [  [ [0,0,0],[0,150,150], ]        ]     ) #ONE ROW TWO COLUMNS
plt.imshow(x)
plt.show()