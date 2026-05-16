from cgnodes import *

# first create all ValueNode objects
x1 = ValueNode()
x2 = ValueNode()
q = ValueNode()
f = ValueNode()
# second create all <Operator>Node objects
mult = MultiplyNode(x1, x2, q)
square = SquareNode(q, f)
# finally build the graph by declaring inputs and outputs as 2 lists of
    #ValueNode objects
cg = CompGraph([x1, x2], [f])
# test the graph with some random inputs
cg.forward([2.0, 4.0])
print(f"f = {f.v}") # should print 64.0