import numpy as np


with open(r"C:02-real.txt", 'r') as file:
    
    totalSafe=0

    for line in file:
    
    
        array = np.fromstring(line, dtype=int, sep=" ")

        print(array)

        diff = np.diff(array)

        print (diff)

        if np.all((diff > 0) & (diff <= 3)) or np.all((diff >= -3) & (diff < 0)):
            totalSafe += 1
        else:
            i=0
            while i < len(array):
                copy = array
                copy = np.delete(copy, i)
                diff2 = np.diff(copy) 
                if np.all((diff2 > 0) & (diff2 <= 3)) or np.all((diff2 >= -3) & (diff2 < 0)):
                    totalSafe += 1
                    i = len(array)
                
                i += 1

       

print("totalSafe",totalSafe)
