import pyautogui
import time
import pandas as pd

pyautogui.FAILSAFE = True

cookie_x, cookie_y = 390, 520
perk_1_x, perk_1_y = 2130, 130

data = pd.read_csv('data/cc.csv')

print("Starting Cookie Clicker bot. To stop:")
print("1. Rapidly move your mouse to the TOP-LEFT corner of your primary screen.")
print("2. Or press Ctrl-C in your terminal (if you can get focus).")
print("Bot will start in 5 seconds. Switch to the game window now.")
time.sleep(5)

click_count = 0
try:
    start_time = time.time()
    while True:
        pyautogui.click(cookie_x, cookie_y)
        click_count += 1
        time.sleep(0.0001)
        
        if click_count % 50 == 0:
            for index, row in data.iloc[::-1].iterrows():
                pyautogui.click(row['x'], row['y'])
        if click_count % 110 == 0:
            pyautogui.click(perk_1_x, perk_1_y)
        
except pyautogui.FailSafeException:
    print("\nFail-safe triggered! Script stopped.")
except KeyboardInterrupt:
    print("\nScript stopped by Ctrl-C.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
finally:
    print(f"Bot execution finished /// Total clicks performed: {click_count}")