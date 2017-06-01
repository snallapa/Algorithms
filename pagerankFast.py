import time, numpy as np
import scipy.linalg
from scipy.sparse import csr_matrix
from scipy.sparse import lil_matrix

def createPMatrix(graph):
	start = time.time()
	outgoingLinks = graph.sum(axis=1)
	indices = graph.nonzero()
	for i in range(len(indices[0])):
		row = indices[0][i]
		col = indices[1][i]
		graph[row, col] = graph[row, col] / outgoingLinks[row]
	end = time.time()
	print("Created H Matrix: " + str((end - start) * 1000) + "ms")
	return graph.tocsr()

def pageRank(P, theta):
	start = time.time()
	P = P.transpose()
	n = P.shape[0]
	v = np.ones((n,1)) * 1.0 / n
	pi = np.ones((n,1)) * 1.0 / n
	newPi = theta * P.transpose().dot(pi)
	gamma = scipy.linalg.norm(pi) - scipy.linalg.norm(newPi)
	newPi = newPi + gamma * v
	i = 0
	while scipy.linalg.norm(newPi - pi) > 0.0001:
		pi = newPi
		newPi = theta * P.dot(pi)
		gamma = scipy.linalg.norm(pi) - scipy.linalg.norm(newPi)
		newPi = newPi + gamma * v
		i += 1
	end = time.time()
	print("Page rank converged: " + str((end - start) * 1000) + "ms")
	return newPi.transpose()

def completePageRank(graph):
	start = time.time()
	P = createPMatrix(graph)
	rank = pageRank(P, .85)
	end = time.time()
	print("Entire Process: " + str((end - start) * 1000) + "ms")
	return rank
print("Reading Graph from file")
graph = scipy.sparse.load_npz("google.npz")
print("Starting page rank")
rank = completePageRank(graph.todok())[0]
print("Page Rankings: " + str(rank))
print("Min to Max Page Rank Index: " + str(np.argsort(rank)))