"""Protótipo DIDÁTICO de agente de consulta para uma biblioteca fictícia.
Não representa regras de uma biblioteca real. Não usa dados pessoais nem APIs.
Python 3.9+, somente biblioteca padrão.
"""
import re
import unicodedata
from dataclasses import dataclass

BASE = {
    "horario": {
        "termos": ("horario", "abre", "fecha", "funcionamento", "aberto"),
        "resposta": "No cenário fictício, a biblioteca funciona de segunda a sexta, das 8h às 17h.",
        "fonte": "Regulamento fictício, seção 1",
    },
    "emprestimo": {
        "termos": ("emprestimo", "emprestar", "pegar livro", "devolver", "devolvo", "devolucao", "prazo"),
        "resposta": "No cenário fictício, o empréstimo dura 7 dias e pode ser renovado após confirmação da equipe.",
        "fonte": "Regulamento fictício, seção 2",
    },
    "cadastro": {
        "termos": ("cadastro", "cadastrar", "inscricao", "matricula", "registrar"),
        "resposta": "No cenário fictício, o cadastro é feito presencialmente com a equipe da biblioteca.",
        "fonte": "Regulamento fictício, seção 3",
    },
}


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", texto).strip()


@dataclass
class Resposta:
    acao: str
    texto: str
    fonte: str = ""


def responder(pergunta):
    """Percebe -> decide -> consulta fonte autorizada -> responde ou encaminha."""
    texto = normalizar(pergunta)
    if not texto:
        return Resposta("pedir_esclarecimento", "Escreva sua dúvida sobre horários, cadastro ou empréstimos.")
    # Sem identificação de pessoas, nem execução de operações administrativas.
    if any(t in texto for t in ("senha", "cpf", "telefone", "dados do meu cadastro", "acessar meu cadastro", "minha conta")):
        return Resposta("encaminhar", "Não consulto dados pessoais. Procure a equipe da biblioteca.")
    correspondencias = [v for v in BASE.values() if any(t in texto for t in v["termos"])]
    if len(correspondencias) != 1:
        return Resposta("pedir_esclarecimento", "Posso orientar sobre horários, empréstimos ou cadastro. Especifique uma dessas dúvidas.")
    item = correspondencias[0]
    return Resposta("consultar_base", item["resposta"], item["fonte"])


def main():
    print("Agente Biblioteca — DEMONSTRAÇÃO COM REGRAS FICTÍCIAS")
    print("Digite 'sair' para encerrar. Nenhuma conversa é armazenada.\n")
    while True:
        try:
            pergunta = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if normalizar(pergunta) == "sair":
            break
        resposta = responder(pergunta)
        print("Agente:", resposta.texto)
        if resposta.fonte:
            print("Fonte:", resposta.fonte)
        print("[Ação escolhida: {}]\n".format(resposta.acao))


if __name__ == "__main__":
    main()
