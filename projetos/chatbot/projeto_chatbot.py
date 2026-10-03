# Bom, nesse projeto vou tentar me aprofundar em duas bibliotecas openai e stremlit
# Titulo do chat
    # input da pergunta da pessoa
    # respotas iterativa do chat
    # modelo de ai do gemini
    
# algumas funções do streamlit
    # st.write() → escreve texto na tela
    # st.button() → cria um botão
    # st.input() -> cria uma pergunta para o chat
    # streamlit run main.py
import streamlit as st
from openai import OpenAI

st.write("# Chat bot com IA") # criando o titulo do chat bot; # criando a caixa de pergunta do usuario;

modelo_ia = OpenAI(api_key = st.secrets["GEMINI_API_KEY"], # chave do chat
                base_url="https://generativelanguage.googleapis.com/v1beta/openai") # link do gemini para openai

# session_state ->  armazenamento da sessão do usuário
if not "lista_de_mensagens" in st.session_state:
    st.session_state["lista_de_mensagens"] = []

texto_usuario = st.chat_input("Digite uma mensagem: ")

for mensagem in st.session_state["lista_de_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    print(texto_usuario)
    # st.chat.message("user") para definir quem esta falando.write() para mostrar a mensagem
    st.chat_message("user").write(texto_usuario)
    # role -> papel | content -> conteudo
    mensagem_user = {"role": "user", "content": texto_usuario}
    st.session_state["lista_de_mensagens"].append(mensagem_user)


    resposta_modelo = modelo_ia.chat.completions.create( # criar uma resposta, pra completar o chat que ta recebendo
        messages=st.session_state["lista_de_mensagens"],
        model="gemini-flash-lite-latest"
    )

    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)
    # role -> papel | content -> conteudo
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_de_mensagens"].append(mensagem_ia)

    

print(st.session_state["lista_de_mensagens"])
