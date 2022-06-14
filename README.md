# Projeto 3 - Meet The World
##### Desenvolvido por Lorran Machado, Letícia Coelho e Lídia Alves
###### Frontend disponível [aqui](https://github.com/insper-tecnologias-web/projeto-3-LLL).

O site tem como objetivo o usuário visualizar as notícias em qualquer lugar do mundo, além de ter acesso às músicas mais tocadas em tal local. O usuário pode salvar as notíciais e músicas que mais o interessam, tendo em seu perfil essas informações.

### APIs e bibliotecas utilizadas:
 
- https://react-leaflet.js.org/

- https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/free-news/

- https://www.last.fm/api

- https://developers.deezer.com/api

- https://rapidapi.com/Snowflake107/api/simple-youtube-search/

### Principais features realizadas

- Componente pronto do React - [Modal](https://bestofreactjs.com/repo/Beisenbayev-use-modal-element#) 

- Componente pronto do Recat - [Mapa]( https://react-leaflet.js.org/)

- Frontend utilizando [React](https://pt-br.reactjs.org)

- CRUD feito em Django - [Backend](https://github.com/LidiaDomingos/backend-LLL)

- Autenticação de usuário - [Backend](https://github.com/LidiaDomingos/backend-LLL)

- Interação com busca do youtube para o play de músicas clicadas.


## Instruções de uso 

**Rodando Localmente Backend- Windows**

1. Realizar o clone do repositório.

2. Instalando dependências:


```bash

pip install -r requirements.txt

```

3. Para rodagem do arquivo local, verificar se a variável DEBUG em `getit/settings.py` está com valor True.

4. Criar um container Docker com imagem Postgres. <p> <a href = "https://docs.docker.com/get-docker/"> Baixe o Docker</a> </p>

5. Ative o container no PowerShell ou em um terminal com permissão de administrador. 


```bash

docker run --rm --name pg-docker -e POSTGRES_PASSWORD=[escolhaumasenha] -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

```

6. Por fim, na pasta do projeto clonado rode no terminal o comando abaixo e acesse em um navegador: `http://localhost:8000`

```bash

python manage.py runserver

```

**Acessando projeto via web (Aplicação Heroku)**

1. Apenas clique <a href = "https://serene-bastion-41676.herokuapp.com/">aqui</a>.

@2022, Insper. Quarto Semestre, Engenharia da Computação.
