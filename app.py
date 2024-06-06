import streamlit as st
import pydot
from IPython.display import Image, display
from streamlit_tags import st_tags
import time

"# Jarons Tree Creator"

n_edges = 0
n_session = 0


def new_session(n_session=n_session):
    st.session_state['edges'] = st_tags(
        label="Add edges. Format: 'Node1,Node2':",
        text="e.g. A,B",
        key=n_session,
    )
    n_edges = 0
    n_session += 1


# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="white")

"## Inputs:"
st.button("Reset", on_click=new_session)

new_session(n_session)

# Edges for debug purposes
# st.write(st.session_state['edges'])

for edge in [e.split(",") for e in st.session_state['edges']]:
    graph.add_edge(pydot.Edge(edge[0], edge[1]))

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
