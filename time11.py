import time

"""

x=time.time()
y=0
while y<10:
    print("Yo whats up mate")
    y+=1
print(f"Time taken is {time.time()-x}")

z=time.time()
for i in range(10):
    print("Yo whats up mate")
print(f"Time taken is {time.time()-z}")

"""
# again comparing time
"""

x = time.time()

y = 0
while y < 10000000:
    y += 1

print("While:", time.time() - x)

z = time.time()

for i in range(10000000):
    pass

print("For:", time.time() - z)

"""
"""
start = time.perf_counter()
for i in range(100000000):
    pass
end= time.perf_counter()

print("Time taken is ", end-start)
"""

# day_time=time.asctime()
# print(day_time)
ranking=1
for i in range(10):
    
    print("Hello this is Darpan ",ranking)
    ranking+=1
    time.sleep(1)

