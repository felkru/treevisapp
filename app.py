import streamlit as st
import pydot
from streamlit_tags import st_tags
import time
import re

def extract_dicts(input_string):
    # Define the regex pattern
    pattern = r'\((\w+),(\w+)\)|(\w+)'

    # Find all matches in the input string
    matches = re.findall(pattern, input_string)

    result = []
    for match in matches:
        if match[0] and match[1]:  # If the match is a pair in parentheses
            result.append({"label": match[0], "id": match[1]})
        elif match[2]:  # If the match is a single string
            result.append({"label": match[2], "id": match[2]})

    return result

"# Jarons Tree Creator"

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="white")

"## Inputs:"

st.session_state['edges'] = st_tags(
        label="Add edges. Format: 'Node1,Node2':",
        text="e.g. A,B"
    )

# Edges for debug purposes
# st.write(st.session_state['edges'])

for edge in [e for e in st.session_state['edges'] if ',' in e]:
    edge = extract_dicts(edge)

    node1 = pydot.Node(edge[0]['id'], label=edge[0]['label'])
    graph.add_node(node1)
    node2 = pydot.Node(edge[1]['id'], label=edge[1]['label'])
    graph.add_node(node2)

    graph.add_edge(pydot.Edge(node1, node2))

"## Preview:"
# Save the graph to a file
graph.set_size('"10,10!"')
graph.write_png('graph.png')

st.image('graph.png')

st.download_button(
    label="Download Image",
    data=graph.create_png(),
    file_name="graph.png",
    mime="image/png"
)
