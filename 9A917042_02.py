student = {}
# a = ()
for i in range(1):
    id = input("請輸入您的學號:")
n = input("請輸入您的姓名:")
c = float(input("請輸入您的國文成績:"))
m = float(input("請輸入您的數學成績:"))
i = float(input("請輸入您的電腦成績:"))

student = {"sid": id, "sname": n, "fchina": c, "fmath": m, "finfo": i}
sum = round(c + m + i, 2)
a = round(sum / 3, 2)
print("-" * 30)

print(f"{n}({id})同學您好:\n以下是您的各科成績與分數評定\n\n")
print(f"國文:{c} / 數學:{m} / 電腦:{i}")
print(f"總分:{sum}  / 平均:{a}")

print("-" * 30)
if a >= 60:
    print("成績判定:合格")
else:
    print("成績判定:不合格")
