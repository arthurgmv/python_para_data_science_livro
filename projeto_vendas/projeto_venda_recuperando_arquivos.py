import os
from pathlib import Path
import pandas as pd

script_path = os.getcwd()
def get_all_files_path():
    files_path = []
    path = Path(script_path + "/Vendas")

    for dir in path.iterdir():
        if dir.is_dir():
            os.chdir(dir)
            path = Path.cwd()
            print(path)

            for dir in path.iterdir():
                if dir.is_dir():
                    os.chdir(dir)
                    path = Path.cwd()
                    for file in path.iterdir():
                        if '.DS_Store' in file.name:
                            continue
                        print(file)
                        files_path.append(file)
    return files_path

file_path = get_all_files_path()
print(file_path)