import filecmp
import os
import csv
import pandas as pd

def compare_files(file1, file2):
    """比較兩個文件的內容是否相同，忽略換行"""
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read().strip() == f2.read().strip()
    
def calculate_total_score():
    results_file = 'comparison_result.csv'
    df = pd.read_csv(results_file)
    df['Score'] = df.drop(['StudentID'], axis=1).sum(axis=1)
    
    df.to_csv(results_file, index=False)
    print("Total scores added the file saved.")
    
def compare_and_record():
    results_file = 'comparison_result.csv'
    results = {}  # 初始化結果存儲結構
    
    for i in range(1, 11):
        # 設定當前目錄下的檔案與目標資料夾
        current_file = f'puzzles{i}.txt'
        target_folder = f'puzzles{i}_txt'
        
        if not os.path.exists(target_folder):
            print(f'Folder {target_folder} does not exist.')
            continue
        for txt_file in os.listdir(target_folder):
            if txt_file.endswith('.txt'):
                txt_file_path = os.path.join(target_folder, txt_file)
                is_identical = compare_files(current_file, txt_file_path)
                score = '10' if is_identical else '0'
                
                # 學生ID就是文件名去掉擴展名
                student_id = os.path.splitext(txt_file)[0]
                student_id = student_id.replace(f'puzzles{i}_', '')
                
                # 保存結果到學生字典
                if student_id not in results:
                    results[student_id] = {}
                results[student_id][f'puzzles{i}'] = score
    # 寫入CSV
    with open(results_file, 'w', newline='', encoding='utf-8') as csvfile:
        total = 0
        fieldnames = ['StudentID'] + [f'puzzles{i}' for i in range(1, 11)]
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        
        for student_id, scores in results.items():
            row = {'StudentID': student_id}
            row.update(scores)
            csv_writer.writerow(row)

    print(f"Finished comparing files. Results have been saved to {results_file}.")

if __name__ == "__main__":
    compare_and_record()
    calculate_total_score()
