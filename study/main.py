for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
            print(num,"是一个质数")
