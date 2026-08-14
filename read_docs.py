# -*- coding: utf-8 -*-
import docx
import os

base_path = r"C:\Users\DD\Desktop\DD\DDSKILL\知识库"

for f in os.listdir(base_path):
    if f.endswith('.docx'):
        print("=" * 60)
        print("文件: " + f)
        print("=" * 60)
        try:
            doc = docx.Document(os.path.join(base_path, f))
            for para in doc.paragraphs:
                if para.text.strip():
                    print(para.text)
        except Exception as e:
            print("读取错误: " + str(e))