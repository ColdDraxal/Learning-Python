def rev(a,b=0):
    if a==0:
        return b
    return rev(a//10,b*10+a%10)
# print(f"This function is imported from {__name__}")
if __name__=="__main__":
    print(rev(12345))