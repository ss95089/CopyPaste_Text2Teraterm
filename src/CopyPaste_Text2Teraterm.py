import sys
import argparse
import pyautogui
import pyperclip
from termcolor import colored
import colorama
colorama.init()


parser = argparse.ArgumentParser()
parser.add_argument('-f', help='Name of command file to execute', required=True)
args = parser.parse_args()
fileName = args.f
fileName = fileName.replace(".\\", '')


input('Move the mouse pointer over the TeraTerm window. Press enter when ready.')
mouse_position01 = pyautogui.position()
print("TeraTerm window position : {}".format(mouse_position01))

input('Move the mouse pointer over the command prompt window of this tool. Press enter when ready.')
mouse_position02 = pyautogui.position()
print("command prompt window position : {}".format(mouse_position02))

before_line = 0
while True:
    vline = []
    with open(fileName, 'r', encoding="utf-8") as file:
        for i1, line in enumerate(file.readlines()):
            if line[:1] == '\t':
                vline.append(i1)

    with open(fileName, 'r', encoding="utf-8") as file:
        for i1, line in enumerate(file.readlines()):
            if i1 >= before_line:
                line = line.rstrip()
                if line[:1] != '\t':
                    print(colored(line, 'green'))
                else:
                    if line[1:] != "":
                        print(colored('\n-------- EXE CMD -------', 'red', attrs=['bold']))
                        print(colored(line[1:], 'red', attrs=['bold']))
                        cmd = input(' -> ExecuteOn[Enter]/[P]asteOnly/[S]kip/[R]eturn/[Q]uit: ').upper()
                        if cmd == "":
                            pyperclip.copy(line[1:])
                            pyautogui.click(mouse_position01)
                            pyautogui.hotkey('alt', 'v')
                            pyautogui.press("enter")
                            pyautogui.click(mouse_position02)
                        elif cmd == "P":
                            pyperclip.copy(line[1:])
                            pyautogui.click(mouse_position01)
                            pyautogui.hotkey('alt', 'v')
                        elif cmd == "R":
                            for i2, n1 in enumerate(vline):
                                if i1 == n1:
                                    before_line = vline[i2 - 1]
                            break
                        elif cmd == "S":
                            pass
                        elif cmd == "Q":
                            sys.exit()
        if cmd != "R":
            break
