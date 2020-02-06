import time

start = time.time()
lst = [i for i in range(100)]
for i in range(10 ** 6):
    for item in lst:
        void = 1 < item
end = time.time()

delta = end - start
print("time elapsed in querying list of 100 rules: " + str(delta))


start = time.time()
hashset = set()
for i in range(255**4):
    hashset.add(i)
end = time.time()

delta = end - start
print("time elapsed with creating hashset over all possible ip addresses: " + str(delta))
