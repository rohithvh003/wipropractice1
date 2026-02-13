import matplotlib.pyplot as plt
import seaborn as sns

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

plt.plot(months,sales,marker="o",linestyle="-")
# plt.show()
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Line chart - Monthly Sales")
plt.grid(True)
plt.show()
plt.savefig("Line Chart.png")

sns.barplot(x=months, y=sales)

plt.title("Bar plot - Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.show()
plt.savefig("Bar plot.png")