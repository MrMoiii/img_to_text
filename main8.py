from pynput import keyboard, mouse
from PIL import ImageGrab
import pytesseract
import pyperclip
import sys

# à modifier : 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def on_press(key):
    #fonction qui permet de demarrer la capture ou stopper le programme
    #les touches "backspace" et "space" peuvent être personnalisées
    global listener
    if key == keyboard.Key.backspace:
        #active le listener de la souris pour demarer la capture
        listener = mouse.Listener(on_click=on_click)
        listener.start()
    if key == keyboard.Key.space:
        sys.exit(-1)

def on_click(x, y, button, pressed):
    # fonction activée lors du clic de la souris 
    global pos1, pos2, listener
    if pressed:
        if pos1 is None:
            pos1 = (x, y)
        else:
            pos2 = (x, y)

            #récupération du square à capturé
            pos1,pos2=(min(pos1[0],pos2[0]),min(pos1[1],pos2[1])),(max(pos1[0],pos2[0]),max(pos1[1],pos2[1]))
            listener.stop()
            box = (pos1[0], pos1[1], pos2[0], pos2[1])
            image = ImageGrab.grab(box)
            image.save('screenshot.png')

            #traitement de l'image pour la convertion en text
            result = pytesseract.image_to_string(image)
            print(result)
            pyperclip.copy(result)

            #reset
            pos1,pos2=None,None

         
pos1 = None
pos2 = None
listener = None
with keyboard.Listener(on_press=on_press) as k_listener:
    k_listener.join()