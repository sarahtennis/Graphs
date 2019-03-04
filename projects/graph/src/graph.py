"""
Simple graph implementation
"""

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return (len(self.queue))

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")
    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty....
        while q.size() > 0:
           # Dequeue the first node from the queue
           v = q.dequeue()
           # If that node has not been visted...
           if v not in visited:
              # Mark it as visited
              print(v)
              visited.add(v)
              # Then, put all of it's children into the queue
              for neighbor in self.vertices[v]:
                  q.enqueue(neighbor)
    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex_id)
        # While the stack is not empty....
        while s.size() > 0:
           # Pop the top node from the stack
           v = s.pop()
           # If that node has not been visted...
           if v not in visited:
              # Mark it as visited
              print(v)
              visited.add(v)
              # Then, put all of it's children into the stack
              for neighbor in self.vertices[v]:
                  s.push(neighbor)

    '''
    Part 3.5: Implement Depth-First Traversal using Recursion

    Write a function within your Graph class that takes takes a starting node
    as an argument, then performs DFT using recursion.
    Your function should print the resulting nodes in the order they were visited.
    '''
    def dft_recursive(self, starting_vertex_id):
        # recursive helper function
        def recursion(vertex):
            # mark id in visited set and print node (requirement)
            visited.add(vertex)
            print(vertex)
            # loop through connections from vertex at given id
            for connected_vertex in self.vertices[vertex]:
            # if connect already visited, do nothing
            # if not visited, run recursion on node
                if connected_vertex not in visited:
                    recursion(connected_vertex)

        # set to hold visited vertices
        visited = set()
        
        if starting_vertex_id in self.vertices:
            # put starting in set
            visited.add(starting_vertex_id)
            # run recursion() on starting
            recursion(starting_vertex_id)
        else:
            print('Vertex not in graph')
        

