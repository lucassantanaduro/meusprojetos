from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = '''
Responda sempre na lingua portuguesa brasil.

Aqui esta o historico da conversa: {contexto}

Questão: {questao}

Resposta:

'''

modelo = OllamaLLM(model='mistral')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | modelo

def linha_de_conversa():
    contexto = ""
    print("Bem vindo ao Chat com uma IA! Digite 'sair' para fechar a aplicação.")
    while True:
        entrada_usuario = input('Você: ')
        if entrada_usuario.lower() == 'sair':
            break
        resposta = chain.invoke({"contexto": contexto,"questao": entrada_usuario})
        print(f'Bot:',resposta)
        contexto += f'\nUsuario: {entrada_usuario}\nAI: {resposta}'

if __name__ == "__main__":
    linha_de_conversa()