import rand_data
import numpy as np
import random
import matplotlib.pyplot as plt

#implement the perceptron learning algorithm
#use rand_data.py to generate random training examples of count n = 4, 10, 20
#In each case run the algorithm until for all examples the weight vector dot the example vector times the example's labelling (+1,-1) > 0
#For each n plot the weight vector and calculate the margin for that solution


#take in N examples a of dimension d
#add extra dimension containing a 1 on all examples
#want to generate a W of dimension d+1 such that


def learnWeights(data):

	#preprocess data
	D = np.array(data)
	size_dataset, y = D.shape
	D = np.c_[D[:,[0,1]], np.ones(size_dataset), D[:,[2]]]
	w = D[0][:3]*D[0][3]
	list_w = [w]

	#create initial list of training points that are wrongly classified
	for i in xrange(size_dataset):
		misList = []
		works_i = (np.dot(w,D[i][:3]))*(D[i][3]) > 0
		if not works_i:
			misList.append(i)

	#modify w iteratively until all points are classified correctly
	while misList:# and x < n:
		i = random.choice(misList)
		w = w + D[i][:3]*(D[i][3])
		list_w.append(w)
		misList = []
		for i in xrange(size_dataset):
			works_i = (np.dot(w,D[i][:3]))*D[i][3] > 0
			if not works_i:
				misList.append(i)

	#calculate the margin
	margin = 1000000000000
	for i in xrange(size_dataset):
		if (np.dot(w,(D[i][:3])/np.linalg.norm(D[i]))*(D[i][3]/np.linalg.norm(D[i]))) < margin: #D[i][:3]
			margin = (np.dot(w,(D[i][:3])/np.linalg.norm(D[i]))*(D[i][3]/np.linalg.norm(D[i])))

	return w, list_w, margin


#plot Ws
#calculate margin
#normalize all rows of D

data4 = rand_data.generateData(2)
data10 = rand_data.generateData(10)
data20 = rand_data.generateData(20)

w4_final, w4_list, w4_margin = learnWeights(data4)
#print "data: ", np.array(data4)
print "w4: ", w4_final
print "w4 list: ", w4_list
print "w4 margin: ", w4_margin
w10_final, w10_list, w10_margin = learnWeights(data10)
#print "\n\n\ndata: ", np.array(data10)
print "w10: ", w10_final
print "w10 list: ", w10_list
print "w10 margin: ", w10_margin
w20_final, w20_list, w20_margin = learnWeights(data20)
#print "\n\n\ndata: ", np.array(data20)
print "w20: ", w20_final
print "w20 list: ", w20_list
print "w20 margin: ", w20_margin



# quickly written plots

D = np.array(w4_list)
np.c_[D[:,[0,1]]]
f = plt.figure(1)
plt.plot(D[0], D[1])
plt.xlabel("first dimension of weight vec")
plt.ylabel("second dimension of weight vec")
f.show()


D = np.array(w10_list)
D = np.c_[D[:,[0,1]]]
g = plt.figure(2)
plt.plot(D[0], D[1])
plt.xlabel("first dimension of weight vec")
plt.ylabel("second dimension of weight vec")
g.show()

D = np.array(w20_list)
D = np.c_[D[:,[0,1]]]
h = plt.figure(2)
plt.plot(D[0], D[1])
plt.xlabel("first dimension of weight vec")
plt.ylabel("second dimension of weight vec")
h.show()

raw_input()