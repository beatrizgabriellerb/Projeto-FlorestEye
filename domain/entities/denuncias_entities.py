from utils.criptografia_propria import criptografar
from datetime import date


class Denuncia:
    def __init__(self, local: str, data_ocorrencia: date, descricao: str, imagem_path: str, status="PENDENTE"):
        self.local = local
        self.data_ocorrencia = data_ocorrencia
        self.descricao = descricao
        self.imagem_path = imagem_path
        self.status = status

    @staticmethod
    def create_denuncia(local: str, data_ocorrencia: date, descricao: str, imagem_path: str):
        validate_local = Denuncia.validate_local(local)
        validate_date = Denuncia.validate_date(data_ocorrencia)
        
        local_criptografado = criptografar(validate_local)
        descricao_criptografada = criptografar(descricao) if descricao else None
        imagem_criptografada = criptografar(imagem_path)

        return Denuncia(local_criptografado, validate_date, descricao_criptografada, imagem_criptografada)

    @staticmethod
    def validate_local(local: str):
        if len(local) < 10:
            raise ValueError("O Local deve ter no mínimo 10 caracteres")
        return local

    @staticmethod
    def validate_date(data_ocorrencia: date):
        if data_ocorrencia > date.today():
            raise ValueError("A data da ocorrência não pode ser no futuro.")
        return data_ocorrencia

    # @staticmethod
    # def validate_status(status: str):
    #     TYPE_STATUS = ["PENDENTE", "EM ANÁLISE", "CONCLUÍDO", "CANCELADO", "ARQUIVADO"]

    #     if not status.strip().upper() in TYPE_STATUS:
    #         raise ValueError("Erro o status não está com o tipo devido")
    #     return status




if __name__ == '__main__':
    denuncia = Denuncia.create_denuncia('local x sddadadasda asdsadada', date(2005, 9, 17), 'Qualquer descrição', 'img/img1.jpg2')
    print(denuncia.__dict__)
    
# decriptografar: bcrypt.checkpw(senha.encode(), hash_armazenado.encode())