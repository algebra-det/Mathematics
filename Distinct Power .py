import time
t = time.time()

prev = []
new = []

for a in range(2,101):
    for b in range(2,101):
        c = a**b
        prev.append(c)

prev = sorted(prev)
for i in prev:
    if i in new:
        pass
    else:
        new.append(i)

print(len(new))

print(time.time()-t)