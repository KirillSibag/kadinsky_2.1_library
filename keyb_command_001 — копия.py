import pyautogui, random
from time import sleep

data = []
with open("words.txt") as f:
    data = f.readlines()

diction = []

for i in range(len(data)):
    linn = data[i]
    counter = 0
    app_obj = ""

    while linn[counter] != " ":
        app_obj += linn[counter]
        counter += 1

    diction.append(app_obj)

times = 1
m = ' '
d = ', '

# пауза и досрочное прекращение
pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

# разрешение и позиция
pyautogui.size()
pyautogui.position()

def delay(time):
    sleep(time)
    
def ctrl(letter):
    pyautogui.hotkey('ctrl', letter)

def alt(lett):
    pyautogui.hotkey('alt', lett)

def mouse(x, y):
    pyautogui.moveTo(x, y, duration=0)
    cl()

def cl():
    pyautogui.click()

def prnt(text):
    pyautogui.typewrite(text, interval=0.0)

def ent():
    pyautogui.press('enter')

def move(x, y):
    pyautogui.moveTo(x, y, duration=0)




def main001():
    delay(6)
    for j in range(times):
        picture_names = []
        
        for i in range(10):
            ctrl('t')

            #перейти на сайт
            prnt('https://fusionbrain.ai/diffusion')
            ent()
            delay(1.4)
            mouse(800, 950)

            prompt = diction[random.randint(0, len(diction)-1)] + m + diction[random.randint(0, len(diction)-1)]

            #ввести промпт
            prnt(prompt)
            picture_names.append("a " + prompt)
            
            vb = random.randint(0, 2)
            if vb > 1:
                #выбрать стиль
                mouse(150, 960)
                mouse(150, 420)
            


                
            #начать генерацию
            mouse(1300, 960)
            

        ctrl('tab')

        for i in range(10):
            ctrl('w')
            #щелк по фотке
            mouse(800, 700)
            
            #загрузить
            mouse(800, 960)
            delay(0.35)
            
            #по сохранению
            mouse(1709, 167) 
            delay(0.3)

            h = 190
            corr = 0
            count = 0
            while corr == 0 and count < 20:
                delay(0.2)
                h += 28
                move(399, h)
                x, y = pyautogui.position()
                px = pyautogui.pixel(x, y)
                if px[0] <= 217:
                    corr = 1
                count += 1

            if count < 15:
                #по названию
                cl()
                delay(0.6)
               

                #имя
                prnt(picture_names[i])
                
                ent()
                delay(0.3)
                
            mouse(1895, 10)
            delay(0.4)


        mouse(251, 1060)
        delay(0.1)
        mouse(251, 950)
        delay(0.3)
        ctrl('n')
        delay(0.5)

main001()
