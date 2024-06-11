from pathlib import Path
import random
from string import ascii_letters,digits

# DIR_PATH = Path(r'DIGITE O CAMINHO DA PASTA AQUI')
DIR_PATH = Path(r'C:\Users\PC\Documents\Pasta')

CHARACTERS = '' + ascii_letters + digits
#Fu
def random_rename(path:Path,name_size:int):
    for root,dirs,files_ in path.walk():
        for file in files_:
            file_path = root / file
            print(file_path)
            extension = file.split('.')[1]
            new_name = ''.join(random.choices(CHARACTERS, k=name_size))
            new_name_path = root / f'{new_name}.{extension}'
            print(new_name_path)
            file_path.rename(new_name_path)

random_rename(DIR_PATH,10)


