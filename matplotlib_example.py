from matplotlib import pyplot

#1 prepare data
machine_counts = [18,4,2]

#2 prepare labels
machine_name = ["PC","Mac","linux"]

#3 draw pie
pyplot.pie(machine_counts,labels= machine_name, autopct="%.1f%%", shadow=True ,explode=[0,0.01,0.1])
#tao hinh tron
pyplot.axis("equal") 
#4show
pyplot.show()
