import numpy as np
import matplotlib.pyplot as plt

#x = np.array(       [ [   [0]      ]  ]    ) #ONE ROW ONE COLUMN BLACK
#x = np.array(         [   [0,0,0]      ]      ) ONE ROW TWO COLUMNS BLACK
x = np.array(         [   [[0,0,0]]      ]      )#ONE ROW ONE COLUMN BLACK
#x = np.array(         [   [255]      ]      ) #PURPLE
plt.imshow(x)
plt.show()