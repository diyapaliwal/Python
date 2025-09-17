import numpy as np

ages = np.array([[21,17,19,20,16,30,18,65],
                 [33,37,54,87,90,12,45,23]])
teenagers = ages[ages <= 19]
# print(teenagers)
youth = ages[(ages >=18) & (ages <= 65)]
# print(youth)
evens = np.sort(ages[ages % 2 == 0])
odds = np.sort(ages[ages % 2 != 0])
print(evens)
print(odds)