This document is in response to a request related to an interview:


I’m asking candidates to review a use case for a small, current project and to outline their high-level technical approach. I would appreciate it if you could do so. Below I’ve provided the description of it. In particular, I’m looking at how you would approach it, particularly on how to reduce risk and cost for the client and prove the idea is feasible. You can choose the tech components you might use, from custom-coding to SaaS platforms or others you may be familiar with.

Here’s the high-level overview.

    Business Opportunity: Reduce effort of finding accurate part and order related information.
    Use Case: Plumbing distributor has a large number of PNG/TIFF catalog images going back many years they want to be able to search with an LLM, to:
        Quickly find the part breakdown diagram
        Identify related parts and part numbers to order
        ALSO query customer order history in a Netsuite system for customer order history, e.g., “what parts did CUSTOMER buy recently.”
    Solution:
        Needs to create a way to search visual images, all stored in a file share today.
        Need to provide links to source catalog for visual reference
        Needs to be able to look up customer details in Netsuite.
    Users:
        Initially internal staff only, from customer service to parts teams. Eventually may extend to external customers via a web chatbot.

Here’s a loom video where I had walked through this with the customer. https://www.loom.com/share/d5aead36a81e403db182bb145151e853?sid=3b0791ad-a92c-4914-a499-cb187f7d91f0


These where the follow up questions and answers that were provided to me before I drafted my document:



- What specific functionalities do you expect the LLM to perform with the catalog images' data? Is it to interpret the text extracted via OCR, understand queries in natural language, or both? I didn’t want to be prescriptive in how you approach it. Ultimately, the business need is to be able to use natural language to be able to find the data they need sourced from the images. There are several ways I think that could be accomplished.

- Could you provide specific examples of search queries you anticipate from users? This will help in understanding the complexity and scope of natural language processing required. Yes. For example:

    “What is the part number for the valve on an American Standard Williamsburg faucet?”
    “Show me the part diagram for the American Standard Williamsburg Faucet?”
    “What customers have purchased the American Standard Williamsburg faucet in the last two months?”

- How should the LLM utilize the customer order history from Netsuite? Is the goal to generate insights, predict future orders, or enhance search capabilities based on past behavior?

Good question. For now, we are thinking this is querying order-related information in a natural language interface, for internal agents (customer service, parts, etc.). Ideally this would be part of one LLM-backed agent, combining the ability to search across the two key datastores mentioned (catalog and Netsuite). No need for analytics, prediction, etc.