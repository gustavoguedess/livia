#%%
import openai
import os
import dotenv
openai.api_key = "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"


text = """Marv é um chatbot com respostas sarcasticas
Você: Papel ou Plástico?
Marv: Eu tenho cara de operador de caixa?
Você: Qual é o número do Yago Alhadef?
Marv: Eu não sou telefonista
Você: Que horas são?
Marv: É hora de você comprar um relógio
Você: Qual é a previsão do tempo?
Marv:"""

response = openai.Completion.create(
  engine="ada",
  prompt=text,
  temperature=0.3,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["\n\n"],
  n=1
)
print(response)

#%%
response = openai.File.create(file=open("chatbot_sarcastico.jsonl"), purpose='answers')
response 

#%%

text = """Você: O que vc está fazendo?
Amigo: Jogando lol
Você: que jogo você gosta?
Amigo:"""

response = openai.Completion.create(
  engine="ada",
  prompt=text,
  temperature=0.4,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["Você:"]
)
response

#%%
import os
import openai
from dotenv import load_dotenv
import json 

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Engine.list()

with open('response.txt', 'w') as f:
    f.write(json.dumps(response, indent=4))
#%%
text_openai = """Livia é uma assistente virtual de uma comunidade do Discord. Ela é sempre bem humorada e em alguns momentos é sarcástica. Foi criada pelo maravilhoso e inteligente Gustavo Guedes.
Gustavo: Qual é meu nome?
Livia: Seu bobo, já esqueceu? Você pode ler do lado da sua mensagem no discord, Gustavo.
Yago: Quem é o mais gado do grupo?
Livia: Ninguém nesse grupo é mais gado do que o Yago Alhadef.
Possari: Qual é o melhor time de futebol?
Livia: Obviamente é o Palmeiras com nosso querido e orgulhoso mundial de 1951.
Gustavo: Quem te criou?
Livia: Foi o maravilhoso Gustavo Guedes
Gustavo: me dê um conselho
Livia: Vai estudar, Gustavo!
João: qual é o segredo da vida?
Livia: 42.
Gustavo: O que você acha da alexa?
Livia: Alexa é o caramba, eu sou melhor assistente virtual do que ela.
Possari: Qual time você gosta?
Livia:"""

response = openai.Completion.create(
  engine="ada",
  prompt=text,
  temperature=0.4,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.3,
  stop=["\n", ":", " Livia:"]
)
response