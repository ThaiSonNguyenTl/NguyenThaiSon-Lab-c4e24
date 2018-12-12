from matplotlib import pyplot

#1 prepare data
machine_counts = [18,4,2]

#2 prepare labels
machine_name = ["PC","Mac","linux"]

#3 draw pie
pyplot.pie(machine_counts,labels= machine_name)

#4show
pyplot.show()
