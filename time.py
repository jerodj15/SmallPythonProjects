'''import time
print("image1")
time.sleep(3)
print("image2")
time.sleep(3)
print("image3")
'''

import time

for a in range(1,11):
    print("\n")
    time.sleep(2)
    for b in range(1,11):
        print (a,"x",b,"=",a*b)
