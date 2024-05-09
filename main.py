import subprocess
import sys

def main(zip_filename):
    # Step 1: Unzip and move testcases
    subprocess.call(['python', 'a07_unzip.py', zip_filename])
    
    # Step 2: Comment to remove package
    subprocess.call(['python', 'comment.py'])

    # Step 3: Compile and Run
    subprocess.call(['python', 'compile_run.py'])
    
    # Step 4: Move the result txt files
    subprocess.call(['python', 'move.py'])

    # # Step 5: Compare
    subprocess.call(['python', 'compare.py'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python full_process.py <zip_file>")
    else:
        main(sys.argv[1])