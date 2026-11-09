# 题 2 · 进制转换
# 这题考：把外来文本按指定进制解析成数字
# 关键：base 描述的是「输入字符串的进制」，输出永远是十进制

binary_text = '1010'      # 二进制
octal_text = '777'        # 八进制
hex_text = 'FF'           # 十六进制

print(int(binary_text, 2))    # 10
print(int(octal_text, 8))     # 511
print(int(hex_text, 16))      # 255
