from bank_agent import agent

def get_visual(query):
    response = agent.run(f"fetch articles on this topic {query} which are occured recently and please don't share any codes")
    return response.content

def get_explanation(query):
    response = agent.run(f"Explain the banking concept: {query}")
    return response.content

def get_code_example(query):
    response = agent.run(f"Give different examples or scenario for this {query} issue")
    return response.content
