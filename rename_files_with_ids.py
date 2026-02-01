import os
import shutil
import re

# Mapping based on the user's provided list and matching files in the workspace
# Only including entries relevant to the files seen (and some likely unicode decodings)
TITLE_TO_ID = {
    "Assign Cookies": "A001", "Pascal's Triangle": "A002", "Plus One": "A003",
    "개": "A184",
    "고양이": "A183",
    "윤년": "A187",
    "수 찾기": "C063",
    "수_찾기": "C063", # Underscore variant
    "A+B - 3": "A191",
    "A_B_3": "A191", # Underscore variant
    "A+B - 5": "A229",
    "A_B_5": "A229",
    "OX퀴즈": "A052",
    "개수 세기": "A196",
    "단어 공부": "A045",
    "단어 길이 재기": "A203",
    "두 수 비교하기": "A185",
    "별 찍기 1": "A195", # Matches A195 별 찍기 - 1
    "사분면 고르기": "A188",
    "시험 성적": "A186",
    "오늘 날짜": "A224",
    "평균은 넘겠지": "A008",
    "나머지": "A034", 
    "괄호": "B183", 
    "별 찍기 1": "A195", # Matches A195 별 찍기 - 1
    "팩토리얼": "A228",
    "과제 안 내신 분": "A234", # Matches A234 과제 안 내신 분..?
    "꼬마 정민": "A182",
}

# Hex-encoded filename handling
# Example: _uac1c -> \uac1c -> 개
def decode_hex_filename(filename):
    # Matches patterns like _uXXXX
    # We replace _u with \u and then decode unicode-escape
    if "_u" in filename and not filename.startswith('.'):
        try:
            # Replace _u with \u
            temp = filename.replace("_u", "\\u")
            # If the filename was like _uac1c.bin, temp is \uac1c.bin
            # ASCII to unicode
            decoded = temp.encode('utf-8').decode('unicode-escape')
            return decoded
        except Exception as e:
            return filename
    return filename

def clean_title(title):
    # Remove extensions and normalize
    base = os.path.splitext(title)[0]
    # Replace spaces with underscores or vice versa for matching?
    # Strategy: Normalize to matched key format
    return base

def main():
    root_dir = "/Users/kim-yejun/2026_baekjoon"
    
    # Walk through directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories
        if '/.' in dirpath:
            continue
            
        for filename in filenames:
            if filename.startswith('.'):
                continue
                
            original_path = os.path.join(dirpath, filename)
            
            # 1. Try to decode hex filenames
            decoded_name = decode_hex_filename(filename)
            if decoded_name != filename:
                print(f"[Info] Decoded {filename} -> {decoded_name}")
                # We interpret the file as if it had the decoded name
                search_name = decoded_name
            else:
                search_name = filename
                
            # 2. Check if already has ID
            # Pattern: Letter + 3 digits + ...
            if re.match(r'^[A-C]\d{3}', search_name):
                # print(f"[Skip] Already renamed: {filename}")
                continue
                
            # 3. Match against DB
            base_name = os.path.splitext(search_name)[0]
            # Normalize: replace underscores with spaces for matching
            name_variants = [
                base_name,
                base_name.replace('_', ' '),
                base_name.replace(' ', '_')
            ]
            
            problem_id = None
            matched_title = None
            
            for variant in name_variants:
                if variant in TITLE_TO_ID:
                    problem_id = TITLE_TO_ID[variant]
                    matched_title = variant
                    break
            
            # Special case for "괄호"
            if "괄호" in base_name and not problem_id:
                # Ambiguity check
                pass

            if problem_id:
                # Construct new name
                # Format: ID_Title.extension
                # We usually want to keep the original extension
                _, ext = os.path.splitext(filename)
                
                # If we decoded the name, should we use the decoded chars in the new name?
                # User prompted "Rename existing files".
                # If original was `_uac1c.bin` (dog), and we map "개" -> "A184",
                # New name should probably be `A184_개.bin` or `A184_uac1c.bin`?
                # Usually users want readable names. Let's propose `A184_개.bin`.
                
                # Use the matched title from dictionary keys if possible, or the decoded name.
                # Actually, using the matched_title from keys is safer for consistency.
                safe_title = matched_title.replace(" ", "_")
                new_filename = f"{problem_id}_{safe_title}{ext}"
                new_path = os.path.join(dirpath, new_filename)
                
                if original_path != new_path:
                    print(f"[RENAME] {filename} -> {new_filename}")
                    # Uncomment to execute
                    os.rename(original_path, new_path)
            else:
                # print(f"[Unmatched] {filename}")
                pass

if __name__ == "__main__":
    main()
