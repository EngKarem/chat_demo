import streamlit as st
from time import perf_counter as counter
from llama_index.llms.openai import OpenAI
from llama_index.core import PromptTemplate
from llama_index.core.agent import ReActAgent
from dotenv import load_dotenv
from vector_query_engine import create_tool
from agent_prompt import agentprompt

# Load environment variables
load_dotenv()


# Define function to initialize the tools and agent
def all_tools():
    pdf_tool = create_tool()  # Assuming create_tool() is already defined in your vector_query_engine module
    react_system_prompt = PromptTemplate(agentprompt)

    # Initialize the agent
    agent = ReActAgent.from_tools(
        llm=OpenAI("gpt-4o", temperature=0),
        tools=[pdf_tool],
        verbose=False,
    )

    # Update agent prompts
    agent.update_prompts({"agent_worker:system_prompt": react_system_prompt})
    return agent


# Initialize the agent
agent = all_tools()


# Streamlit App
def main():
    st.title("Chatbot Demo")

    # Input field for user query
    user_input = st.text_area("Enter your query:")

    # Button to submit the query
    if st.button("Submit"):
        if user_input:
            # Start the timer
            start = counter()

            # Get the response from the agent
            response = agent.chat(user_input)

            # End the timer
            end = counter()

            # Display the response and time taken
            st.write("Response:")
            st.write(response.response)
            # st.write(f"Time taken: {end - start:.2f} seconds")
        else:
            st.write("Please enter a query.")


# Run the app
if __name__ == "__main__":
    main()
