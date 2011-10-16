class Node:
    def __init__(self,label):
        self.label = label
        self.links = []
        
        self.path = []
        self.count = 0

    def paths(self):
        out = ""
        for i,p in enumerate(self.path):
            if i>0:
                out+=" -> "
            out+=p.label
        return out
    
class Link:
    def __init__(self,a,b,costs=1):
        self.a = a        
        self.b = b
        self.costs = costs
        a.links.append(self)
        b.links.append(self)


a = Node("a")
b = Node("b")
l = Link(a,b)
print "{} -> {}".format(a.label,b.label)

arad = Node("arad")
zerind = Node("zerind")
oradea = Node("oradea")
timisora = Node("timisora")
sibiu = Node("sibiu")
pitesti = Node("pitesti")
fagaras = Node("fagaras")
rimnicu = Node("rimnicu vilcea")
bucharest = Node("bucharest")
lugoj = Node("lugoj")

Link(arad,zerind)
Link(zerind,oradea)
Link(oradea,sibiu)
Link(arad,sibiu)
Link(sibiu,fagaras)
Link(sibiu,rimnicu)
Link(rimnicu,pitesti)
Link(fagaras,bucharest)
Link(pitesti,bucharest)
Link(arad,timisora)
Link(timisora,lugoj)


class Search1:
    def __init__(self,target):
        self.frontier =[]
        self.target = target
        self.actual = []
        self.explored = []

    def toFrontier(self,node, parent):
        if node not in self.frontier and node not in self.explored and node not in self.actual:
            self.frontier.append(node)
            node.path += parent.path + [node]
        
                

    def explore(self,node):
        self.frontier.remove(node)
        self.actual.append(node)   
        
        print "trying "+ node.label+" ("+node.paths()+")"
        if node == self.target:
            print "found!"
        
        for l in node.links:
            self.toFrontier(l.a,node)
            self.toFrontier(l.b,node)


        self.actual.remove(node)
        self.explored.append(node)

        if len(self.actual)>0:
            child = self.actual[0]
            self.explore(child)
        elif len(self.frontier)>0:
            child = self.frontier[0]
            self.explore(child)
        
    def goOn(self,start):
        print "traveling from {} to {}...".format(start.label,self.target.label)
        self.toFrontier(start,start)
        self.explore(self.frontier[0])
        
s = Search1(bucharest)
s.goOn(arad)
