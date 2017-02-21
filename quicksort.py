import random, time

def swap(unsortedList, j, k):
	temp = unsortedList[j]
	unsortedList[j] = unsortedList[k]
	unsortedList[k] = temp

def partition (unsorted, low, high):
	pivot = low
	low = low + 1 
	while high >= low:
		while low < len(unsorted) and unsorted[low] < unsorted[pivot]:
			low = low + 1
		while unsorted[high] > unsorted[pivot] and high >= 0:
			high = high - 1
		if (low < high):
			swap(unsorted, low, high)
	swap(unsorted, pivot, high)
	return high


def quicksort(unsorted, low, high):
	if high <= low:
		return
	pivot = partition(unsorted, low, high)
	quicksort(unsorted, low, pivot-1)
	quicksort(unsorted, pivot+1, high)

for i in xrange(0,10):

	unsorted = [i for i in xrange(1000000)]
	random.shuffle(unsorted)
	start = time.time()
	quicksort(unsorted, 0, len(unsorted)-1)
	end = time.time()
	if all(unsorted[i] <= unsorted[i+1] for i in xrange(len(unsorted)-1)):
		print "List Sorted: Took " + str(end*1000 - start*1000) + "ms"