def divide(a,b):
    try:
        return a/b
    except Exception as e:
        return e


print(divide(1,0))
print("End of Program")