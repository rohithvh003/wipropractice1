import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,5,6])
plt.show()

x=[1,2,3,4]
y=[10,20,25,30]

plt.plot(x,y,marker="o",linestyle="-")
# plt.show()
plt.xlabel("x Axis")
plt.ylabel("y Axis")
plt.title("Line chart")
plt.grid(True)
plt.show()


names = ["A", "B", "C", "D"]
scores = [80,90,30,50]
plt.bar(names,scores)
plt.title("Student Scores")
plt.show()

plt.barh(names,scores)
plt.show()

plt.scatter(x,y)
marks = [50,60,70,77,86]
plt.hist(marks,bins=5)
plt.title("Marks")
plt.show()

labels=["Chrome","Firefox","Edge"]
sizes=[50,60,77]
plt.pie(sizes,labels=labels,autopct="%1.1f%%" )
plt.title("Browser Usage")
plt.show()

