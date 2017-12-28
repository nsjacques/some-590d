import matplotlib.pyplot as plt #check out seaborn? - gui mpl?
import random

'''
Count Min Sketch data structure
'''
class CMS:
	'''
	Constructor takes range of hash functions, number of hash funcitons
	'''
	def __init__(self, buckets, functions):
		self.num_buckets = buckets
		self.num_functions = functions
		self.num_insertions = 0
		self.counters = [[0]*buckets for x in xrange(functions)]
		self.hashlist = []

		'''
		Generate hashes from a linear hash family on prime P
		For P, I just choose a random prime from a list of 14 random large primes (E4-E6)
		That works fine for this problem.
		'''
		p = random.choice([11393,11071,11689,11887,11897,11903,101359,101363,
			101377,101383,101399,1002553,1002569,1002577])
		arange = range(1,p)
		brange = range(0,p+1)
		
		for i in xrange(self.num_functions):
			a = random.choice(arange)
			b = random.choice(brange)
			h = lambda x : (((a*x + b) % p) % self.num_buckets)
			self.hashlist.append(h)

	'''
	for value v increment cms at [i][h_i(v)] for each hash function i
	'''
	def inc(self, value):
		for i in xrange(self.num_functions):
			self.counters[i][self.hashlist[i](value)] += 1
		self.num_insertions += 1

	'''
	return cms frequency count of v i.e. the number of times inc(v) has been called
	'''
	def count(self, value): 
		li = []
		for i in xrange(self.num_functions):
			li.append(self.counters[i][self.hashlist[i](value)])

		return min(li)


'''
Instantiate and fill a CMS

'''
# error = .0001 so #buckets=2.7E4
my_cms = CMS(27183, 25)
actual_freq = [0]*1001

for i in xrange(1000000):
	datum = random.randint(1,1000)
	my_cms.inc(datum)
	actual_freq[datum]+=1


'''
Prepare data
'''

x_list = []
y_list = []
del actual_freq[0]

for i in range(1,1001):
	y_list.append(my_cms.count(i))
	x_list.append(i)

'''
Plot cms frequency and actual frequency
'''

f = plt.figure(1)
plt.plot(x_list, y_list)
plt.xlabel("item")
plt.ylabel("cms frequency")
f.show()

g = plt.figure(2)
plt.plot(x_list, actual_freq)
plt.xlabel("item")
plt.ylabel("actual frequency")
g.show()

raw_input()
