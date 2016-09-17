[![Opensanca](https://pbs.twimg.com/profile_images/612970307821764609/um0MzITq.jpg)] (http://www.opensanca.com.br/)

#Opensanca - Mão Aberta

[![Build Status](https://travis-ci.org/opensanca/maoaberta.svg?branch=master)](https://travis-ci.org/opensanca/maoaberta)
[![Coverage Status](https://coveralls.io/repos/github/opensanca/maoaberta/badge.svg)](https://coveralls.io/github/opensanca/maoaberta)

Se trata de um projeto social idealizado pelo participantes da Trilha Python, da qual visa consolidar os conhecimentos adquiridos no treinamento visam devolver algo de positivo para a sociedade.
Assim sendo, surgiu o projeto **Mão Aberta**, que visa fornecer uma aplicação web para que Asilos, Orfanatos e Escolas que precisam de ajuda possam ter maior visibilidade e o público possa ajudar conforme viabilidade.

# Como rodar o projeto 

- Download
```
$ git clone https://github.com/opensanca/maoaberta.git
```

- Instalação dos pré-requisitos
```
$ cd maoaberta
$ pip install -r requirements.txt
```
- Configuração do banco de dados
```
$ cd maoaberta
$ python manage.py migrate
```

- Rodando o projeto
```
$ python manage.py runserver
```

- O projeto está rodando, basta acessar no navegador a url [http://127.0.0.1:8000](http://127.0.0.1:8000)


# Como contribuir

Para contribuir com o mão aberta acesse o arquivo [CONTRIBUTING.md](https://github.com/opensanca/maoaberta/blob/master/CONTRIBUTING.md)


### Como funciona a aplicação:

Basicamente as instituições poderão se cadastrar na aplicação, informando dados gerais como:
 - Imagem/Logo
 - Nome Fantasia
 - Endereço
 - Responsável
 - Site/Facebook/Twitter and others...
 - **Lista de Pedidos**
 - Supervisor/Coordenador/Roles

### Como funciona a lista de pedidos:

A lista de pedidos são os itens que faltam para compor a  "cesta" de itens que a insituição necessita, como por exemplo, Orfanato.
  - Fralda
  - Produtos de Limpeza (Sabonete, Sabão, Detergente, Bombril...)
  - Mantimentos (Leite, Chocolate, Bolacha...)

### Como funciona a interação da aplicação com os participantes:
Os participantes deverão ter um login (e-mail/senha ou 0auth) da qual poderão se vincular a uma instituição e ajudar mensalmente, anulamente ou apenas 1x.


##License:
Ver arquivo LICENSE.md

<!-- Projeto de alguma coisa que eu não exatamente o que, mas futuramente saberei -->
