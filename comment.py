import os

# 定義函式來處理單個Java檔案
# def process_java_file(file_path):
    # with open(file_path, 'r') as file:
    #     lines = file.readlines()

    # modified_lines = []
    # inside_package = False

    # for line in lines:
    #     if line.strip().startswith("package "):
    #         modified_lines.append("//" + line)
    #     else:
    #         modified_lines.append(line)

    # with open(file_path, 'w') as file:
    #     file.writelines(modified_lines)

def comment_package_lines(folder_path):
    # 遍歷資料夾中的所有Java檔案
    for filename in os.listdir(folder_path):
        if filename.endswith('.java'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()  # 讀取所有行
                with open(file_path, 'w', encoding='utf-8') as file:
                    for line in lines:
                        # 如果行以'package'開頭，則添加註解
                        if line.strip().startswith('package'):
                            line = '//' + line
                        file.write(line)
            except UnicodeDecodeError:
                print(f"Encoding error in file: {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

def main():
    # # 取得當前資料夾中的所有Java檔案
    # folder_path = "./files"
    # java_files = [f for f in os.listdir(folder_path) if f.endswith('.java')]

    # # 逐一處理每個Java檔案
    # for java_file in java_files:
    #     file_path = os.path.join(folder_path, java_file)
    #     process_java_file(file_path)
    
    # 呼叫函數，資料夾路徑設為'files'
    comment_package_lines('files')

    print("Completely remove all the packages.")
    
if __name__ == "__main__":
    main()