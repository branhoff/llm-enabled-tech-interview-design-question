from graphviz import Digraph

dot = Digraph(comment='Technical Solution Design for Plumbing Distributor Project')

# Setting graph direction (left to right)
dot.attr(rankdir='LR')

# Defining nodes with specific shapes for different components
dot.node('A', 'User Interface (Web/Chatbot)', shape='rectangle')
dot.node('B', 'Natural Language Query Processing\n(LLM like GPT-3)', shape='component')
dot.node('C', 'OCR Processing\n(e.g., Tesseract OCR)', shape='cylinder')
dot.node('D', 'Catalog Image Database\n(e.g., File Share)', shape='folder')
dot.node('E', 'Text Indexing & Search\n(e.g., Elasticsearch)', shape='cylinder')
dot.node('F', 'Customer Order History Query', shape='component')
dot.node('G', 'Netsuite API Integration', shape='cylinder')
dot.node('H', 'Unified Query Interface', shape='component')


# Adding edges to represent the flow and interactions
dot.edge('A', 'B', 'interprets via')
dot.edge('B', 'H', 'processes queries for')
dot.edge('C', 'D', 'extracts text from')
dot.edge('C', 'E', 'feeds into')
dot.edge('D', 'C', 'stores')
dot.edge('E', 'H', 'provides search results to')
dot.edge('F', 'G', 'retrieves data via')
dot.edge('G', 'H', 'integrates with')
dot.edge('H', 'A', 'displays results in')


# Render and save the diagram to a file
dot.format = 'png'
path = "./plumbing_distributor_project_diagram"
dot.render(path, view=True)  # Set view=False if you do not want the diagram to open automatically

# The diagram is saved as 'plumbing_distributor_project_diagram.png'
