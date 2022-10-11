# Shortest-path-algorithms
Python shortest path algorithms (Bellman-Ford and Djkstra)

## Dijkstra Algorithm :
function `algoDijkstra(M, si)` 
where `M` is the matrix and `si` is the starting node.
Returns the list of all the nodes and their shortest path to the starting node if exists.

## Bellman-Ford Algorithm :
function `algoBellmanFord(M, si, fleches, n)` where `M` is the matrix, `si` is the starting node, `fleches` is the list of arrows *[departing node, arriving node]* and `n` is the number of nodes.
#### The three versions of Bellman-Ford
function `algoBellmanFordv1` creates the arrows in sequential order.
function `algoBellmanFordv2` creates the arrows by using the Breadth-first search method.
function `algoBellmanFordv3` creates the arrows by using the Depth-first search method.
