import base64
import os

def imagem_para_base64(nome_arquivo):
  caminho_completo = os.path.join("img", str(nome_arquivo))

  if os.path.exists(caminho_completo):
    with open(caminho_completo, "rb") as f:
      return "data:image/png;base64," + base64.b64encode(f.read()).decode()
  return None
