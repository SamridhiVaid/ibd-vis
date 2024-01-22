import pickle
import pprint

class Node:
    def __init__(self):
        self.children = {}
        self.size = 0
        self.community_patients = 0
        self.ICDs = []
        
    
    def compute_total_community_patients(self):
        total = self.community_patients
        for child in self.children.values():
            total += child.compute_total_community_patients()
        return total
    
    def count_children_in_subtree(self):
        count = len(self.children)
        for child in self.children.values():
            count += child.count_children_in_subtree()
        return count

    def print_node(self):
        total_community_patients = self.compute_total_community_patients()  # Fix: Add this line to compute the total community patients
        total_children_count = self.count_children_in_subtree()  # Fix: Add this line to compute the total children count
        print(f"Size: {self.size}")
        print(f"Community Patients: {self.community_patients}")
        print(f"ICDs: {self.ICDs}")
        print(f"Children: {list(self.children.keys())}")
        print(f"Total Community Patients in Subtree: {total_community_patients}")
        print(f"Total Children Count in Subtree: {total_children_count}")



def convert_data_to_react_format(node, prefix='', id=0):
    nodes = {}
    edges = []
    node_id = str(id)
    nodes[node_id] = { 'size': node.size, 'community_patients': node.community_patients, 'ICDs': node.ICDs, 'Children': [prefix + char for char in node.children.keys()],'totalChildrenInSubtree': node.count_children_in_subtree(), 'totalCommunityPatients': node.compute_total_community_patients() }
    for char, child in node.children.items():
        child_id = str(id + 1)
        edges.append({'id': f"{node_id}->{child_id}", 'source': node_id, 'target': child_id, 'hidden': True})
        child_nodes, child_edges, id = convert_data_to_react_format(child, prefix + char, id + 1)
        nodes.update(child_nodes)
        edges.extend(child_edges)
    return nodes, edges, id

pickle_file = open('./f_hierarchical_data.pickle', 'rb')
root = pickle.load(pickle_file)

initialNodes, initialEdges, _ = convert_data_to_react_format(root)

#store initial nodes and edges in a log file
# pickle.dump(initialNodes, open('./initial
pprint.pprint(initialNodes)
#pprint.pprint(initialEdges)

#save initial nodes in log
#python3 text.py /log2<initialNodes.txt

#save initial edges in log

#python3 text.py > log &2>1  

