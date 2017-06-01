import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import dok_matrix
import scipy.sparse
def getGraphFromEdgelist(file, delimiter=" "):
	nodetoid = {}
	counter = 0
	f = open(file)
	n = int(f.readline().strip())
	graph = dok_matrix((n,n))
	next(f)
	for line in f:
		edge = line.strip().split(delimiter)
		toid = int(edge[0])
		fromid = int(edge[1])
		if nodetoid.get(toid) == None:
			nodetoid[toid] = counter
			counter += 1
		if nodetoid.get(fromid) == None:
			nodetoid[fromid] = counter
			counter += 1
		graph[nodetoid.get(toid), nodetoid.get(fromid)] = 1
	return graph
graph = getGraphFromEdgelist("web-Google.txt", "\t")
graph = graph.tocsr()
scipy.sparse.save_npz("google", graph)