import streamlit as st
import pydot
import re

def extract_dicts(input_string):
    # Define the regex pattern
    pattern = r'\(([^,]*),([^)]*)\)|([^,]+)'

    # Find all matches in the input string
    matches = re.findall(pattern, input_string)

    result = []
    for match in matches:
        if match[0] or match[1]:  # If the match is a pair in parentheses
            label = match[0].strip() if match[0].strip() else " "
            result.append({"label": label, "id": match[1]})
        elif match[2]:  # If the match is a single string
            result.append({"label": match[2], "id": match[2]})

    return result

"# Jarons Tree Creator"

# instruction image
with st.expander("Tutorial", expanded=False):
    st.image('tutorial.png')

uploaded_file = st.file_uploader("Import Tree", type="txt")
if uploaded_file is not None:
    file_str = uploaded_file.getvalue().decode("utf-8")
    st.session_state['edges'] = st.text_input(label="Enter A,B;B,C", key="edge_input_value", value=file_str)
else:
    st.session_state['edges'] = st.text_input(label="Enter A,B;B,C", key="edge_input_value")

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="white")

for edge in st.session_state['edges'].split(" - "):
    edge = extract_dicts(edge)

    node1 = pydot.Node(edge[0]['id'], label=edge[0]['label'])
    graph.add_node(node1)
    node2 = pydot.Node(edge[1]['id'], label=edge[1]['label'])
    graph.add_node(node2)

    graph.add_edge(pydot.Edge(node1, node2))

"## Preview:"
# Save the graph to a file
graph.set_size(f'"{10 + 1.6 * len(st.session_state["edges"])},{10 + 1.6 * len(st.session_state["edges"])}!"')
graph.write_png('graph.png')
graph.write_svg('graph.svg')

st.image('graph.png')

st.download_button(
    label="Download SVG",
    data=graph.create_svg(),
    file_name="graph.svg",
    mime="image/png"
)

st.download_button(
    label="Export Tree",
    data=str(st.session_state['edges']),
    file_name="tree.txt",
    mime="text/plain"
)