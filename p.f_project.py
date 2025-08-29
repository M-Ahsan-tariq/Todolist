def dict(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")
dict(name = "ahsan ", age = 19 , GPA = 3.64)
dict = {"name":"ahsan","age":18,"GPA":3.64}
for key, value in dict.items():
    print(f"{key} = {value}")
def names(*names):
    for i in names:
        print(i,end=" ,")
names("ahsan","ali","madhav")