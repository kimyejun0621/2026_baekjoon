import os

def main():
    log_path = "/Users/kim-yejun/2026_baekjoon/undo_log.txt"
    root_dir = "/Users/kim-yejun/2026_baekjoon"
    
    if not os.path.exists(log_path):
        print(f"Error: {log_path} not found.")
        return

    with open(log_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        if "[RENAME]" in line:
            # Parse line: [RENAME] original -> new
            # Example: [RENAME] _uac1c.bin -> A184_개.bin
            parts = line.split(" -> ")
            if len(parts) != 2:
                continue
                
            original_name = parts[0].replace("[RENAME] ", "").strip()
            new_name = parts[1].strip()
            
            # The files are currently named `new_name`. We want to rename them back to `original_name`.
            # We need to find `new_name` in the directory structure.
            # Since files might be in subdirectories, we walk search or assume they are where we found them?
            # The log didn't print full paths, just filenames.
            # We will walk the directory to find the file `new_name`.
            
            file_found = False
            for dirpath, dirnames, filenames in os.walk(root_dir):
                if new_name in filenames:
                    current_path = os.path.join(dirpath, new_name)
                    original_path = os.path.join(dirpath, original_name)
                    print(f"Reverting: {new_name} -> {original_name}")
                    try:
                        os.rename(current_path, original_path)
                        file_found = True
                    except Exception as e:
                        print(f"Error renaming {new_name}: {e}")
                    # Break after finding one? Warning: Duplicate filenames exist in different folders.
                    # The log didn't specify path. This might rename ALL `new_name` to `original_name` in all folders.
                    # In this user's case, duplicates were renamed identically, so this is likely correct/desired behavior.
            
            if not file_found:
                print(f"Warning: Could not find {new_name} to revert.")

if __name__ == "__main__":
    main()
