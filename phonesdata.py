# 1. Открывать файл (режим txt)+
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def open_file (path):# принимает файл и открывает его в консоли построчно в виде списков
    with open (path, 'r') as f:
        for line in f:
            print((line.rstrip().split(':')))

def delite_contact(path, line_number):
    with open(path, 'r+') as f:
        lines = f.readlines()
        if line_number > len(lines):
            print(f"Такого контакта не существует")
            return
        del lines[line_number - 1]
        f.seek(0)    
        f.writelines(lines)
        f.truncate()
    print(f"Контакт №{line_number} успешно удален из справочника")

def create_contact (path):
    with open (path, 'a') as f:
        f.write(input()+'\n')   

def redaction_contact(path, line_number):
    with open(path, 'r') as f:
        lines = f.readlines()
    line_to_edit = lines[line_number - 1].strip().split()
    for i in range(len(line_to_edit)):
        line_to_edit[i] = input()
    lines[line_number - 1] = ' '.join(line_to_edit) + '\n'
    with open(path, 'w') as f:
        f.writelines(lines)

def search_word_in_file(file_path, keyword):
    line_number = 0
    matching_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            line_number += 1
            if keyword in line:
                matching_lines.append((line_number, line))
    return matching_lines

print('Это телефонный справочник')
print('Просмотреть контакты - 1, Добавить контакт - 2, удалить контакт - 3, редактировать контакт - 4')
menu_command=int(input('Введите номер команды: '))

if menu_command>0 and menu_command<5:
        if menu_command==1:
            open_file('phones.txt')
        if menu_command==2:
            create_contact('phones.txt')
        if menu_command==3:
            delite_contact('phones.txt', int(input()))
        if menu_command==4:
            redaction_contact('phones.txt', int(input()))



    


 


