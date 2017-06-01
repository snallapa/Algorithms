import time, numpy as np
import scipy.linalg
from scipy.sparse import csr_matrix
from scipy.sparse import lil_matrix

def createGMatrixFast(graph, theta):
	start = time.time()
	n = graph.shape[0]
	halfGProduct = (1 - theta) * (1/n)
	G = halfGProduct * np.ones(graph.shape)
	outgoingLinks = graph.sum(axis=1)
	indices = graph.nonzero()
	for i in range(len(indices[0])):
		row = indices[0][i]
		col = indices[1][i]
		G[row, col] = theta * (graph[row, col] / outgoingLinks[row]) + halfGProduct
	indicesOfZeroRows = np.where(outgoingLinks == 0)[0]
	newRow = np.ones((1,n)) * 1.0 / n
	for i in indicesOfZeroRows:
		G[i] = newRow
	end = time.time()
	print("Created G Matrix: " + str((end - start) * 1000) + "ms")
	return G


def pageRank(G):
	start = time.time()
	n = G.shape[0]
	pi = np.ones((1, n)) * 1/n
	newPi = pi.dot(G)
	i = 0
	while np.linalg.norm(newPi - pi) > 0.0001:
		pi = newPi
		newPi = pi.dot(G)
		i += 1
	end = time.time()
	print("Page rank converged: " + str((end - start) * 1000) + "ms")
	return newPi


def completePageRank(graph):
	start = time.time()
	G = createGMatrixFast(graph, .85)
	rank = pageRank(G)
	end = time.time()
	print("Entire Process: " + str((end - start) * 1000) + "ms")
	return rank
print("Reading Graph from file")
graph = scipy.sparse.load_npz("p2p-Gnutella04Sparse.npz")
#graph = scipy.sparse.load_npz("p2p-Gnutella31Sparse.npz")
print("Starting page rank")
rank = completePageRank(graph.todok())[0]
print("Page Rankings: " + str(rank))
print("Min to Max Page Rank Index: " + str(np.argsort(rank)))