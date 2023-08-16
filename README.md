# Boas-vindas!
<details>
<summary>🧑‍💻 O que foi desenvolvido</summary>

- Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side. Ou seja, o Backend irá fornecer a camada View, para a pessoa usuária.

</details>

<details>
  <summary>📝 Habilidades trabalhadas </summary>

- Implementar uma API utilizando arquitetura em camadas MVC;
- Utilizar o Docker para projetos Python;
- Aplicar conhecimentos de Orientação a Objetos no desenvolvimento WEB.
- Escrever testes para APIs para garantir a implementação dos endpoints;
- Interagir com um banco de dados não relacional MongoDB;
- Desenvolver páginas web Server Side.

</details>

## Preparando Ambiente

<details>

<summary>🐳 Subindo a aplicação</summary>
Lembre-se de que, para executar esse processo em sua máquina, você precisará ter o Docker instalado e configurado corretamente, além de ter o Python (versão 3.x) instalado para configurar o ambiente virtual e instalar as dependências.
**[1]** Crie o ambiente virtual para o projeto

```bash
python3 -m venv .venv && source .venv/bin/activate
```

**[2]** Instale as dependências

```bash
python3 -m pip install -r dev-requirements.txt
```

**[3 - Opção A]** Suba o projeto pelo Docker

```bash
docker compose up translate
```

- Recomendado: Dockerfile e Docker-compose já estão prontos para uso, para subir o MongoDB e o Flask.

**[3 - Opção B]** Caso queira subir somente o banco MongoDB pelo Docker

```bash
docker compose up -d mongodb

python3 src/app.py
```

**[4]** Podemos já acessar a aplicação pelo navegador na rota <http://127.0.0.1:8000/> .

</details>

Obrigado pela visita 🙂 !
