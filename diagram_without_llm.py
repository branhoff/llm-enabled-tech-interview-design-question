from graphviz import Digraph

dot = Digraph(comment='Adapted Technical Approach Overview Without LLM')

# Setting the graph to flow from left to right
dot.attr(rankdir='LR')

# Defining nodes with shapes to represent different components of the system
dot.node('A', 'User Interface\n(Direct Query Interface)', shape='rectangle')
dot.node('B', 'OCR Processing\n(e.g., Tesseract OCR)', shape='cylinder')
dot.node('C', 'Catalog Image Database\n(e.g., File Share)', shape='folder')
dot.node('D', 'Text Indexing & Search\n(e.g., Elasticsearch)', shape='cylinder')
dot.node('E', 'Customer Order History Query', shape='component')
dot.node('F', 'Netsuite API Integration', shape='cylinder')

# Updating the edges to reflect the flow and separation of processes
dot.edge('C', 'B', 'processed by OCR to extract text')  # Clarifying the one-way process from images to OCR
dot.edge('B', 'D', 'text indexed in')  # Direct flow from OCR to indexing
dot.edge('A', 'D', 'queries')  # Direct querying to the indexed text
dot.edge('A', 'E', 'requests order history')  # Direct requests for order history
dot.edge('E', 'F', 'retrieves from')  # Retrieval from Netsuite

# Visual representation adjustments
dot.format = 'png'
path = "./adapted_technical_approach_overview_without_llm_updated"
dot.render(path, view=True)  # Set view=False if you do not want the diagram to open automatically

# The diagram is saved as 'adapted_technical_approach_overview_without_llm_updated.png'
