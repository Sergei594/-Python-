import json
import os

def load_notes():
    file_path = os.path.join(os.getcwd(), 'notes.json')  
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        with open(file_path, 'w') as file:
            json.dump({}, file)
        return {}

