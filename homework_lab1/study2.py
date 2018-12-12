from matplotlib import pyplot

#1 prepare data
phone_counts = [20,10,3]

#2 prepare labels
phone_name = ["iphone","Samsung","oppo"]

#3 draw pie
pyplot.pie(phone_counts,labels= phone_name,autopct="%.1f %%",shadow=True,explode=[0,0.02,0.1])
pyplot.title("iphone vs samsung vs oppo")
pyplot.axis("equal")
#4 show
pyplot.show()
