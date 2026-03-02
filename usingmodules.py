"""

#This are In Built modules

import random
random_number=random.randint(1,100) # gives a random number between 1 to 100 including 1,100
# print(random_number)
# rand=random.random() # gives random float integer between 0 and 1
rand=random.random()*100 # gives random float integer between 0 and 100
# print(rand)

channels=["CN","Nick","Disney","Disney XD","Sonic","Hungama"]
choice=random.choice(channels)
print(choice)


# Now To install external Modules.
# 1) Go to Terminal Below
# 2) Type python -m pip install (module name) for eg: python -m pip install scikit-learn
#import module and write your code.


"""

# Testing math modules
"""
import math
print(math.sqrt(81))
print(math.factorial(3))
print(math.pi)

"""


"""

# Testing date and time module
import datetime
import datetime

now = datetime.datetime.now()

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
birth=datetime.date(2004,8,12)
today=datetime.date.today()
lived= today-birth
print(f"I have lived {lived.days} days")


"""

# Testing Sys module
import sys
print(sys.platform)