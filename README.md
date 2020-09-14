Car Manager - Gerenciador.

A plataforma foi desenvolvida utilizando o framework Django, Python e como database PostgreSQL.

###Para o funcionamento da plataforma:
 
     Criar um diretório em seu computador com o nome de sua preferência, e executar o comando
     git clone https://github.com/totorodorico/carmanager.git no diretorio criado.
     
     Após o download da plataforma, É necessário executar o comando "sudo docker-compose up --build -d" em seu terminal de comando,
     no raiz do projeto, path de exemplo: DiretorioCriado/carmanager.
     
     Em seguida, executar o comando, "docker-compose run web python manage.py createsuperuser" e cadastrar um usuario de acesso.

###Django Admin
1 - Para o cadastro de proprietários e gerenciamento.:

     Ao acessar a plataforma, é possível cadastrar os proprietários no menu Owner.
     Dados padrões são exigidos, como nome, celular, documento, etc.
     
     A plataforma também possibilita o cadastro dos veículos na mesma tela, assim já vinculando veículo, proprietário.
     Mas se preferir é possível fazer o cadastro do veículo no menu Vehicle na home da plataforma.

2 - Cadastro de veículos:

     No menu Vehicle, é possível cadastrar os veículos e vinculá-lo a 1 (um) proprietário
     Dados padrões são exigidos, como modelo, tipo do veículo, proprietário, etc.


###Django REST Framework
    
1 - Aulocalhosttenticação/Token:
    
    URL: http://localhost:8000/auth
    
    Passar como parametro usuario e senha criados no inicio do processo.
    
    Retono:
    
    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUz...
    }
    
2 - Criar proprietario:
    
    É necessario criar o token anteriormente para executar esse metodo.
    
    URL: http://localhost:8000/create/owner/

    Parametros Exemplo:
    
    {
        "name": "Gustavo",
        "phone_number": "11992901060",
        "email": "teste@teste.com.br",
        "doc_number": "36290644856"
    }
    
    Retorno:
    
    {
        "status_code": 200,
        "message": "Successfully created",
        "result": {
            "name": "Gustavo",
            "phone_number": "11992901060",
            "email": "teste@teste.com.br",
            "doc_number": "36290644856",
            "user": 1
        }
    }
    
3 - Buscar proprietario especifico:
    
    É necessario criar o token anteriormente para executar esse metodo.
    
    Esse metodo é executado utilizando apenas a URL
    
    URL: http://localhost:8000/search/owner/(doc_number do proprietario)
    
    Exemplo: http://localhost:8000/search/owner/36290644856
    
    Retorno:
    [
        {
            "name": "Gustavo",
            "phone_number": "11992901060",
            "email": "teste@teste.com.br",
            "doc_number": "36290644856"
        }
    ]

4 - Listar todos os proprietarios cadastrados pelo usuario:

    É necessario criar o token anteriormente para executar esse metodo.
    
    Esse metodo é executado utilizando apenas a URL:
    
    URL: http://localhost:8000/owner/
    
    Retorno:
    [
        {
            "name": "Gustavo",
            "phone_number": "11992901060",
            "email": "teste@teste.com.br",
            "doc_number": "36290644856"
        }
    ]
    
    
