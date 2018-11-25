a = "xyz";
b = "abxc"

print(a + b)
print(list(a)[1:3])
print(b*10)

if "x" in list(b):
    print("ok");
else:
    print("not ok")

print("a" in a)
print("a" in b)