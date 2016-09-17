Contribuindo para o Mão Aberta
============================

Mão aberta é um projeto open source. Você pode colaborar de diversas maneiras:

- Código (pull requests) e revisões
- Melhorias na documentação
- Report de bugs (via [Github Issues](https://github.com/opensanca/maoaberta/issues))
- Novas features


Pedindo ajuda
---------------

Você pode pedir ajuda participando do [slack do opensanca](https://slack-opensanca.herokuapp.com/).
Participe do canal **#maoaberta**, tire suas dúvidas sobre o projeto e troque idéias com outros colaboradores :) 


Como configurar o Git
----------------

O `django contributing docs` tem um simples e intuitivo [tutorial](https://docs.djangoproject.com/pt-br/1.9/internals/contributing/writing-code/working-with-git/)
explicando como instalar e configurar o seu git para colaborar com projetos e também ensina como criar um repositório local integrado com o github.


Como rodar o mão aberta para desenvolvimento
---------------------------------------

- Fork o projeto para o seu usuário do github:
  
  Clique no botão **Fork** localizado nesta página. Caso encontre problemas [clique aqui](http://tableless.com.br/contribuindo-em-projetos-open-source-com-o-github/) para mais informações.

- Clone o projeto mao aberta:
  
```
$ git clone https://github.com/<seu_usuario_github>/maoaberta.git
``` 
  
- (opcional) Crie um ambiente virtual:

```
$ python -m venv env
$ source env/bin/activate
```

- Instale os pré-requisitos:

```
$ cd maoaberta
$ (env) pip install -r requirements/local.txt
```

- Execute as migrações:
  
```
$ python manage.py migrate
```

- Rode o servidor.

```
$ cd maoaberta
$ python manage.py runserver
```

Fim :-)

Estilo de Código
------------

Seguimos as definições da [PEP8](https://www.python.org/dev/peps/pep-0008/) no desenvolvimento do código.
