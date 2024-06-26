class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        
        for start, end, weight in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append((end, weight))
            else:
                self.graph_dict[start] = [(end, weight)]
        
    def get_paths(self, start, end, path=[], total_weight=0):
        path = path + [(start, total_weight)]
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        
        for (node, weight) in self.graph_dict[start]:
            if node not in [p[0] for p in path]:
                new_paths = self.get_paths(node, end, path, total_weight + weight)
                for p in new_paths:
                    paths.append(p)
                    
        return paths
    
    def get_shortest_path(self, start, end, path=[], total_weight=0):
        path = path + [(start, total_weight)]
        
        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for (node, weight) in self.graph_dict[start]:
            if node not in [p[0] for p in path]:
                sp = self.get_shortest_path(node, end, path, total_weight + weight)
                if sp: # if sp is not None
                    if shortest_path is None or sum([p[1] for p in sp]) < sum([p[1] for p in shortest_path]):
                        shortest_path = sp
                        
        return shortest_path
        

routes = [
    ("Mumbai", "Paris", 7000),
    ("Mumbai", "Dubai", 2000),
    ("Paris", "Dubai", 3000),
    ("Paris", "New York", 8000),
    ("Dubai", "New York", 9000),
    ("New York", "Toronto", 600)
]

route_graph = Graph(routes)

start = "Paris"
end = "New York"

print(f"Shortest path between {start} and {end}:", route_graph.get_shortest_path(start, end))
