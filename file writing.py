"""d=open("draxal.txt") # its in default mode and if i write d=open("draxal.txt","r") it wont change
#r means reading mode which we already are in and we can have 2 readind mode which is rb binary reading
#mode and rt which is default rt text reading mode. if we keep it empty it shows us rt as default.
# content=d.read()
# print(content)
# content=d.read(5) # if we keep read() empty it will read all the content of the file
# print(content)
# content=d.read(2) # prints from where it cut off from d.read(5) for eg "draxa l "
# print(content)
# for line in d:
#     print(line,end="")
print(d.readline())
print(d.readline())
print(d.readline())
# print(d.readlines())
d.close()
"""


# with open("draxal2.txt","w") as d:
#     d.write("K xa Hajur\n")
# with open("draxal2.txt","a") as d:
#     d.write("Thikai xa ni\n")
# with open("draxal2.txt","r+") as d:
#  d.write("Darpan Basyal is my name.")
with open("draxal2.txt","r") as d:
    # for line in d:
    #     print(line,end="")
    print(d.tell())
    print(d.readline(),end="")
    d.seek(7)
    print(d.tell())
    print(d.readline(),end="")
    print(d.tell())