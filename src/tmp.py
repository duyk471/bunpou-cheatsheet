import re
import os

# Regex match đường dẫn trong Markdown
pattern = re.compile(r'(?<=\]\()([^)]+)')

def encode_spaces(match):
    return match.group(0).replace(' ', '%20')

def process_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updated_content = re.sub(pattern, encode_spaces, content)

    # Ghi đè nội dung đã sửa
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                print(f'🔧 Đang xử lý: {full_path}')
                process_markdown_file(full_path)

# Thay đường dẫn này bằng thư mục bạn muốn quét
target_folder = './'
process_folder(target_folder)
