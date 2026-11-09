# 题 3 · 字符和编码
# 这题考：字符与编码的双向转换
# ord：字符 -> 编码；chr：编码 -> 字符。两者互逆。

print(ord('A'))                # 65   'A' 的编码
print(chr(97))                 # a    编码 97 对应的字符
print(ord('d') - ord('a'))     # 3    'd' 比 'a' 大 3
print(chr(ord('A') + 3))       # D    'A' 往后数 3 个字母
