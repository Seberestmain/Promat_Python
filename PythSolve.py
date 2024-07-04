import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data) # печатаем до

#==================================================#
print('После скрипта')
 
data['tmp'] = 1  # Временный столбик для значений
data.set_index([data.index, 'whoAmI'], inplace=True)  #Устанавливается новый индекс DataFrame, состоящий из текущего индекса и значений столбца whoAmI
data = data.unstack(level=-1, fill_value = 0).astype(int)  # Функция Unstack преобразует уровни индекса в столбцы|Аргумент level=-1 указывает, что нужно "развернуть" последний уровень индекса
data.columns = data.columns.droplevel() # Убирается уровень столбцов, который появился после unstack
data.columns.name = None # Удаляется имя
print(data) #  Печатаем после