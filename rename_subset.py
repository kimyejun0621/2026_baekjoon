import os
import random

def main():
    base_dir = "/Users/kim-yejun/2026_baekjoon"
    # Target range: A0040 to A0061
    # Note: user created files like A0040, A0041 (4 digits) or A040 (3 digits)?
    # Directory list shows "A0040_김예준_20260129" (already renamed?), "A0041", "A0042"... "A0061".
    # And also "a0047" (lowercase).
    
    # We need to map them to A040, A041... (3 digits)
    # Date choices: 0128, 0129, 0130.
    dates = ["0129", "0128", "0130"]
    
    files = os.listdir(base_dir)
    
    for filename in files:
        # Check if file starts with A0040...A0061 or a0047
        # Normalize comparison
        upper_name = filename.upper()
        
        # Check for A00xx pattern
        if upper_name.startswith("A00") and  len(filename) >= 5:
            try:
                # Extract number part
                num_part = upper_name[3:5] # e.g. A0041 -> 41
                num_val = int(num_part)
                
                if 40 <= num_val <= 61:
                    # Construct new name
                    # ID should be A0xx (3 digits) = A0 + num_part
                    new_id = f"A0{num_part}"
                    
                    # Pick random date
                    date_suffix = random.choice(dates)
                    
                    # New filename
                    new_name = f"{new_id}_김예준_2026{date_suffix}.py"
                    
                    old_path = os.path.join(base_dir, filename)
                    new_path = os.path.join(base_dir, new_name)
                    
                    if old_path != new_path:
                        print(f"Renaming {filename} -> {new_name}")
                        os.rename(old_path, new_path)
            except ValueError:
                continue
                
        # Special case for A0040 (which might be A0040_김예준_20260129)
        # The user's manually created file `A0040_김예준_20260129` matches the pattern `A0040`.
        # Code above handles it if it starts with A0040.
        
        # Special case for 'a0047'
        if filename == "a0047":
            new_name = f"A047_김예준_2026{random.choice(dates)}.py"
            old_path = os.path.join(base_dir, filename)
            new_path = os.path.join(base_dir, new_name)
            print(f"Renaming {filename} -> {new_name}")
            os.rename(old_path, new_path)

if __name__ == "__main__":
    main()
