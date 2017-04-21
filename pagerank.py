import time, numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import lil_matrix

def createHMatrix(graph):
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

def createHRoof(H):
	start = time.time()
	n = H.shape[0]
	sumRows = H.sum(axis=1)
	newRow = np.ones((1,n)) * 1.0 / n
	a = []
	for i in range(n):
		if sumRows[i] == 0:
			a.append(i)
	H = H.tolil()
	H[a,:] = newRow
	end = time.time()
	print("Created new H Matrix: " + str((end - start) * 1000) + "ms")
	return H.tocsr()

def createGMatrix(HRoof, theta):
	start = time.time()
	G = theta * HRoof + (1 - theta) * (1/HRoof.shape[0]) * np.ones(HRoof.shape)
	end = time.time()
	print("Created G Matrix: " + str((end - start) * 1000) + "ms")
	return G

def pageRank(G):
	start = time.time()
	n = G.shape[0]
	pi = np.ones((1, n)) * 1/(n)
	newPi = pi.dot(G)
	i = 0
	while np.linalg.norm(newPi - pi) > 0.0001 and i < 50:
		pi = newPi
		newPi = pi.dot(G)
		i += 1
	end = time.time()
	print("Page rank converged: " + str((end - start) * 1000) + "ms")
	return newPi

def completePageRank(graph):
	H = createHMatrix(graph)
	HRoof = createHRoof(H)
	g = createGMatrix(HRoof, .85)
	return pageRank(g)

def file_len(full_path):
  f = open(full_path)
  nr_of_lines = sum(1 for line in f)
  f.close()
  return nr_of_lines

def getGraphFromMatrix(file):
	n = file_len(file)
	f = open(file)
	graph = np.zeros((n,n))
	i = 0
	for line in f:
		graph[i] = np.fromiter(line.strip(), dtype=int)
		i = i + 1
	return graph

def getGraphFromEdgelist(file):
	f = open(file)
	n = int(f.readline().strip())
	graph = np.zeros((n+2,n+2))
	next(f)
	for line in f:
		edge = line.strip().split("\t")
		graph[int(edge[0]), int(edge[1])] = 1
	return graph

graph = getGraphFromEdgelist("p2p-Gnutella04.txt")
graph = csr_matrix(graph)
graph.eliminate_zeros()
rank = completePageRank(graph.todok())
print("Page Rankings: " + str(rank))
print("Maximum Page Rank Index: " + str(rank.argmax(axis=1)))