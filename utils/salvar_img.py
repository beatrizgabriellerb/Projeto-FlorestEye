import os

def save_img(img):
    if not img:
        return None

    pasta_imagens = "static"
    
    # Garante que a pasta existe (caso ainda não tenha sido criada)
    os.makedirs(pasta_imagens, exist_ok=True)
    
    # Monta o caminho completo onde o arquivo será salvo
    caminho_completo = os.path.join(pasta_imagens, img.name)
    
    # Salva os bytes da imagem no disco
    with open(caminho_completo, "wb") as f:
        f.write(img.getbuffer())
        