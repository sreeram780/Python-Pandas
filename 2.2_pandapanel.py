# pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
# Parameter	Description
# data	Data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame
# items	axis=0
# major_axis	axis=1
# minor_axis	axis=2
# dtype	Data type of each column
# copy	Copy data. Default, false

# From 3D ndarray
# creating an empty panel
import pandas as pd
import numpy as np
data = np.random.rand(2,4,5)
p = pd.core.panel(data)
print(p)


# From dict of DataFrame Objects
#creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)

#creating an empty panel
import pandas as pd
p = pd.Panel()
print(p)

# Selecting the Data from Panel using Items
# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p['Item1'])

# Selecting the Data from Panel using major_axis
# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p.major_xs(1))