import pyautogui 
import time

# pyautogui.press() -> Apertar uma tecla
# pyautogui.click() -> Clicar com o mouse 
# pyautogui.write() - > escrever um texto
# pyautogui.hotkey("coomand", "space") - > atalho do teclado

pyautogui.PAUSE = 0.5
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# Entrar no site
pyautogui.write("https://www.hashtagtreinamentos.com/curso-python?tipo=a&src=site")
pyautogui.press("enter")

time.sleep(5)
# Preencher o formulario
pyautogui.click(x=541, y=626)
pyautogui.write("Joao Carlos")
pyautogui.press("tab")
pyautogui.write("...@gmail.com")
pyautogui.press("tab")
pyautogui.write("...")

# Enviar o formulario
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1.5)
# Abriu outra aba, repeteco
pyautogui.click(x=807, y=301)
pyautogui.write("Joao Carlos")
pyautogui.press("tab")
pyautogui.write("...@gmail.com")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("Brazil")
pyautogui.press("enter")
pyautogui.write("...")
pyautogui.press("tab")
pyautogui.press("enter")
