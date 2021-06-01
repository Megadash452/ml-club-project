from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expected

from time import sleep
import voice

print("hello")

# for i in range(1, 6):
listener = voice.AudioClassifier(
    model_file=voice.VOICE_MODEL,
    labels_file=voice.VOICE_LABELS,
    audio_device_index=1
)

browser = webdriver.Chrome("chromedriver")
browser.get("file:///home/pi/final_ml_club/help_site/help.html")

while 1:
    command = listener.next(block=False)

    if command:
        print(command)