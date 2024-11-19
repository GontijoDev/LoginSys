# Sistema de Login com Interface Gráfica

Este é um projeto simples de login utilizando Python, a biblioteca `CustomTkinter` para a interface gráfica e `bcrypt` para a criptografia de senhas. O sistema permite o cadastro de novos usuários e a realização de login, utilizando um banco de dados SQLite para armazenar os dados dos usuários.

## Funcionalidades

- **Cadastro de Usuário:** O usuário pode criar uma conta fornecendo um nome de usuário e uma senha. A senha é criptografada com o uso do `bcrypt` antes de ser armazenada no banco de dados.
- **Login:** O sistema permite que o usuário faça login com o nome de usuário e a senha. Se a senha estiver correta, o login é bem-sucedido.
- **Interface Gráfica:** Utiliza o `CustomTkinter`, uma biblioteca para criar interfaces gráficas modernas, combinando o `Tkinter` com componentes customizados.
- **Banco de Dados:** O projeto utiliza o SQLite para persistir os dados dos usuários, armazenando seus nomes e senhas criptografadas.

## Requisitos

Antes de executar o projeto, certifique-se de ter o Python instalado e as seguintes bibliotecas:

- customtkinter
- bcrypt
- Pillow
- SQLAlchemy

Você pode instalar todas as dependências necessárias com o seguinte comando:

pip install -r requirements.txt

Bom uso :D
