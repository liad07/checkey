import requests

response = requests.get("https://liad07.github.io/checkey/license.txt")
data = response.text
data=data.split("\n")
inp=input("enter license\n")
count=0
for i in range (0, len(data)):
    data[i]=data[i].replace("\r","")
    if inp==data[i]:
        count+=1
        break
if count==1:
    print("good key")
else:
    print("Incorrect key")