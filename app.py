import streamlit as st
import ollama

client = ollama.Client()

def main():
    st.set_page_config(page_title="ChatBot Qwen2", layout="centered")
    
    with st.container(border=True):
        st.title("ChatBot Pessoal Offline")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Me pergunte qualquer coisa..."):
            
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            try:
                response_data = client.generate(model="qwen2:latest", prompt=prompt)
                full_response = response_data['response']

                with st.chat_message("assistant"):
                    st.markdown(full_response)
                
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            except Exception as e:
                st.error(f"Erro ao contatar o Ollama: {e}")

if __name__ == "__main__":
    main()