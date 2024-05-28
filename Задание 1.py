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

def delete_note_by_title(notes):
    print("Список заметок:")
    for note_id, note_info in notes.items():
        print(f'ID: {note_id}, Заголовок: {note_info["title"]}')
    title_to_delete = input('Введите заголовок заметки для удаления: ')
    note_ids_to_delete = [note_id for note_id, note_info in notes.items() if note_info["title"] == title_to_delete]
    if note_ids_to_delete:
        for note_id in note_ids_to_delete:
            delete_note_by_id(notes, note_id)
    else:
        print('Заметка с таким заголовком не найдена')

def delete_note(notes):
    print("Выберите как вы хотите удалить заметку:")
    print("1. По ID")
    print("2. По заголовку")
    choice = input("Ваш выбор: ")
    if choice == '1':
        note_id = input('Введите ID заметки для удаления: ')
        if note_id.isdigit():
            note_id = int(note_id)
            delete_note_by_id(notes, note_id)
        else:
            print('Некорректный ввод ID заметки')
    elif choice == '2':
        delete_note_by_title(notes)
    else:
        print('Некорректный выбор, попробуйте снова')

def edit_note_by_title(notes):
    print("Список заметок:")
    for note_id, note_info in notes.items():
        print(f'ID: {note_id}, Заголовок: {note_info["title"]}')
    title_to_edit = input('Введите заголовок заметки для редактирования: ')
    note_ids_to_edit = [note_id for note_id, note_info in notes.items() if note_info["title"] == title_to_edit]
    if note_ids_to_edit:
        for note_id in note_ids_to_edit:
            title = input('Введите новый заголовок заметки: ')
            body = input('Введите новый текст заметки: ')
            edit_note(notes, note_id, title, body)
    else:
        print('Заметка с таким заголовком не найдена')

def list_notes(notes):
    for note_id, note_info in notes.items():
        print(f'ID: {note_id}, Заголовок: {note_info["title"]}')

notes = load_notes()

while True:
    print('\n1. Посмотреть список заметок')
    print('2. Добавить заметку')
    print('3. Редактировать заметку')
    print('4. Удалить заметку')
    print('5. Выйти')
    
    choice = input('Выберите действие: ')
    
    if choice == '1':
        list_notes(notes)
    elif choice == '2':
        title = input('Введите заголовок заметки: ')
        body = input('Введите текст заметки: ')
        add_note(notes, title, body)
    elif choice == '3':
        edit_note_by_title(notes)
    elif choice == '4':
        delete_note(notes)
    elif choice == '5':
        break
    else:
        print('Некорректный выбор, попробуйте снова')
