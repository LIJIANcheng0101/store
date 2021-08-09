f = open(file="baidu_x_system.log", mode="r", encoding="utf-8")
data = f.readlines()
dt = dict()
for val in data:
    t = val.split(" ", 1)[0]
    if t in dt:
        dt[t] += 1
    else:
        dt[t] = 0
print(dt)
f.close()
