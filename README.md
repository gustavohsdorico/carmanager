Car Manager - Gerenciador.

A plataforma foi desenvolvida utilizando o framework Django, Python e como database PostgreSQL.

1 - Para o funcionamento da plataforma:
 
     Criar um diretório em seu computador com o nome de sua preferência, e executar o comando
     git clone https://github.com/totorodorico/carmanager.git no diretorio criado.
     
     Após o download da plataforma, É necessário executar o comando "sudo docker-compose up --build -d" em seu terminal de comando,
     no raiz do projeto, path de exemplo: DiretorioCriado/carmanager.
     
     Em seguida, executar o comando, "docker-compose run web python manage.py createsuperuser" e cadastra um usuario de acesso.

2 - Criação do Token para poder executar a funções desejadas.
    
    utilizar a rota auth/ utilizando o metodo POST.
    e utilizando como argumento o seguinte JSON:
    
    {
        "username": "usuario criado"
        "password": "senha criada"
    }
    
    E como retorno um "token" é gerado, que será necessarios nas demais operações

3 - Para o cadastro de proprietários e gerenciamento.:

     Ao acessar a plataforma, é possível cadastrar os proprietários no menu Owner.
     Dados padrões são exigidos, como nome, celular, documento, etc.
     
     A plataforma também possibilita o cadastro dos veículos na mesma tela, assim já vinculando veículo, proprietário.
     Mas se preferir é possível fazer o cadastro do veículo no menu Vehicle na home da plataforma.

4 - Cadastro de veículos:

     No menu Vehicle, é possível cadastrar os veículos e vinculá-lo a 1 (um) proprietário
     Dados padrões são exigidos, como modelo, tipo do veículo, proprietário, etc.
