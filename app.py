import streamlit as st
import pydot
from IPython.display import Image, display

"# Jarons Tree Creator"

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="white")

graph.add_edge(pydot.Edge("Link A", "Link B", color="black"))
graph.add_edge(pydot.Edge("Link A", "Link C", color="black"))
graph.add_edge(pydot.Edge("Link A", "Link D", color="black"))
graph.add_edge(pydot.Edge("Link B", "-", color="black"))
graph.add_edge(pydot.Edge("Link C", "Link F", color="black"))
graph.add_edge(pydot.Edge("Link C", "Link G", color="black"))
graph.add_edge(pydot.Edge("-", "Link H", color="black"))
graph.add_edge(pydot.Edge("Link F", "Link I", color="black"))


# Save the graph to a file
graph.set_size('"10,10!"')
graph.write_png('graph.png')

# Display the graph
display(Image(filename='graph.png'))

"## Inputs:"



"## Preview:"
st.image('graph.png')

st.download_button(
    label="Download Image",
    data=graph.create_png(),
    file_name="graph.png",
    mime="image/png"
)