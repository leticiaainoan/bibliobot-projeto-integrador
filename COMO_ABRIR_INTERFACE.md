# Interface visual do agente BiblioBot (Streamlit)

Na pasta do projeto, no terminal integrado do VS Code (Mac), ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Instale a biblioteca de interface:

```bash
python -m pip install -r requirements.txt
```

Inicie o aplicativo:

```bash
python -m streamlit run app_biblioteca.py
```

Abra o endereço local que aparecer no terminal (geralmente `http://localhost:8501`). Para encerrar, pressione `Ctrl + C` no terminal.

O código usa `agente_biblioteca.py` como motor de respostas. Não é um LLM, não acessa a internet e utiliza somente informações fictícias. A conversa permanece na sessão do aplicativo e pode ser limpa na barra lateral.
