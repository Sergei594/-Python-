import json
import os
from datetime import datetime

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
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[note_id] = {'title': title, 'body': body, 'created_at': current_time, 'updated_at': current_time}
    save_notes(notes)
    print('Заметка добавлена')

def edit_note(notes, note_id, title, body):
    if note_id in notes:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes[note_id] = {'title': title, 'body': body, 'created_at': notes[note_id]['created_at'], 'updated_at': current_time}
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
        print(f'ID: {note_id}, Заголовок: {note_info["title"]}, Создано: {note_info["created_at"]}, Последнее изменение: {note_info["updated_at"]}')
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

def list_notes(notes):
    for note_id, note_info in notes.items():
        print(f'ID: {note_id}, Заголовок: {note_info["title"]}, Создано: {note_info["created_at"]}, Последнее изменение: {note_info["updated_at"]}')

def filter_notes_by_date(notes):
    date_str = input("Введите дату в формате 'День-Месяц-Год' (DD-MM-YYYY): ")
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        filtered_notes = {note_id: note_info for note_id, note_info in notes.items() if datetime.strptime(note_info['created_at'], "%Y-%m-%d %H:%M:%S").date() == date.date() or datetime.strptime(note_info['updated_at'], "%Y-%m-%d %H:%M:%S").date() == date.date()}
        if filtered_notes:
            print("Найденные заметки:")
            list_notes(filtered_notes)
        else:
            print("Заметки не найдены для указанной даты.")
    except ValueError:
        print("Некорректный формат даты. Пожалуйста, введите дату в формате 'День-Месяц-Год' (DD-MM-YYYY).")

notes = load_notes()

while True:
    print('\n1. Посмотреть список заметок')
    print('2. Добавить заметку')
    print('3. Редактировать заметку')
    print('4. Удалить заметку')
    print('5. Найти заметки по дате')
    print('6. Выйти')
    
    choice = input('Выберите действие: ')
    
    if choice == '1':
        list_notes(notes)
    elif choice == '2':
        title = input('Введите заголовок заметки: ')
        body = input('Введите текст заметки: ')
        add_note(notes, title, body)
    elif choice == '3':
        note_id = int(input('Введите ID заметки для редактирования: '))
        title = input('Введите новый заголовок заметки: ')
        body = input('Введите новый текст заметки: ')
        edit_note(notes, note_id, title, body)
    elif choice == '4':
        delete_note(notes)
    elif choice == '5':
        filter_notes_by_date(notes)
    elif choice == '6':
        break
    else:
        print('Некорректный выбор,
