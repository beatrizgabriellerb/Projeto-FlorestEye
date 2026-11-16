import re
import bcrypt

class User:
    def __init__(self, nome: str, email: str, senha: str, is_admin=0):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.is_admin = is_admin

    @staticmethod
    def create_user(nome: str, email: str, senha: str):
        validated_name = User.validate_name(nome)
        validated_email = User.validate_email(email)
        validated_senha = User.validate_password(senha)
        senha_cpriptografada = bcrypt.hashpw(validated_senha.encode(), bcrypt.gensalt()).decode()
    
        return User(validated_name, validated_email, senha_cpriptografada)

    @staticmethod
    def validate_name(nome):
        if not nome or len(nome) < 3:
            raise ValueError("O nome deve ter no mínimo 3 caracteres")
        return nome

    @staticmethod
    def validate_email(email):
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
        if not re.match(padrao, email):
            raise ValueError("Email inválido")
        return email

    @staticmethod
    def validate_password(senha):
        if len(senha) < 6:
            raise ValueError("Senha inválida deve ter no mínimo 6 caracteres")
        return senha


if __name__ == '__main__':
    user = User.create_user("Fabio", "fabio@gmail.com", '123456')
    print(user.__dict__)