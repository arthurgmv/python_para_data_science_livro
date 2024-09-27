import pyautogui

#move o mouse para uma coordenada específica
pyautogui.moveTo(x=2, y=1, duration=2)

#move o mouse para uma coordenada relativa a posição atual
#pyautogui.moveRel(xOffset=200, yOffset=0, duration=2)

#clicando o mouse após uma coordenada
#pyautogui.click(x=27, y=13, duration=2, button='right')

pyautogui.doubleClick(button='right')