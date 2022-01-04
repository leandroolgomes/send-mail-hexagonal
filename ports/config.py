from dotenv import load_dotenv
import os

def start():
    load_dotenv()
    print('Config component started!')
    return os.environ