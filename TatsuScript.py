import time
import pyautogui as auto
import random as rd

msg = "ttg train"

auto.position()
counter = 0
time.sleep(2)
luckynumber = rd.randint(5, 9)
print(luckynumber)
while counter < 50:
    auto.typewrite(msg, interval=(rd.randint(10, 20)/100))
    time.sleep(0.4)
    auto.press("enter")
    time.sleep(5 + (rd.randint(8, 15) / 10))
    counter += 1
    if (counter % 10) == luckynumber:
        time.sleep(rd.randint(5, 10) + rd.randint(0, 9)/10)
    print(counter)
