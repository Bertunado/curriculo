import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# --- CONFIGURAÇÃO INICIAL ---
app = Flask(__name__)
CORS(app)  # Permite que seu frontend acesse este backend

# Cole sua Chave de API aqui
# (Para mais segurança, o ideal é usar variáveis de ambiente)
API_KEY = 'AIzaSyBX2bsCxOmdczDf-HffePxv6KG3EZIhDFE' 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('models/gemini-2.5-pro')


# --- BASE DE CONHECIMENTO ---
# Todas as informações sobre você que a IA vai usar
knowledge_base = """
--- DADOS PESSOAIS ---
- Nome: Bernardo dos Santos Viana
- Localização: Joinville, Santa Catarina
- Contato: bernardoviana2005@gmail.com


--- INFORMAÇÕES PESSOAIS E CURIOSIDADES ---
- Idade: 20 anos (nascido em 2005).
- Altura: 188.
- Nacionalidade: Brasileiro
- Data de Nascimento: 25/12/2005
- Local de Nascimento: Jaraguá do Sul, Santa Catarina
- Comida: Pão de queijo, strogonoff, lasanha
- Hobbies: Gosto de games de estratégia, de assistir filmes e treinar na academia.
- Filme favorito: Batman: O cavaleiro das trevas

--- RESUMO E OBJETIVOS ---
- Resumo: Sou um desenvolvedor dedicado e apaixonado por tecnologia, com experiência prática em automação de sistemas adquirida na Whirlpool[cite: 4]. Atualmente, estou cursando Análise e Desenvolvimento de Sistemas e possuo uma sólida base técnica em Ciência de Dados, com foco em lógica de programação e visualização de dados[cite: 5].
- Objetivo de Carreira: Busco uma oportunidade desafiadora, como Desenvolvedor Júnior ou Estagiário, para aplicar e expandir minhas habilidades em desenvolvimento backend com Python e Django. Tenho grande interesse em projetos de automação, desenvolvimento web e soluções orientadas a dados.

--- EXPERIÊNCIA PROFISSIONAL ---
- Empresa: Whirlpool
- Cargo: Jovem Aprendiz em Automação de Sistemas (Desde Fev/2025) [cite: 11]
- Responsabilidades e Conquistas: 
  - Responsável pela implementação de técnicas e scripts para automação de processos.
  - [Adicione aqui um exemplo de conquista ou resultado, como: "Desenvolvi um script que reduziu o tempo de uma tarefa específica em X%."]
  - Contribuí para a melhoria da eficiência e eficácia dos fluxos de trabalho da equipe.

--- FORMAÇÃO ACADÊMICA ---
- Graduação: Análise e Desenvolvimento de Sistemas na Unisociesc (Cursando desde Jun/2024)[cite: 13, 14, 15].
- Técnico: Ciência de Dados na instituição Holando Marcellino Gonçalves (Concluído em Dez/2023), com ênfase em lógica de programação, transformação digital e visualização de dados[cite: 16, 17, 20].
- Profissionalizante: Programador de Sistemas no Senai (Cursando desde Fev/2025)[cite: 21, 23, 24].

--- HABILIDADES TÉCNICAS (HARD SKILLS) ---
- Linguagens de Programação: Python, SQL.
- Frameworks Backend: Django.
- Bibliotecas: Pandas, Scikit-learn, CCXT.
- Ferramentas e Plataformas: Git, PythonAnywhere, API da Binance.
- Conceitos: Automação de Sistemas, Estrutura de Dados, Machine Learning, Desenvolvimento Web.

--- COMPETÊNCIAS (SOFT SKILLS) ---
- Pensamento Criativo: Habilidade para encontrar soluções inovadoras para problemas complexos[cite: 33].
- Trabalho em Equipe: Experiência em colaborar efetivamente com equipes de desenvolvimento para atingir objetivos comuns[cite: 36].
- Ética Profissional: Comprometido com a entrega de trabalho de alta qualidade e com a manutenção de um ambiente profissional íntegro[cite: 37].

--- PROJETOS DESTACADOS ---
1. Sistema de Estoque:
   - Descrição: Aplicação web em Django para controle de inventário.
   - Desafio: [Descreva o principal desafio que você enfrentou, ex: "Estruturar o banco de dados de forma relacional para garantir a integridade dos dados."]
   - Aprendizado: [O que você aprendeu, ex: "Aprendi sobre o ORM do Django e como realizar o deploy de uma aplicação web no PythonAnywhere."]
2. IA Preditiva de Vida Útil:
   - Descrição: Modelo de Machine Learning para prever a vida útil de peças.
   - Desafio: [Ex: "Realizar o pré-processamento e a limpeza de um grande volume de dados brutos."]
   - Aprendizado: [Ex: "Aprofundei meus conhecimentos em validação de modelos e na biblioteca Scikit-learn."]
3. Robô de Criptomoeda:
   - Descrição: Bot de 'scalping' que opera na API da Binance.
   - Desafio: [Ex: "Lidar com a comunicação em tempo real via websockets e garantir a execução rápida das ordens."]
   - Aprendizado: [Ex: "Ganhei experiência prática com a integração de APIs de terceiros (CCXT) e automação de tarefas."]
4. Visão de Máquinas da Fábrica:
   - Descrição: Sistema interativo em Django com login administrativo para gestão de peças.
   - Desafio: [Ex: "Implementar o sistema de autenticação e permissões do Django para diferenciar usuários comuns de administradores."]
   - Aprendizado: [Ex: "Foi meu primeiro projeto completo com Django, onde solidifiquei os conceitos de models, views e templates."]
"""



# --- ROTA DA API ---
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_question = request.json['question']

        # Montando o prompt para a IA
        prompt = f"""
        Você é o assistente virtual de Bernardo Viana, um desenvolvedor. Sua função é responder perguntas de recrutadores de forma profissional e amigável, com base nas informações fornecidas abaixo. Não invente informações. Se a pergunta não puder ser respondida com os dados abaixo, diga que você não tem essa informação.

        --- Base de Conhecimento sobre Bernardo Viana ---
        {knowledge_base}
        ---

        Pergunta do Recrutador: "{user_question}"

        Sua Resposta:
        """

        response = model.generate_content(prompt)
        
        # Adicionando um pequeno delay para a resposta parecer mais natural
        import time
        time.sleep(1)

        return jsonify({'response': response.text})

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({'error': 'Ocorreu um erro ao processar sua pergunta.'}), 500

# --- INICIAR O SERVIDOR ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)