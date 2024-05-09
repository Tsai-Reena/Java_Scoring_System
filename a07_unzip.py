import os
import sys
import zipfile
import shutil

def collectfiles(source_file, extracted_folder, files_path, suffix):

    # 創建資料夾
    if os.path.exists(extracted_folder):
        shutil.rmtree(extracted_folder)
    os.makedirs(extracted_folder, exist_ok=True)
    if os.path.exists(files_path):
        shutil.rmtree(files_path)
    os.makedirs(files_path, exist_ok=True)

    # 解壓縮
    ZIP = zipfile.ZipFile(source_file)
    ZIP.extractall(extracted_folder)
    ZIP.close()

    filelist = [] # 儲存要 copy 的文件名

    for dirpath, dirnames, filenames in os.walk(extracted_folder):
        for file in filenames:
            file_type = file.split('.')[-1] # 副檔名
            if(file_type in suffix):
                file_fullname = os.path.join(dirpath, file)
                filelist.append(file_fullname)
    for file in filelist:
        print(file)
        shutil.copy(file, files_path)
    if os.path.exists(extracted_folder):
        shutil.rmtree(extracted_folder)

def move_puzzles():
    # 設定目標資料夾
    target_folder = 'files'

    # 遍歷當前目錄中的項目
    for item in os.listdir('.'):
        # 檢查是否為以 'puzzles' 開頭的資料夾
        if os.path.isdir(item) and item.startswith('puzzles'):
            # 移動資料夾
            shutil.move(item, os.path.join(target_folder, item))
            print(f"Moved {item} to {target_folder}/")

    print("Finished moving puzzle folders.")
    
def move_inputs():
    # 設定目標資料夾
    target_folder = 'files'
    
    # 遍歷當前目錄中的所有文件
    for filename in os.listdir('.'):
        # 檢查文件名稱是否以 '.in' 結尾
        if filename.endswith('.in'):
            # 移動文件
            shutil.move(filename, os.path.join(target_folder, filename))
            print(f"Moved {filename} to {target_folder}/")

    print("Finished moving .in files.")

def main(zip_file):
    # 要解壓縮的資料夾
    source_file = zip_file

    # 解壓縮後的目標資料夾路徑
    extracted_folder = 'unzip_file'
    files_path = 'files'
    
    # 解壓縮
    collectfiles(source_file, extracted_folder, files_path, ['java', 'cpp'])
    
    # 移動 puzzles 資料夾
    move_puzzles()
    
    # 移動 .in 檔案
    move_inputs()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("請提供 ZIP 檔案名稱作為命令行參數。")
    else:
        zip_file = sys.argv[1]
        main(zip_file)
    