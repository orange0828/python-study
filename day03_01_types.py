# grep.py
import sys

def search(path, keyword):
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                line = line.rstrip("\n")
                if keyword in line:
                    print(f"{line_num}: {line}")
                    count += 1
        print(f"共匹配 {count} 行")
    except FileNotFoundError:
        print(f"文件不存在：{path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：py grep.py 文件路径 关键词")
    else:
        file_path = sys.argv[1]
        key = sys.argv[2]
        search(file_path, key)
