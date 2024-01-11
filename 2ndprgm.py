class Graph:
    def __init__(self, graph, heuristic, start):
        self.graph, self.H, self.start = graph, heuristic, start
        self.parent, self.status, self.solutionGraph = {}, {}, {}

    def applyAOStar(self):
        self.aoStar(self.start, False)

    def getNeighbors(self, v):
        return self.graph.get(v, '')

    def getStatus(self, v):
        return self.status.get(v, 0)

    def setStatus(self, v, val):
        self.status[v] = val

    def getHeuristic(self, n):
        return self.H.get(n, 0)

    def setHeuristic(self, n, value):
        self.H[n] = value

    def printSolution(self):
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("------------------------------------------------------------")
        print(self.solutionGraph)
        print("------------------------------------------------------------")

    def computeMinCostChildNodes(self, v):
        minCost, costToChild = 0, {}
        costToChild[minCost] = []
        flag = True

        for nodeInfoList in self.getNeighbors(v):
            cost, nodeList = 0, []
            for c, weight in nodeInfoList:
                cost += self.getHeuristic(c) + weight
                nodeList.append(c)

            if flag:
                minCost = cost
                costToChild[minCost] = nodeList
                flag = False
            elif minCost > cost:
                minCost = cost
                costToChild[minCost] = nodeList

        return minCost, costToChild[minCost]

    def aoStar(self, v, backTracking):
        print("HEURISTIC VALUES:", self.H)
        print("SOLUTION GRAPH:", self.solutionGraph)
        print("PROCESSING NODE:", v)
        print("-----------------------------------------------------------------------------------------")

        if self.getStatus(v) >= 0:
            minCost, childNodeList = self.computeMinCostChildNodes(v)
            self.setHeuristic(v, minCost)
            self.setStatus(v, len(childNodeList))
            solved = True

            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.getStatus(childNode) != -1:
                    solved = solved and False

            if solved:
                self.setStatus(v, -1)
                self.solutionGraph[v] = childNodeList

            if v != self.start:
                self.aoStar(self.parent[v], True)

            if not backTracking:
                for childNode in childNodeList:
                    self.setStatus(childNode, 0)
                    self.aoStar(childNode, False)


h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1, 'T': 3}
graph1 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}

G1 = Graph(graph1, h1, 'A')
G1.applyAOStar()
G1.printSolution()