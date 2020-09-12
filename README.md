Car Manager - Gerenciador.

A plataforma foi desenvolvida utilizando o framework Django, Python e como database PostgreSQL.

1 - Para o funcionamento da plataforma:
 
     Criar um diretório em seu computador com o nome de sua preferência, e executar o comando
     git clone https://github.com/totorodorico/carmanager.git no diretorio criado.
     
     Após o download da plataforma, É necessário executar o comando "sudo docker-compose up" em seu terminal de comando,
     no raiz do projeto, path de exemplo: DiretorioCriado/carmanager.
     
     E como acesso padrão a plataforma é disponibilizada na url: http://127.0.0.1:8000/admin/

2 - A plataforma exige uma autenticação de usuário:

     user: admin
     password: admin

3 - Para o cadastro de proprietários:

     Ao acessar a plataforma, é possível cadastrar os proprietários no menu Owner.
     Dados padrões são exigidos, como nome, celular, documento, etc.
     
     A plataforma também possibilita o cadastro dos veículos na mesma tela, assim já vinculando veículo, proprietário.
     Mas se preferir é possível fazer o cadastro do veículo no menu Vehicle na home da plataforma.

4 - Cadastro de veículos:

     No menu Vehicle, é possível cadastrar os veículos e vinculá-lo a 1 (um) proprietário
     Dados padrões são exigidos, como modelo, tipo do veículo, proprietário, etc.
 

5 - Busca de veículos ou proprietários:

     Ao acessar qualquer menu do car manager, é possível fazer busca por itens utilizando as barras de search localizadas
     no topo da lista.