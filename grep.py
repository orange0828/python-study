import sys

def search(path, keyword):
    res = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, start=1):
                line = line.rstrip("\n")
                if keyword in line:
                    res.append((line_num, line))
    except FileNotFoundError:
        # 文件找不到，返回特殊标记或者直接抛，这里我们返回None，main里处理
        return None
    return res


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: py grep.py 文件路径 关键词")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]
    result = search(file_path, key)

    if result is None:
        print(f"文件不存在：{file_path}")
        sys.exit(1)

    # 打印放到main里
    for num, text in result:
        print(f"{num}: {text}")
    print(f"共匹配 {len(result)} 行")

