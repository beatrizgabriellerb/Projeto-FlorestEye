# FlorestEye

Sistema Inteligente de Cadastro de Denúncias Ambientais.

## Sobre o projeto

O FlorestEye foi desenvolvido para facilitar o registro e o acompanhamento de ocorrências ambientais. Sem um canal simples para comunicar casos como desmatamento, poluição e descarte irregular de resíduos, informações importantes podem deixar de chegar a quem pode analisá-las.

O sistema permite registrar denúncias ambientais com local, data, descrição e imagem. Cada denúncia recebe um status para que o usuário acompanhe seu andamento, enquanto administradores podem consultar e atualizar os registros.

## Funcionalidades

- Cadastro de usuários e acesso por e-mail e senha.
- Registro de denúncias com local, data da ocorrência, descrição e imagem.
- Consulta das próprias denúncias e de seus status.
- Painel administrativo para consultar denúncias, filtrar por status ou data e atualizar o status.
- Armazenamento de senhas com hash e criptografia de alguns dados das denúncias.

## Instalação e execução

É necessário ter o Python instalado. No terminal, na pasta do projeto:

1. Crie e ative um ambiente virtual:

   **Windows (PowerShell):**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **Linux/macOS:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie a aplicação:

   ```bash
   streamlit run app.py
   ```

4. Acesse o endereço local exibido no terminal pelo Streamlit.
