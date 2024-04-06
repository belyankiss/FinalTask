import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
human = [1 if i == 'human' else 0 for i in lst]
robot = [1 if i == 'robot' else 0 for i in lst]
new_data = pd.DataFrame({'human': human, 'robot': robot})
print(new_data)