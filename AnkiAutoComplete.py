import pyautogui
import time
import pyperclip

def FoundByIMG (I):
    try:
        return pyautogui.locateCenterOnScreen(I, confidence=0.7)
    except:
        return 0
#Search for an image, if found return the position, if an error occurs return a negative value without crashing the code.

STRING = pyautogui.prompt(text="Enter text in the correct format E: CPU:Ryzen;GPU:Nvidia", title="PYAUTOGUI", default="")

if  (STRING == "" or STRING == "None"):
    pyautogui.alert(text="Enter text in the correct format, this field cannot be inwhite", title="PYAUTOGUI", button="X")
    # check if there is text, if there is no close the program
else:
    array = STRING.split(";")
    def go ():
        for ar in array:
            if (not (":" in ar)):
                pyautogui.alert(text=f"{ar}: Incorrect text format, fix it and try again", title="PYAUTOGUI", button="X")
                # Closes the program and indicates the error if it is not in the correct format
                return
        for ra in array:
            def ab ():
                verify = FoundByIMG("x.png")
                if (not verify):
                    pyautogui.click(FoundByIMG("O.png"))
                    pyautogui.press("end")
                    pyautogui.press("enter")
                    # look for the text box and if you don't find it, open the application tab
                [fre,  ver] =  ra.split(":")
                pyautogui.click(FoundByIMG("x.png"))
                pyperclip.copy(fre)
                pyautogui.hotkey("ctrl", "v")
                time.sleep(1)
                # Type the text, and wait 1 second
                if (FoundByIMG("D.png")):
                    pyautogui.hotkey("ctrl", "a")
                    pyautogui.press("delete")
                    # checks if the text is repeated, if so, deletes it and jumps to the next one.
                else:
                    pyautogui.click(FoundByIMG("y.png"))
                    pyperclip.copy(ver)
                    pyautogui.hotkey("ctrl", "v")
                    pyautogui.click(FoundByIMG("G.png"))
                    # Write the text of the verse, and finish the section
                reveri = FoundByIMG("x.png")
                if (not reveri):
                    ab()
                # checks if the application tab is active, if not, repeats the last action
            ab()
        print("Finish")
    go()