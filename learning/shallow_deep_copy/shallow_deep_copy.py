"""
python的赋值、浅拷贝与深拷贝
"""
import copy

# origin
a = ["Zhang", 28, ["Python", "C#", "JavaScript"]]
b = ["Li", 32, ["Java", "C"]]
b = a
# c = list(a)      # 浅拷贝
# c = a[:]                 # 浅拷贝
# c = a.copy()          # 浅拷贝
c = copy.copy(a)        # 浅拷贝
d = copy.deepcopy(a)    # 深拷贝

print(f"a={a},", f"identity a={id(a)}, {[id(ele) for ele in a]}, {[id(ele) for ele in a[2]]}")
print(f"b={b},", f"identity a={id(b)}, {[id(ele) for ele in b]}, {[id(ele) for ele in a[2]]}")
print(f"c={c},", f"identity a={id(c)}, {[id(ele) for ele in c]}, {[id(ele) for ele in a[2]]}")
print(f"d={d},", f"identity a={id(d)}, {[id(ele) for ele in d]}, {[id(ele) for ele in a[2]]}")

# change
a[0] = "Wang"
a[2].append("Go")

print("=====================After change=========================")
print(f"a={a},", f"identity a={id(a)}, {[id(ele) for ele in a]}, {[id(ele) for ele in a[2]]}")
print(f"b={b},", f"identity a={id(b)}, {[id(ele) for ele in b]}, {[id(ele) for ele in a[2]]}")
print(f"c={c},", f"identity a={id(c)}, {[id(ele) for ele in c]}, {[id(ele) for ele in a[2]]}")
print(f"d={d},", f"identity a={id(d)}, {[id(ele) for ele in d]}, {[id(ele) for ele in a[2]]}")