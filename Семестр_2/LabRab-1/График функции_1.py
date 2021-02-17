import matplotlib.pyplot as plt

def my_func(x, a, b, c, d):
    return (a*x**2 + b*x + c) / (x + d)


styles = plt.style.available
plt.style.use(styles[7])

a = 0; b = -100; c = 100; d = 5
left = -100; right = 100; step = .5

data_x = []; data_y = []
pos_x = left

while pos_x <= right:
    try:
        pos_y = my_func(pos_x, a, b, c, d)
        data_x.append(pos_x)
        data_y.append(pos_y)
    except:
        pass
    pos_x += step

plt.plot(data_x, data_y, lw = 3, color = "#00ffff")

plt.grid(True)
plt.axhline(lw = 2, color = "#000")
plt.axvline(lw = 2, color = "#000")

plt.show()