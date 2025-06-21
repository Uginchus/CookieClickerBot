import pyautogui
import time

pyautogui.FAILSAFE = True

cookie_x, cookie_y = 390, 520
upgrade_1_x, upgrade_1_y = 2330, 300
upgrade_2_x, upgrade_2_y = 2330, 400
upgrade_3_x, upgrade_3_y = 2330, 500
upgrade_4_x, upgrade_4_y = 2330, 600
upgrade_5_x, upgrade_5_y = 2330, 700
upgrade_6_x, upgrade_6_y = 2330, 800
upgrade_7_x, upgrade_7_y = 2330, 900

perk_1_x, perk_1_y = 2130, 130

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
        
        if click_count % 40 == 0:
            pyautogui.click(upgrade_7_x, upgrade_7_y)
            pyautogui.click(upgrade_6_x, upgrade_6_y)
            pyautogui.click(upgrade_5_x, upgrade_5_y)
            pyautogui.click(upgrade_4_x, upgrade_4_y)
            pyautogui.click(upgrade_3_x, upgrade_3_y)
            pyautogui.click(upgrade_2_x, upgrade_2_y)
            pyautogui.click(upgrade_1_x, upgrade_1_y) 
        if click_count % 100 == 0:
            pyautogui.click(perk_1_x, perk_1_y)
        
except pyautogui.FailSafeException:
    print("\nFail-safe triggered! Script stopped.")
except KeyboardInterrupt:
    print("\nScript stopped by Ctrl-C.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
finally:
    print(f"Total clicks performed: {click_count}")
    print("Bot execution finished.")