import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])
plt.title("plot1")

plt.subplot(1,2,2)
plt.bar(["a","b","c"],[4,5,6])
plt.title("Plot 2")

plt.show()
plt.savefig("plot.png")
