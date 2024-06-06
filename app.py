import streamlit as st
import pydot
from IPython.display import Image, display
from streamlit_tags import st_tags

"# Jarons Tree Creator"

if 'edges' not in st.session_state:
    st.session_state['edges'] = []

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="white")

"## Inputs:"
txt_input = st.text_input("Add edges. Format: 'Node1,Node2':", placeholder='A,B')

if txt_input:
    st.session_state['edges'] += [txt_input.split(",")]

# Edges for debug purposes
# st.write(st.session_state['edges'])

for edge in st.session_state['edges']:
    graph.add_edge(pydot.Edge(edge[0], edge[1], color="black"))

st.button("Clear", on_click=lambda: st.session_state.edges.clear())

"## Preview:"
# Save the graph to a file
graph.set_size('"10,10!"')
graph.write_png('graph.png')

# Display the graph
display(Image(filename='graph.png'))

st.image('graph.png')

st.download_button(
    label="Download Image",
    data=graph.create_png(),
    file_name="graph.png",
    mime="image/png"
)