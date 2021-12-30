from datetime import datetime
import colorama

# # set windows for cmd and powershell.
# colorama.init()

# k = int(input("กรอกความยาวต้นไม้  :  (limit 20)"))
# i = 0
# while i <= k:
#     if(i==0):
#         print("            "+colorama.Fore.YELLOW +'***2021 --->>>>> 2022***')
#         print("            "+colorama.Fore.YELLOW +'Now',datetime.now())
#     print("      "+colorama.Fore.GREEN +'*'*i)
#     i += 1
# print(colorama.Fore.RED + "Level 1")


# for p in range(i):
#  print((i-p) * ' ' +colorama.Fore.GREEN+'*'*p)


# print(colorama.Back.WHITE+colorama.Fore.RED + "Level 2 Happy Newyear"+colorama.Back.RESET)

print(colorama.Fore.YELLOW +"สุขสันต์วันขึ้นปีใหม่ 2022 by Ongarj Dev")

# set windows for cmd and powershell.
colorama.init()

num = 10
i = 0
while i < num:
    i += 1
    space = num - i
    for s in range(space):
        print(colorama.Fore.LIGHTGREEN_EX+" ", end='')
    for n in range(1, (num - space) + 1):
        print(n, end='')
    for n in reversed(range(1, i)):
        print(n, end='')
    print("")
z = num/1.5
print(' '*int(z)+"|     |")
print(' '*int(z)+"|     |")
print(' '*int(z)+"|     |")

print(colorama.Fore.LIGHTCYAN_EX+"ปีเก่ากำลังจะผ่านไป  ปีใหม่กำลังจะผ่านมา")
print("ขณะนี้วันที่",datetime.now())