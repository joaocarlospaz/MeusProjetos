# Ambientes virtuais em Python (venv)
# Vantagens -> Caso vc faça varios tipos de projetos diferentes, 
# as instalações e o conteudo usado, fica salvo no ambiente virtual;
# * para ver a versão do python - > python -V / python -version
# gcm python mostra o caminho de onde está o python
# gcm python -Syntax


# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido - pasta lib .
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.

# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# python -m venv nome_do_ambiente <- para criar um ambiente virtual

# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

# para desativar o venv -> desactivate
# para ativar - >  .venv\Scripts\activate

# Para instalar coisas para seu ambiente virtual, usa-se pip
# ficam na pasta lib
# duas formas
# pip install pyautogui
# python -m pip install pyautogui -y
# pra desinstalar o mesmo codigo, mas com uninstall
# pip freeze mostra tudo que já está instalado
# pip index versions pyautogui -> aparece todas as versões do pyautogui
# --upgrade para atualizar para ultima versão
# pip freeze > requeriments.txt -> gera uma pasta com tudo que esta instalado no venv
# para instalar tudo que ta em requeriments
# pip install -r .\requeriments.txt -> instala tudo que tem

# pwd pra mostrar o caminho de todas as pastas