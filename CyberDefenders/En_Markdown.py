import base64
import re

def convert_image_to_base64(image_path):
    # Đọc file ảnh và mã hóa thành Base64
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def process_markdown_file(input_file, output_file):
    # Đọc nội dung file Markdown
    with open(input_file, "r", encoding="utf-8") as md_file:
        content = md_file.read()

    # Tìm tất cả các đường dẫn ảnh trong Markdown
    image_pattern = r"!\[.*?\]\((.*?)\)"
    matches = re.findall(image_pattern, content)

    # Thay thế từng đường dẫn ảnh bằng chuỗi Base64
    for image_path in matches:
        try:
            base64_string = convert_image_to_base64(image_path)
            base64_image = f"data:image/png;base64,{base64_string}"
            content = content.replace(image_path, base64_image)
        except FileNotFoundError:
            print(f"Không tìm thấy file ảnh: {image_path}")

    # Ghi nội dung mới vào file đầu ra
    with open(output_file, "w", encoding="utf-8") as output_md_file:
        output_md_file.write(content)

    print(f"Xuất file Markdown với ảnh nhúng thành công: {output_file}")

# Đường dẫn file Markdown gốc và file đầu ra
input_markdown = "Cyber ​​Security Certificate.md"
output_markdown = "Cyber ​​Security Certificate.md_Encoded.md"

# Xử lý file Markdown
process_markdown_file(input_markdown, output_markdown)