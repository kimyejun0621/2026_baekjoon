import os
import random
import re

def rename_files():
    # Target directory is current directory
    directory = "."
    
    # regex to match files ending with 2025_<4 digits>.py
    # Example: A106김예준_2025_0721.py
    # We look for "2025" and a date suffix.
    
    files = os.listdir(directory)
    count = 0
    
    for filename in files:
        if filename.endswith(".py") and "2025" in filename:
            # New filename construction
            new_filename = filename.replace("2025", "2026")
            
            # Find the date part (last 4 digits before .py) using regex
            # Assuming format like ..._0721.py
            match = re.search(r'_(\d{4})\.py$', new_filename)
            
            if match:
                old_date = match.group(1)
                new_date = random.choice(['0116', '0117', '0118'])
                new_filename = new_filename[:match.start(1)] + new_date + new_filename[match.end(1):]
                
                # Check for 0721/old date anywhere else if needed, but request said: "날짜(0721)같은거..."
                # The filename format looks like: A106김예준_2025_0721.py
                # replace 2025 -> 2026 implies A106김예준_2026_0721.py
                # then replace 0721 -> random
                
            try:
                os.rename(filename, new_filename)
                print(f"Renamed: {filename} -> {new_filename}")
                count += 1
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

    print(f"Total files renamed: {count}")

if __name__ == "__main__":
    rename_files()
