from event_planner.agent import agent


query = input("What is your query?")
# prompt= """
#     Alfred needs to prepare for the party. Here are the tasks:
#     1. Prepare the drinks - 30 minutes
#     2. Decorate the mansion - 60 minutes
#     3. Set up the menu - 45 minutes
#     4. Prepare the music and playlist - 45 minutes

#     If we start right now, at what time will the party be ready? [Answer shall be like 5 hours 24 minutes 12 seconds from now, etc]
# """
system_prompt = """
You are a precise coding assistant.
- Always generate clean, minimal, and correct Python code.
- Prefer functions with clear names and docstrings.
- Avoid redefining functions unnecessarily.
- Return only the final working solution, no exploratory scraps.
- Output must be executable without manual fixes.
"""
response = agent.run(system_prompt + query)
# response = agent.run(prompt)
print("Agent says: ", response)
