
class Graph():
    def __init__(self):
        self.numnodes = 0
        self.adjacentList = {}

    def addVertex(self, data):  # lets us peek at the top of element without removing it from the stack
        if data not in self.adjacentList:
            self.adjacentList[data] = []  # add key [data] to the empty object
            self.numnodes += 1
            return

    def addEdge(self, node1, node2):
        # its undirected graph
        if node2 not in self.adjacentList[node1]:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
            return
        return "it already exists"

    def showConnections(self):
        allNodes = dict(self.adjacentList)
        for i in allNodes:
            print(f'{i}-->{" ".join(map(str, self.adjacentList[i]))}')
            # print(" ".join(map(str, self.adjacentList[i])))


if __name__ == '__main__':
    g = Graph()

    # s.print_list()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addEdge(2, 3)
    g.addEdge(2, 1)
    g.addEdge(3, 1)

    g.showConnections()

    print(g.adjacentList)

    # s.push("Discord")
    # s.push("Udemy")
    # s.push("google")
    # print(s.peek())
    # s.print_list()
    # s.pop()
    # s.print_list()
