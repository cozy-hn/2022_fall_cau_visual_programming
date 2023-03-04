def change(degree):
    print("섭씨 %.1f도는 화씨 %.1f도" %(degree, (degree*1.8)+32))
    print("화씨 %.1f도는 섭씨 %.1f도" %(degree, (degree-32)/1.8))

print("온도? ", end="")
degree=float(input())
change(degree)