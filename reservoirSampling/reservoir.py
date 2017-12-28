import matplotlib.pyplot as mpl #check out seaborn? - gui mpl?
import random

#reservoir sampling with a size one reservoir
def reservoirSample(stream):

	i = 0
	reservoir = stream[i]

	for elem in stream[1:]:
		i=i+1
		p = 1.0/i

		if (random.random() < p):
			reservoir = elem

	return reservoir


print "Single run result: ", reservoirSample(range(1,101))

list = []
for x in range(1000):
	list.append(reservoirSample(range(1,101)))
mpl.hist(list, 99, histtype='step')
mpl.xlabel("element")
mpl.ylabel("times selected")
mpl.show()

list = []
for x in range(10000):
	list.append(reservoirSample(range(1,101)))
mpl.hist(list, 99, histtype='step')
mpl.xlabel("reservoir sample run")
mpl.ylabel("reservoir sample output")
mpl.show()

list = []
for x in range(100000):
	list.append(reservoirSample(range(1,101)))
mpl.hist(list, 99, histtype='step')
mpl.xlabel("reservoir sample run")
mpl.ylabel("reservoir sample output")
mpl.show()

'''
list = []
for x in range(100000*5):
	list.append(reservoirSample(range(1,101)))
mpl.hist(list, 99, histtype='step')
mpl.xlabel("reservoir sample run")
mpl.ylabel("reservoir sample output")
mpl.show()
'''


#run 1000 times and keep track of each result
#run 10000 times and keep track of each result
#run 100000 times and keep track of each result