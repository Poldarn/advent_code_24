import numpy as np


with open(r"C:\02-real.txt", 'r') as file:
    
    totalSafe=0

    for line in file:
    
        array = np.fromstring(line, dtype=int, sep=" ")

        previousDirecction = 0

        chance = 1
        safe = 1
        i = 1
        j = i - 1

        
        while i < len(array):

        

            direcction = array[i] - array[j] 

            print(line)
            print("i",i)
            print("j",j)
            print("safe",safe)
            print("chance", chance)
            if (abs(direcction) == 0 or abs(direcction) >=4) or np.sign(direcction) + np.sign(previousDirecction) == 0:
                if chance == 0:
                    safe = 0
                    i = len(array) 
                    print("----------break-------")
                else: 
                    print("--++++-chance+++-")
                    chance = 0
                    j = j - 1
                    if i == 2 and j==0: previousDirecction = 0
            else:
                previousDirecction = direcction
                i += 1
                j = i - 1
        

        totalSafe += safe
       

print("totalSafe",totalSafe)
