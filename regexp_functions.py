import re
import os # работа с файловой системой

def salted_translate(text):
    """Функцию которая осуществляет перевод с русского на "солёный язык" - 
    после каждой гласной добавляется постоянная согласная 'с' и ещё раз эта же гласная"""
    pattern = r'([АЕЁИОУЫЭЮЯаеёиоуыэюя])'
    return re.sub(pattern, r'\1с\1', text)

def accords_extract(file_path):
    """Из файла с текстом и аккордами песни возвращает аккорды (set)"""
    with open(file_path, 'r') as file:
        text=file.read()
    pattern=r'\b[A-G]m?\b'
    accord = set(re.findall(pattern, text))
    
    return accord

def rename_files(dir, pattern, new_pattern=None, sample_names=None,to_replace=False):
    """Функция осуществляет групповое переименование файлов либо по паттерну, 
    либо по словарю названий образцов, либо последовательно по обоим механизмам. """
    #https://pythonworld.ru/moduli/modul-os.html
    for filename in os.listdir(dir):
        if not re.search(pattern,filename):
            continue
        
        # https://pythonworld.ru/moduli/modul-os-path.html
        path=os.path.join(dir,filename)
        new_name = filename
        if new_pattern != None:
            new_name=re.sub(pattern, new_pattern, new_name)
            
        if sample_names != None:
            for old, new in sample_names.items():
                new_name=re.sub(old,new,new_name)
                
        new_path=os.path.join(dir,new_name)
        
        if os.path.exists(new_path): # не перезаписать существующий файл
            continue
        
        if to_replace:
            os.rename(path, new_path)
        else:
            with open(path, 'r') as old_file:
                with open(new_path, 'w') as new_file:
                    for line in old_file:
                        new_file.write(line)
                        
            
        