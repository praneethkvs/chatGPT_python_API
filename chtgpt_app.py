import streamlit as st
import os
import openai

API_KEY = YOUR_API_KEY
openai.api_key = API_KEY


# Define the ChatGPT function
def chat_gpt(input_messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.chat
    )
    output_message = response.choices[0].message.content
    return output_message



# Set the Streamlit app title
st.title("My ChatGPT")

# Create an input box for the system message
system_message = st.text_input("System Message",value="You are a Technology expert.")

# Create an input box for the user message
user_message = st.text_input("User Message",value="What is the affect of advanced LLMs on jobs in the technology sector?")


def main():
    
    #initialize list with sessionstate
    if "chat" not in st.session_state:
            st.session_state.chat = []
    
    
    if st.button("Send"):
        
        if len(st.session_state.chat) ==0:
            
            st.session_state.chat.append({"role": "system", "content": system_message})
            st.session_state.chat.append({"role": "user", "content": user_message})
                        
                        
            assistant_message = chat_gpt(st.session_state.chat)
            st.session_state.chat.append({"role": "assistant", "content": assistant_message})
        else:
            st.session_state.chat.append({"role": "user", "content": user_message})
            assistant_message = chat_gpt(st.session_state.chat)
            st.session_state.chat.append({"role": "assistant", "content": assistant_message})
           
        
        conversation_user = st.empty()
        conversation_assistant = st.empty()
        
        
        
        for message in st.session_state.chat:
           if message["role"] == "user":
               conversation_user.write(f"You: {message['content']}")
           elif message["role"] == "assistant":
               conversation_assistant.write(f"Assistant: {message['content']}")
              
    
  
    if st.button("Show Conversation History"):
        st.subheader("Conversation History")
        st.session_state.chat.reverse()
        for message in st.session_state.chat:
            if message["role"] == "user":
                st.text_area("User Input", value=message['content'], height=200, max_chars=None)
            elif message["role"] == "assistant":
                st.text_area("Assistant Response", value=message['content'], height=500, max_chars=None)
    
      
if __name__ == '__main__':
    main()

