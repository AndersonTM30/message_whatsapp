from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui


url = 'https://web.whatsapp.com/'

# webbrowser.open(url)


telefone = '5500999998888'

mensagem = 'Bonju, já testou os processos?'

link_mensagem_whatsapp = f'{url}send?phone={telefone}&text={quote(mensagem)}'

for i in range(10):
    webbrowser.open(link_mensagem_whatsapp)
    sleep(10)
    try:
        send = pyautogui.locateCenterOnScreen('send.png')
        sleep(5)
        pyautogui.click(send[0], send[1])
        sleep(3)
        pyautogui.hotkey('ctrl', 'w')
        sleep(3)
    except:
        print(f'Não foi possível clicar na imagem!')
    print(f'Mensagem de número {i}')
    
