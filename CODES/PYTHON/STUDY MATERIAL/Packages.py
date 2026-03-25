import math           # Operações matemáticas
import random         # Geração de números aleatórios
import datetime       # Datas e horários
import os             # Operações com o sistema operacional
import sys            # Parâmetros e funções do sistema
import json           # Manipulação de JSON
import re             # Expressões regulares
import statistics     # Estatísticas básicas
import collections    # Tipos de dados avançados
import requests       # Requisições HTTP (precisa instalar: pip install requests)
  
# 1. math — Operações matemáticas avançadas
# Fornece funções matemáticas como seno, cosseno, logaritmo, potência, raiz, etc.
print("[math] Raiz quadrada de 16:", math.sqrt(16))
print("[math] Seno de 90 graus:", math.sin(math.radians(90)))
print("[math] Logaritmo natural de 10:", math.log(10))

# 2. random — Geração de números aleatórios
# Permite gerar números aleatórios, embaralhar listas, escolher elementos aleatórios, etc.
print("[random] Número aleatório entre 1 e 10:", random.randint(1, 10))
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print("[random] Lista embaralhada:", lista)
print("[random] Escolha aleatória da lista:", random.choice(lista))

# 3. datetime — Datas e horários
# Manipula datas, horas, intervalos de tempo, formatação e cálculos com datas.
agora = datetime.datetime.now()
print("[datetime] Data e hora atual:", agora)
ontem = agora - datetime.timedelta(days=1)
print("[datetime] Ontem foi:", ontem.strftime('%d/%m/%Y'))
data_nasc = datetime.datetime(2000, 5, 15)
idade = (agora - data_nasc).days // 365
print(f"[datetime] Idade aproximada de quem nasceu em 15/05/2000: {idade} anos")

# 4. os — Interação com o sistema operacional
# Permite acessar arquivos, diretórios, variáveis de ambiente, executar comandos do sistema, etc.
print("[os] Diretório atual:", os.getcwd())
print("[os] Listando arquivos do diretório atual:", os.listdir('.'))
print("[os] Nome do sistema operacional:", os.name)

# 5. sys — Parâmetros e funções do sistema
# Permite acessar informações do interpretador, argumentos de linha de comando, manipular saída, etc.
print("[sys] Versão do Python:", sys.version)
print("[sys] Caminho dos módulos:", sys.path)
print("[sys] Nome do script em execução:", sys.argv[0])

# 6. json — Manipulação de dados em formato JSON
# Permite converter dicionários para JSON e vice-versa, útil para APIs e arquivos de configuração.
dicionario = {"nome": "Ana", "idade": 25}
json_str = json.dumps(dicionario)
print("[json] Dicionário para JSON:", json_str)
novo_dic = json.loads(json_str)
print("[json] JSON para dicionário:", novo_dic)

# 7. re — Expressões regulares
# Permite buscar, validar e manipular padrões em textos, como e-mails, telefones, etc.
texto = "Meu e-mail é exemplo@email.com e outro@email.com"
emails = re.findall(r'\S+@\S+', texto)
print("[re] E-mails encontrados:", emails)))

# 8. statistics — Estatísticas básicas
telefone = re.search(r'\d{4,5}-\d{4}', 'Ligue para 99999-1234')
if telefone:
	print("[re] Telefone encontrado:", telefone.group(
# Calcula média, mediana, moda, variância, desvio padrão, etc.
dados = [10, 20, 20, 40]
print("[statistics] Média dos dados:", statistics.mean(dados))
print("[statistics] Mediana dos dados:", statistics.median(dados))
print("[statistics] Moda dos dados:", statistics.mode(dados))

# 9. collections — Tipos de dados avançados
# Fornece estruturas como namedtuple, deque, Counter, OrderedDict, defaultdict, etc.
contagem = collections.Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print("[collections] Contagem de elementos:", contagem)
Deque = collections.deque([1, 2, 3])
Deque.appendleft(0)
print("[collections] Deque com appendleft:", Deque)
Pessoa = collections.namedtuple('Pessoa', 'nome idade')
p = Pessoa('Lucas', 22)
print("[collections] NamedTuple Pessoa:", p)

# 10. requests — Requisições HTTP
# Permite fazer requisições para APIs, baixar dados da internet, enviar formulários, etc.
# (Necessário instalar: pip install requests)
resposta = requests.get("https://api.github.com")
print("[requests] Status da requisição HTTP:", resposta.status_code)
print("[requests] Cabeçalhos da resposta:", resposta.headers)
print("[requests] Parte do conteúdo da resposta:", resposta.text[:60], "...")
dados = [10, 20, 20, 40]
print("Média dos dados:", statistics.mean(dados))

# 9. collections
contagem = collections.Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print("Contagem de elementos:", contagem)

# 10. requests
resposta = requests.get("https://api.github.com")
print("Status da requisição HTTP:", resposta.status_code)
