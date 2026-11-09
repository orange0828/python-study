side_a, side_b, side_c = map(float, input("请输入三条边长：").split())
if side_a > 0 and side_b > 0 and side_c > 0 and side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
	print("可以构成三角形")
	print("周长：", side_a + side_b + side_c)
	semiperimeter = (side_a + side_b + side_c) / 2
	area = (semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) * (semiperimeter - side_c)) ** 0.5
	print("面积：", area)
	print("是等边三角形:", side_a == side_b == side_c)
else:
	print("不能构成三角形")
	
	
	
