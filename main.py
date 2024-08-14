import re

def remove_index_and_time(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正則表達式移除索引和時間戳
    cleaned_content = re.sub(r'\d+\s*\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', content)
    
    # 移除多餘的空行
    cleaned_content = re.sub(r'\n+', '\n', cleaned_content).strip()
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

# 使用示例
remove_index_and_time(r'C:\yt\INTEL\DATA2.srt', r'C:\yt\INTEL\cleaned_subtitles2.srt')