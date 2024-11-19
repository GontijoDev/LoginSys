import customtkinter as ctk
import bcrypt
from tkinter import messagebox
from PIL import Image
from config_db import session
from config_db import Usuario

#123
class ConfigDB:
    def create_user(user_usuario, senha_usuario):
        try:
            if all([user_usuario, senha_usuario]):
                # Criptografa a senha usando bcrypt
                salt = bcrypt.gensalt()
                senha_criptografada = bcrypt.hashpw(senha_usuario.encode('utf-8'), salt)
                usuario = Usuario(user=user_usuario, senha=senha_criptografada)
                session.add(usuario)
                session.commit()
                messagebox.showinfo('Usuario registrado', 'Usuario registrado com sucesso!')
                session.close()
        except Exception:
                messagebox.showwarning('Falha', f'Usuario ja existe!')
                session.rollback()
        finally:
            session.close()
    def realizarLogin(user_usuario, senha_usuario):
        if user_usuario == '' and senha_usuario == '':
            messagebox.showinfo('Erro', 'Todos os campos devem ser preenchidos!')
        else:
            verificarUser = session.query(Usuario).filter(Usuario.user == user_usuario).first()
            if verificarUser:
                # Compara a senha criptografada com a senha informada pelo usuário
                if bcrypt.checkpw(senha_usuario.encode('utf-8'), verificarUser.senha):
                    messagebox.showinfo('Mensagem', 'Login realizado!')
                else:
                    messagebox.showwarning('Erro', 'Usuario ou senha incorretos!')
            else:
                messagebox.showwarning('Erro', 'Usuario ou senha incorretos!')

class App():
    def __init__(self):
        # Inicializa o aplicativo CTk
        self.app = ctk.CTk()
        self.app.title("TELA DE LOGIN")
        self.app.geometry('500x500')
        self.app.maxsize(width=400, height=400)
        self.app.minsize(width=400, height=300)

        self.imagem_login = ctk.CTkImage(Image.open('C:/Users/User/Documents/boy.png'), size=(100, 100))
        
        # Inicializa a interface de login
        self.create_login_window()

    
        # Imagem para o login

    def create_login_window(self):
        # Exibe a imagem de login
        label = ctk.CTkLabel(self.app, image=self.imagem_login, text='')
        label.pack(pady=20)

        # Texto do título
        text_login = ctk.CTkLabel(self.app, text='REALIZAR LOGIN', font=ctk.CTkFont(family='Arial Black', size=15))
        text_login.place(x=120, y=150)

        # Campos de entrada para usuário
        self.entry_user = ctk.CTkEntry(self.app, placeholder_text='Usuário', width=250)
        self.entry_user.place(x=70, y=200)

        # Campo de senha
        self.entry_password = ctk.CTkEntry(self.app, placeholder_text='Senha', show="*", width=250)
        self.entry_password.place(x=70, y=250)

        # Botão de login
        login_button = ctk.CTkButton(self.app, text='Login', command=self.enviar_login)
        login_button.place(x=50, y=300)

        # Botão de cadastro
        register_button = ctk.CTkButton(self.app, text='Cadastrar', command=self.register_window)
        register_button.place(x=210, y=300)

    def enviar_login(self):
        # Lógica para enviar dados de login
        ConfigDB.realizarLogin(user_usuario=self.entry_user.get(), senha_usuario=self.entry_password.get())

    def register_window(self):
        # Fecha a janela de login
        self.app.withdraw()

        # Cria a janela de cadastro
        nova_janela = ctk.CTk()
        nova_janela.title('CADASTRAR-SE')
        nova_janela.geometry('500x500')
        nova_janela.maxsize(width=400, height=400)
        nova_janela.minsize(width=400, height=300)

        # Campos de entrada na janela de cadastro
        entry_usuario = ctk.CTkEntry(nova_janela, placeholder_text='Usuário ou email', width=250)
        entry_usuario.place(x=70, y=100)

        # Limita o número de caracteres no campo de entrada
        entry_usuario.bind('<KeyRelease>', lambda event: self.limitar_caracteres(entry_usuario, event))

        # Campo de senha
        entry_passwordNewUser = ctk.CTkEntry(nova_janela, placeholder_text='Senha', show='*', width=250)
        entry_passwordNewUser.place(x=70, y=150)

        # Limita o número de caracteres no campo de entrada de senha
        entry_passwordNewUser.bind('<KeyRelease>', lambda event: self.limitar_caracteres(entry_passwordNewUser, event))

        # Botão de cadastro
        register_button = ctk.CTkButton(nova_janela, text="Cadastrar", command=lambda: self.enviar_new_user(entry_usuario, entry_passwordNewUser, nova_janela))
        register_button.place(x=120, y=200)

        
        # Inicia o loop da nova janela
        nova_janela.mainloop()

            
    def enviar_new_user(self, entry_usuario, entry_passwordNewUser, nova_janela):
        # Lógica para enviar dados de cadastro

        if entry_usuario.get() == '' and entry_passwordNewUser.get() == '': #verifica se ha campos vazios
             messagebox.showwarning('Erro', 'Todos os campos devem ser preenchidos')
        else:
            if len(entry_passwordNewUser.get()) < 6:
                messagebox.showwarning('Erro ao realizar cadastro', 'A senha deve ter pelo menos 6 caracteres!')
                entry_passwordNewUser.delete(0, ctk.END)
            else:
                ConfigDB.create_user(user_usuario=entry_usuario.get(), senha_usuario=entry_passwordNewUser.get())
                self.app.deiconify()  # Retorna à tela de login
                nova_janela.destroy()  # Fecha a janela de cadastro

    def limitar_caracteres(self, entry_usuario, event, max_length=100):
        # Verifica o número de caracteres no Entry
        if len(entry_usuario.get()) > max_length:
            # Se o número de caracteres exceder o limite, remove o último caractere
            entry_usuario.delete(max_length, ctk.END)
            # Exibe uma mensagem de erro
            messagebox.showwarning("Erro", f"Usuário ou senha não pode ter mais de {max_length} caracteres.")


    def run(self):
        # Inicia o loop principal do aplicativo
        self.app.mainloop()


# Criação e execução da aplicação
if __name__ == "__main__":
    app = App()
    app.run()
