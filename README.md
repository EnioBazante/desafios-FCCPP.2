```markdown
# README - Projeto de Dados com Microsserviços

## Introdução

Este projeto mostra a evolução de uma aplicação que simula rolagem de dados, começando com uma API simples e evoluindo para uma arquitetura distribuída com múltiplos serviços se comunicando.

---

## Desafio 1: API Básica

### Arquitetura

```
Cliente  ------>  Servidor
         <------
```

O cliente faz requisições HTTP para o servidor, que responde com números aleatórios.

### Componentes

**server.py**

Este arquivo cria uma API com dois endpoints:

- `/random_d6` - retorna um número aleatório de 1 a 6
- `/random_d/{x}` - retorna um número aleatório de 6 a x

O servidor usa FastAPI para criar esses endpoints. Quando alguém acessa a URL, a função `random.randint()` gera um número aleatório e retorna em formato JSON.

Problema encontrado: o segundo endpoint deveria retornar de 1 a x, não de 6 a x.

**client.py**

Este arquivo testa o servidor. Ele:

1. Espera 15 segundos para o servidor iniciar
2. Entra em loop infinito fazendo requisições
3. Testa o dado de 6 lados
4. Testa dados de 6, 10 e 20 lados
5. Aguarda 5 segundos e repete

O `sys.stdout.reconfigure(line_buffering=True)` e `flush=True` garantem que as mensagens apareçam imediatamente no terminal, sem esperar o buffer encher.

---

## Desafio 2: Adicionando Banco de Dados

### Arquitetura

```
Cliente  ------>  Servidor  ------>  Banco de Dados
         <------            <------
```

Agora o servidor não apenas gera números, mas também salva cada resultado em um banco de dados.

### Componentes

**server.py**

Três funções principais:

1. `init_db()` - cria a tabela no banco se ela não existir
2. `save_roll()` - insere um novo resultado na tabela
3. Endpoints modificados - agora chamam `save_roll()` antes de retornar

A tabela tem duas colunas:
- `dice` - tipo do dado (ex: "d6", "d20")
- `result` - resultado da rolagem

Cada vez que alguém rola um dado, o resultado é salvo no SQLite localizado em `/app/data/dice.db`.

**client.py**

Mesma lógica do Desafio 1, mas sem o sleep inicial de 15 segundos.

---

## Desafio 3: Separação em Microsserviços

### Arquitetura

```
Cliente  ------>  Middleware  ------>  Database Service
         <------              <------           |
                                                v
                                          SQLite DB
```

A aplicação agora está dividida em dois serviços independentes:
- Middleware: gera os números aleatórios
- Database: cuida apenas de salvar no banco


**middleware.py**

Responsável pela lógica de negócio:
- Recebe requisição do cliente
- Gera número aleatório
- Retorna resposta


**database.py**

Responsável apenas por persistência:
- Recebe dados via POST no endpoint `/save`
- Salva no SQLite
- Retorna confirmação


**client.py**

Agora aponta para `middleware:8000` em vez de `server:8000`. Tem um sleep de 5 segundos no início.



## Desafio 4: Comunicação Recursiva

### Arquitetura

```
Cliente
   |
   v
Service A  <------>  Service B
   |                    |
   v                    v
Chama B              Chama A
```

Dois serviços que se chamam mutuamente até atingir um limite.

### Componentes

**service_a.py e service_b.py**

Ambos têm a mesma lógica, apenas trocam qual serviço chamam:

1. Recebe requisição com número de lados e profundidade
2. Valida se o número está entre 2 e 9999
3. Se profundidade >= 5, para a recursão
4. Gera número aleatório
5. Chama o outro serviço com esse número como novo dado
6. Retorna resposta aninhada

### Fluxo de Execução

Exemplo: Cliente chama Service A com dado de 20 lados

```
1. Service A rola d20, resultado = 15
2. Service A chama Service B com d15
3. Service B rola d15, resultado = 8
4. Service B chama Service A com d8
5. Service A rola d8, resultado = 3
6. Service A chama Service B com d3
7. Service B rola d3, resultado = 2
8. Service B chama Service A com d2
9. Service A rola d2, resultado = 1
10. Service A chama Service B com d1
para
```

### Estrutura da Resposta

```json
{
  "service": "A",
  "dice_sides": 20,
  "next": {
    "service": "B",
    "dice_sides": 15,
    "next": {
      "service": "A",
      "dice_sides": 8
    }
  }
}
```


## Como Executar

Cada desafio possui seus próprios arquivos e configuração Docker. Para executar:

1. Navegue até a pasta do desafio desejado
2. Execute `docker-compose up` para iniciar os containers

---

## Tecnologias Utilizadas

- Python 3.x
- FastAPI - Framework web para criar APIs
- SQLite - Banco de dados relacional
- Requests - Biblioteca para fazer requisições HTTP
- Docker - Containerização dos serviços

---

## Estrutura de Arquivos

```
DESAFIOS/
│
├── desafio_1/
│   ├── client/
│   │   ├── client.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── server/
│   │   ├── server.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── docker-compose.yml
│
├── desafio_2/
│   ├── client/
│   │   ├── client.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── server/
│   │   ├── server.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── docker-compose.yml
│
├── desafio_3/
│   ├── client/
│   │   └── (arquivos do cliente)
│   │
│   ├── database/
│   │   └── (arquivos do serviço de banco)
│   │
│   ├── middleware/
│   │   └── (arquivos do middleware)
│   │
│   ├── docker-compose.yml
│   └── requirements.txt
│
├── desafio_4/
│   ├── service_a/
│   │   ├── service_a.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── service_b/
│   │   ├── service_b.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   └── docker-compose.yml
│
└── desafio_5/
├── client/
│   ├── client.py
│   └── Dockerfile
│
├── gateway/
│   ├── main.py
│   └── Dockerfile
│
├── order_service/
│   ├── main.py
│   └── Dockerfile
│
├── user_service/
│   ├── main.py
│   └── Dockerfile
│
├── docker-compose.yml
└── requirements.txt


```

---

Autor: Ênio Matheus
Data: Dezembro 2025
```