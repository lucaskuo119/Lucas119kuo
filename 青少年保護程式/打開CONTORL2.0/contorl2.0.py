import pyautogui
import time
import random
import tkinter as tk
from tkinter import messagebox
#git hub test
#root = tk.Tk()
#root.withdraw()

#messagebox.showinfo("lucas119", "ok")

#申訴文案內容

#內容結束
i = 0
while i < 101:

    time.sleep(0.2)
    help_pos = pyautogui.locateOnScreen('bot15.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")

    time.sleep(0.5)
    pyautogui.typewrite('https://www.win.org.tw/addCase')
    pyautogui.keyDown('enter')



    time.sleep(1)

    help_pos = pyautogui.locateOnScreen('bot0.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")


    

    time.sleep(0.2)
    pyautogui.moveRel(0,500,duration=0.1)
    pyautogui.scroll(1000)
    time.sleep(0.2)


    help_pos = pyautogui.locateOnScreen('bot1.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")
    pyautogui.typewrite('ministry of educatipn')

    time.sleep(0.2)

    num = random.random()*290+30
    #pyautogui.moveRel(0,num,duration=0.2)

    help_pos = pyautogui.locateOnScreen('bot2.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")
    pyautogui.moveRel(0,num,duration=0.2)
    pyautogui.click(button="left")#bot2

    time.sleep(0.2)

    help_pos = pyautogui.locateOnScreen('bot3.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")
    time.sleep(0.2)
    pyautogui.moveRel(0,50,duration=0.2)
    pyautogui.click(button="left")#bot2

    time.sleep(0.2)

    help_pos = pyautogui.locateOnScreen('bot4.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")
    time.sleep(0.2)
    pyautogui.moveRel(85,0,duration=0.01)
    pyautogui.click(button="left")
    pyautogui.moveRel(85,0,duration=0.01)
    pyautogui.click(button="left")

    time.sleep(0.2)
#2.0更改處
    #help_pos = pyautogui.locateOnScreen('bot5.png')
    #goto_pos = pyautogui.center(help_pos)
    #pyautogui.moveTo(goto_pos,duration=0.2)
    #pyautogui.click(button="left")
    item2 = random.choice([426,669,656])
    if item2 == 426 :
        a = 900
    if item2 == 669 :
        a = 905
    if item2 == 656 :
        a = 976
    if item2 == 1107 :
        a = 902
    pyautogui.moveTo(item2,a)
    pyautogui.click(button="left")
#更改結束

    time.sleep(2)

    pyautogui.scroll(-400)

    time.sleep(0.2)
#on.2 change
    pyautogui.moveTo(403,788)
    pyautogui.click(button="left")
#end
    pyautogui.moveTo(404,925)
    pyautogui.click(button="left")
    #time.sleep(0.2)
    #pyautogui.scroll(-130)
    #time.sleep(0.2)
    #pyautogui.click(button="left")

    #time.sleep(0.2)
    #pyautogui.scroll(-160)
    #time.sleep(0.1)
    #pyautogui.click(button="left")
    #pyautogui.typewrite('https://www.edu.tw/Default.aspx')

    time.sleep(0.2)

    pyautogui.scroll(-1000)

    help_pos = pyautogui.locateOnScreen('bot2.1.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")
    pyautogui.typewrite('https://english.moe.gov.tw/mp-1.html')

    time.sleep(0.2)

    help_pos = pyautogui.locateOnScreen('bot6.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")

    time.sleep(0.2)

    pyautogui.scroll(-300)
    help_pos = pyautogui.locateOnScreen('bot7.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")
    time.sleep(0.2)
    pyautogui.typewrite('The existence of this website has brought about significant drawbacks to our society. It not only encourages violent behavior and poses a threat to the safety of others but also serves as a platform inciting crime. These games are filled with brutal scenes, turning violence and slaughter into a form of entertainment, causing significant damage to the values and ethical principles of players. This website also fuels national hatred, spreading hate speech and racial discrimination, intensifying social division and disharmony. This has serious consequences for our societal image, cultural literacy, and social harmony.')
    time.sleep(0.2)
    pyautogui.typewrite('We strongly recommend taking down this website to protect the harmony and safety of society. Taking down this website is for safeguarding the mental and physical health of young people, allowing them to grow in a proper value system. Additionally, it is to maintain the image and reputation of the country, preventing the spread of national hatred.We hope the government takes this issue seriously, strengthens network management and supervision, removes such negatively impactful gaming websites from the internet, and makes our society more harmonious and secure.')


    time.sleep(0.2)

    pyautogui.moveRel(300,100,duration=0.2)
    pyautogui.click(button='left')
    time.sleep(0.2)
    pyautogui.scroll(-300)

    time.sleep(0.2)


    help_pos = pyautogui.locateOnScreen('bot8.png')
    goto_pos = pyautogui.center(help_pos)
    pyautogui.moveTo(goto_pos,duration=0.2)
    pyautogui.click(button="left")

    time.sleep(random.randint(1000,1200))

