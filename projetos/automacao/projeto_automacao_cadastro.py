# Automação pyautogui/time/panda
import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 0.5 # delay

# pyautogui.press -> pressionar tecla
# pyautogui.write -> escrever
# pyautogui.click -> clicar na tela
# pyautogui.scroll -> rolar o scroll

# entrar no site
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# fazer login
pyautogui.click(x=725, y=391) # peguei com position
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("enter")
time.sleep(3)

# usar a base de dados 
tabela = pd.read_csv(r"C:\Users\N1no\OneDrive\Documentos\Projetos Udmy\projetos\automacao\produtos.csv")

# cadastrar um produto
# repetir a ação varias vezes
for linha in tabela.index: #index, retorna os indices da tabela
    # codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=699, y=279)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)