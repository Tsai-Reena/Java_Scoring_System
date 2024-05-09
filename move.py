import os
import shutil

def move_files(source_folder, start_with, target_folder):
    # 如果目標資料夾不存在，則創建它
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍歷當前目錄下的所有檔案
    for filename in os.listdir(source_folder):
        # 檢查檔案是否以 start_with 開頭且為'.txt'檔案
        if filename.startswith(start_with) and filename.endswith('.txt'):
            # 建立來源和目標檔案的完整路徑
            source_file = os.path.join(source_folder, filename)
            target_file = os.path.join(target_folder, filename)
            
            # 移動檔案
            shutil.move(source_file, target_file)
            print(f"Moved {filename} to {target_folder}/")

def main():
    for i in range(10, 0, -1):
        # 設定來源和目標資料夾
        source_folder = '.'
        start_with = f'puzzles{i}_'
        target_folder = f'puzzles{i}_txt'
        move_files(source_folder, start_with, target_folder)
        print(f"Finished moving puzzles{i} .txt files.")
        
if __name__ == "__main__":
    main()