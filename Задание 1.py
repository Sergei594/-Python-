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

def save_notes(notes):
    file_path = os.path.join(os.getcwd(), 'notes.json')  
    with open(file_path, 'w') as file:
        json.dump(notes, file, indent=4)

def add_note(notes, title, body):
    note_id = len(notes) + 1
    notes[note_id] = {'title': title, 'body': body}
    save_notes(notes)
    print('Заметка добавлена')

def edit_note(notes, note_id, title, body):
    if note_id in notes:
        notes[note_id] = {'title': title, 'body': body}
        save_notes(notes)
        print('Заметка отредактирована')
    else:
        print('Заметка с таким ID не найдена')

def delete_note_by_id(notes, note_id):
    if note_id in notes:
        del notes[note_id]
        save_notes(notes)
        print('Заметка удалена')
    else:
        print('Заметка с таким ID не найдена')

