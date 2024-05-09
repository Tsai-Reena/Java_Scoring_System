import os

def compile_and_run_files_in_folders(folder_path):
    
    # 取得資料夾中的所有Java檔案
    java_files = [f for f in os.listdir(folder_path) if f.endswith('.java')]
    
     # 逐一處理每個Java檔案
    for java_file in java_files:
        file_path = os.path.join(folder_path, java_file)
        student_id = java_file.split('.')[0]  # 提取學號，即檔案名稱
        print(f"Compiling and running {java_file} with student ID {student_id}...")
        
        # 編譯該Java檔案
        compile_command = f"javac {file_path}"
        os.system(compile_command)
        # os.chdir("files")
        for i in range(1,11):
            # 執行編譯後的Java檔案
            # run_command = f"java assignment.A04_{student_id} < ../{i}.in > {i}.out"
            run_command = f"java -cp ./files/ {student_id} < ./files/{i}.in > ./files/{i}.out"
            os.system(run_command)
def main():
    compile_and_run_files_in_folders("./files")

if __name__ == "__main__":
    main()