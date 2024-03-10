from graphviz import Digraph

dot = Digraph(comment='Adapted Technical Approach Overview Without LLM')

# Setting the graph to flow from left to right
dot.attr(rankdir='LR')

# Defining nodes with shapes to represent different components of the system
dot.node('A', 'User Interface (Web/Chatbot)', shape='rectangle')
dot.node('B', 'OCR Processing\n(e.g., Tesseract OCR)', shape='cylinder')
dot.node('C', 'Catalog Image Database\n(e.g., File Share)', shape='folder')
dot.node('D', 'Text Indexing & Search\n(e.g., Elasticsearch)', shape='cylinder')
dot.node('E', 'Customer Order History Query', shape='component')
dot.node('F', 'Netsuite API Integration', shape='cylinder')
dot.node('G', 'Caching Layer', shape='folder')

# Updating the edges to reflect the flow without LLM
dot.edge('A', 'B', 'initiates OCR Processing')
dot.edge('B', 'C', 'extracts text from')
dot.edge('C', 'B', 'stores')
dot.edge('B', 'D', 'feeds into')
dot.edge('A', 'D', 'searches via')
dot.edge('A', 'E', 'requests')
dot.edge('E', 'F', 'retrieves from')
dot.edge('E', 'G', 'caches results with')
dot.edge('G', 'F', 'supplements')

# Visual representation adjustments
dot.format = 'png'
path = "./adapted_technical_approach_overview_without_llm"
dot.render(path, view=True)  # Set view=False if you do not want the diagram to open automatically

# The diagram is saved as 'adapted_technical_approach_overview_without_llm.png'
