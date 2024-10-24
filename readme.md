# MINI-TWITTER: (IMPLEMENTAÇÃO DE UMA API REST) 

## RESUMO PRÉVIO
* Uma API para uma plataforma de rede social como exemplo o twitter,construída com Django e Django REST Framework, onde os usuários podem se registrar, criar e curtir postagens, seguir uns aos outros e visualizar um feed paginado das postagens dos usuários que seguem.

## Funcionalidades 
- **Cadastro de Usuários**: Registro de novos usuários.
- **Login com JWT**: Autenticação com tokens de acesso e atualização.
- **Publicação de Postagens**: Criação, listagem e visualização de postagens.
- **Feed Personalizado**: Exibe postagens dos usuários seguidos.
- **Seguir/Deixar de Seguir**: Usuários podem seguir ou deixar de seguir outros.
- **Curtir Postagens**: Curtir ou remover curtidas em publicações.

## Tecnologias Utilizadas 
- **Python 3.8+**
- **Django 4.x**
- **Django REST Framework**
- **Simple JWT (para autenticação com tokens)**


# COMO EXECUTAR O PROJETO 
### PRÉ-REQUESITOS
- Python 3.x instalado
- Virtualenv instalado (opcional, mas recomendado)
+ Banco de dados PostgreSQL configurado
    - Nome do banco: 
    - Usuário: 
    - Senha: 
    - Host: 
    - Porta:

### PASSO A PASSO
Siga os passos abaixo para configurar e executar a aplicação Django.

### 1. Clone o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositoriO 
```
### 2. Crie um Ambiente Virtual
É recomendável criar um ambiente virtual para gerenciar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```
## 3. Instale as Dependências
```bash
pip install -r requirements.txt
```
## 4. Crie o Banco de Dados
Acesse o console do PostgreSQL e crie um novo banco de dados:
```bash
psql -U postgres
CREATE DATABASE mini_twitter;
\q
```
## 5. Configure as Configurações do Banco de Dados
Abra o arquivo settings.py e configure as credenciais do banco de dados:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mini_twitter',
        'USER': 'postgres',  # ou seu_usuario se você criou um novo usuário
        'PASSWORD': '12345', # ou a senha do seu novo usuário
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Claro! Aqui está um passo a passo para criar uma seção "Passo a Passo" no seu README.md, onde você pode incluir as etapas necessárias para configurar e executar a aplicação Django.

Exemplo de Seção "Passo a Passo"
markdown
Copiar código
## Passo a Passo para Configuração da Aplicação

Siga os passos abaixo para configurar e executar a aplicação Django.

### 1. Clone o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```
### 2. Crie um Ambiente Virtual
É recomendável criar um ambiente virtual para gerenciar as dependências do projeto:

```bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```
### 3. Instale as Dependências
Instale as dependências necessárias usando o arquivo requirements.txt:

```bash

pip install -r requirements.txt
```
### 4. Crie o Banco de Dados
Acesse o console do PostgreSQL e crie um novo banco de dados:

```bash

psql -U postgres
CREATE DATABASE mini_twitter;
\q
```
## 5. Configure as Configurações do Banco de Dados
Abra o arquivo settings.py e configure as credenciais do banco de dados:
```bash

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mini_twitter',
        'USER': 'postgres',  # ou seu_usuario se você criou um novo usuário
        'PASSWORD': '12345', # ou a senha do seu novo usuário
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## 6. Aplique as Migrações
Aplique as migrações do Django para criar as tabelas necessárias no banco de dados:
```bash
python manage.py migrate
```

## 7. Execute o Servidor 

```bash
python manage.py migrate
```

## Exemplo de Tabela de Endpoints da API

## Endpoints da API

| Método | Endpoint                     | Descrição                                    |
|--------|------------------------------|----------------------------------------------|
| POST   | /register/                   | Cadastrar um novo usuário                    |
| POST   | /login/                      | Realizar login e obter tokens de acesso      |
| GET    | /feed/                       | Obter o feed de postagens dos usuários seguidos |
| POST   | /follow/<int:user_id>/       | Seguir um usuário                            |
| DELETE | /unfollow/<int:user_id>/     | Deixar de seguir um usuário                  |
| POST   | /posts/                      | Criar uma nova postagem                       |
| GET    | /posts/                      | Listar todas as postagens                    |
| GET    | /posts/<int:post_id>/        | Obter detalhes de uma postagem específica     |
| POST   | /posts/<int:post_id>/like/   | Curtir uma postagem                           |


### EXEMPLOS DE REQUESIÇÕES
#### 1.Registro de Usuários
- **/register/**:  
  - Método: `POST`  
  - Payload:  
    ```json
    {
      "username": "seu_username",
      "email": "seu_email@example.com",
      "password": "sua_senha"
    }
    ```
### 2. Login
- **/login/**:  
  - Método: `POST`  
  - Payload:  
    ```json
    {
      "username": "seu_username",
      "password": "sua_senha"
    }
    ```
### 3. Visualiza feed dos seguidos 
- **/feed/**:  
  - Método: `GET`  
  - Retorna: Uma lista de postagens dos usuários que você está seguindo.
### 4. Seguir
- **/follow/<int:user_id>/**:  
  - Método: `POST`  
  - Descrição: Segue um usuário específico.
### 5. Parar de seguir
- **/unfollow/<int:user_id>/**:  
  - Método: `DELETE`  
  - Descrição: Deixa de seguir um usuário específico.
### 6. Faz uma postagem 
- **/posts/**:  
  - Método: `POST` e `GET`  
  - `POST`: Cria uma nova postagem.  
  - `GET`: Lista todas as postagens.
### 7. Busca publicação específica
- **/posts/<int:post_id>/**:  
  - Método: `GET`  
  - Descrição: Obter detalhes de uma postagem específica.
### 8. Curti uma postagem
- **/posts/<int:post_id>/like/**:  
  - Método: `POST`  
  - Descrição: Curtir uma postagem específica.


## Autenticação
A API utiliza JWT (JSON Web Tokens) para autenticação. Ao fazer login, o usuário receberá dois tokens:

- Access Token: Para acessar endpoints autenticados.
- Refresh Token: Para obter novos access tokens.

### Exemplo de Autenticação
Adicione o token no cabeçalho da requisição:

```BASH
Authorization: Bearer <seu_access_token>
``` 

## Testando no Postman
Siga as instruções abaixo para testar os endpoints da API usando o Postman, vou utilizar o método de registrar um usuário(Onde os outros seguem a mesma lógica):

### Registro de Usuário
- Método: POST
- URL: http://127.0.0.1:8000/register/
- Body (JSON):
```BASH
{
  "username": "novo_usuario",
  "email": "usuario@example.com",
  "password": "123456"
}
```
- Resposta Esperada (201 Created):
json
```bash
{
  "id": 1,
  "username": "novo_usuario",
  "email": "usuario@example.com"
}
```
## Conclusão
Este projeto demonstra a implementação de uma API REST simples para uma plataforma de rede social utilizando Django e Django REST Framework. Esperamos que, ao seguir este guia, você consiga configurar e testar todos os endpoints corretamente.

Sinta-se à vontade para contribuir com sugestões ou melhorias através de Pull Requests no repositório. Qualquer dúvida ou problema encontrado durante a execução, não hesite em abrir uma Issue.

## Contato
Em caso de dúvidas ou sugestões, entre em contato:

E-mail: kennyd3030@gmail.com