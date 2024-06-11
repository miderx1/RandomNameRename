from pathlib import Path
import random
from string import ascii_letters,digits

DIR_PATH = Path(r'DIGITE O CAMINHO DA PASTA AQUI')

CHARACTERS = '' + ascii_letters + digits

def random_rename(path:Path,name_size:int):
    for root,dirs,files_ in path.walk():
        for file in files_:
            file_path = root / file
            extension = file.split('.')[1]
            new_name = ''.join(random.choices(CHARACTERS, k=name_size))
            new_name_path = root / f'{new_name}.{extension}'
            file_path.rename(new_name_path)

random_rename(DIR_PATH,10)


