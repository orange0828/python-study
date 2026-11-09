# 题 4 · 华氏转摄氏（验收题）
# 这题考：input 读入 + float 转换 + 格式化输出
# 公式：C = (F - 32) * 5 / 9
# 输入 212 应输出 100.0

fahrenheit = float(input("请输入华氏温度："))
celsius = (fahrenheit - 32) * 5 / 9

print(f"对应的摄氏温度为：{celsius:.1f}")
