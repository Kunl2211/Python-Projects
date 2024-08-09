import pyautogui
import pyperclip
import time

# This function helps to check if new message is there or not 

def get_last_message_sender(chat_history):
    # Extract the sender from the last message
    last_message = chat_history.split(']')[-1].split(":")[0]
    if("Kunal" in last_message): return True
    return False

# This function ensures the scanning of chats with the pyautogui function

def scan_chats():
    # Coordinates of whatsapp screen
    start_x, start_y = 613, 205  # Replace with the starting coordinates 
    end_x, end_y = 623, 935      # Replace with the ending coordinates

    # Move the cursor to the starting point and click
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()  # Press and hold the mouse button

    # Drag the cursor to the ending point
    pyautogui.moveTo(end_x, end_y)

    # Release the mouse button
    pyautogui.mouseUp()

    # Copy the selected text (usually Ctrl+C for most systems)
    pyautogui.hotkey('ctrl', 'c')

    # Optionally, you can add a delay to ensure the text is copied
    time.sleep(1)
    
    # This click is to release the dragged screen (Blue)
    pyautogui.click(613, 205)

    # It returns the scanned chat
    return pyperclip.paste()

# This ensures if there is any delay in execution, it is accounted before
time.sleep(2)

# This will open chrome from the Taskbar (You should Customize it)
pyautogui.click(1235,1050)

# Will run untill not killed by user
while(True):
    Input_data = scan_chats()

    last_msg = get_last_message_sender(Input_data)

    while(last_msg):
        print("No reply from other side yet!")
        time.sleep(10)
        Inp = scan_chats()
        last_msg = get_last_message_sender(Inp)

    # Placing ChatGpt on second tab and clicking it
    pyautogui.click(468,18)
    
    time.sleep(0.5)

    # This click presses the input bar of chatgpt and paste the chat
    pyautogui.click(713,951)
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(0.5)

    # Presses the enter key
    pyautogui.hotkey('enter')

    time.sleep(5) #Time to load the response
    pyautogui.click(751, 803) #This clicks the copy button in gpt screen to get the response copied

    time.sleep(0.5) #Accounting any delays
    pyautogui.click(172, 17) # Clicking the whatsapp tab again

    time.sleep(0.5)
    pyautogui.click(740, 966) #Clicking and Pasting the response in the chatbar
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

    # Wait for 10 seconds before restarting the scanning.
    time.sleep(10)
