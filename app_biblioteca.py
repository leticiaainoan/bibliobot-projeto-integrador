"""Interface visual Streamlit do agente didático da biblioteca fictícia.
Execute: python -m streamlit run app_biblioteca.py
"""
import streamlit as st
from agente_biblioteca import responder

st.set_page_config(page_title="BiblioBot | Assistente da Biblioteca", page_icon="📚", layout="centered")

st.markdown("""
<style>
.stApp { background: #f6f8fc; color: #142338; }
.block-container { max-width: 900px; padding-top: 2.3rem; padding-bottom: 3rem; }
.hero { padding: 1.8rem 2rem; border-radius: 22px; background: linear-gradient(112deg,#16325f,#3158a3 65%,#6b67c5); color: white; margin-bottom: 1.2rem; box-shadow: 0 12px 28px rgba(20,48,90,.13); }
.hero h1 { color: white; font-size: 2.25rem; margin: 0 0 .35rem 0; }
.hero p { margin: 0; font-size: 1.01rem; opacity:.95; }
.eyebrow { font-size:.78rem; text-transform:uppercase; letter-spacing: .09em; font-weight:700; opacity:.85; margin-bottom:.7rem; }
.note {background: #eaf0fa; border-left: 4px solid #4268bc; padding: .72rem 1rem; border-radius: 8px; font-size:.9rem; margin:.6rem 0 1.3rem; color:#213957;}
.stButton > button { border-radius: 12px; min-height: 2.7rem; border-color:#d6e0f1; background:white; color:#204273; font-weight: 600; }
[data-testid="stChatMessage"] { border:1px solid #e5ebf6; border-radius: 16px; background:white; }
[data-testid="stSidebar"] {background: #edf2fa;}
/* Fundo da barra lateral */
[data-testid="stSidebar"] {
    background-color: #EAF0F8 !important;
    border-right: 1px solid #CBD5E1;
}

/* Cor dos textos da barra lateral */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] small {
    color: #183153 !important;
}

/* Botão limpar conversa */
[data-testid="stSidebar"] button {
    background-color: #FFFFFF !important;
    color: #183153 !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 10px !important;
}

/* Texto do botão */
[data-testid="stSidebar"] button * {
    color: #183153 !important;
}

/* Efeito ao passar o mouse */
[data-testid="stSidebar"] button:hover {
    background-color: #DCE8F8 !important;
    border-color: #3B65A7 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('''<div class="hero"><div class="eyebrow">Projeto Integrador III · Demonstração didática</div><h1>📚 BiblioBot</h1><p>Seu assistente virtual para informações da biblioteca.</p></div>''', unsafe_allow_html=True)
st.markdown('<div class="note">ℹ️ <b>Ambiente demonstrativo:</b> horários, regras e biblioteca são fictícios. Este protótipo é baseado em regras, não utiliza LLM nem consulta dados pessoais.</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("📖 Sobre o projeto")
    st.write("**Objetivo:** orientar consultas sobre horário, empréstimo e cadastro.")
    st.write("**Método:** percepção da pergunta → identificação por regras → consulta à base → resposta ou encaminhamento.")
    st.write("**Fontes:** regulamento fictício, seções 1–3.")
    st.divider()
    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()
    st.caption("Não insira nomes completos, CPF, senhas ou informações pessoais.")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

st.subheader("Como posso ajudar?")
st.caption("Escolha uma pergunta rápida ou escreva sua dúvida abaixo.")

perguntas = [
    "Qual é o horário de funcionamento?",
    "Em quantos dias devo devolver um livro?",
    "Como faço meu cadastro?",
    "Qual é a senha da minha conta?",
]
cols = st.columns(2)
pergunta_rapida = None
for i, pergunta in enumerate(perguntas):
    with cols[i % 2]:
        if st.button(pergunta, key=f"pergunta_{i}", use_container_width=True):
            pergunta_rapida = pergunta

for msg in st.session_state.mensagens:
    with st.chat_message(msg["papel"], avatar="📚" if msg["papel"] == "assistant" else "👤"):
        st.write(msg["conteudo"])
        if msg.get("fonte"):
            st.caption("📄 Fonte: " + msg["fonte"])
        if msg.get("acao"):
            st.caption("Ação: " + msg["acao"])

entrada = st.chat_input("Digite sua dúvida sobre a biblioteca...")
pergunta_atual = pergunta_rapida or entrada
if pergunta_atual:
    st.session_state.mensagens.append({"papel": "user", "conteudo": pergunta_atual})
    resultado = responder(pergunta_atual)
    st.session_state.mensagens.append({
        "papel": "assistant", "conteudo": resultado.texto,
        "fonte": resultado.fonte, "acao": resultado.acao,
    })
    st.rerun()

st.divider()
st.caption("Projeto demonstrativo para ensino de agentes baseados em regras. A validação extensionista exige parceria real, testes e documentação da entrega.")
