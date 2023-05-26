# 1. Открывать файл (режим txt)+
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# path = 'call.txt'
# data = open(path, 'w')
# for line in data:
#     print(line)
# data.close()

def open_file_read(path):# принимает и открывает файл, возвращает в виде списка списков
    with open(path,'r') as file:
        main_list=(file.readlines())   
        main_list_str=[x.rstrip().split(':') for x in main_list]
    return main_list_str
    
print(open_file_read('phones.txt'))

def open_file_write(path, list_file):
    with open(path, 'w') as file:
        file.writelines([':'.join(x)+'\n' for x in list_file])
list_for_look=[['Ivanov', 'Ivan', '123456', 'comment'], ['Petrov', 'Petr', '456789', 'comment'], ['Chudilov', 'Sasha', '987654', 'comment']]
def look_list (list_for_look):
    print([' '.join(x) for x in list_for_look], end='\n')

look_list(list_for_look)




        



