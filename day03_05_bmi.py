# 题 5 · BMI 计算器
# 这题考：两次读入 + 括号改变优先级 + 两位小数
# 公式：BMI = 体重 / 身高^2
# 身高 1.75、体重 70 应输出 22.86
#
# 注意：分母必须加括号。
# weight / height * height  会先除后乘，结果等于 weight 本身（错）
# weight / (height * height) 才是对的

height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（公斤）："))

bmi = weight / (height * height)

print(f"BMI指数为：{bmi:.2f}")
