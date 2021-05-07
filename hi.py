import random

#Khởi tạo giá trị nguoif chơi
a = input("Nhập đam / la / keo: ")

#Khởi tạo giá trị máy
b = random.randint(0,2)
if b == 0:
	b = "dam"
elif b == 1:
	b = "la"
else:
	b = "keo"

#so sánh kết quả
if a == b:
	c = "Hòa"

else:
	if a == "dam":
		if b == "la":
			c = "Thua"
	else:
		c = "Thắng"

	if a == "la":
		if b == "dam":
			c = "Thắng"
	else:
		c = "Thua"

	if a == "keo":
		if b == "la":
			c = "Thắng"
	else:
		c = "Thua"
		
		

print("------")
print("Bạn chọn: " + a)
print("Máy chọn: " + b)
print("Kết quả: " + c)
print("------")