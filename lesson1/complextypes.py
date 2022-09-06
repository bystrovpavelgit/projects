lst = [3, 5, 7, 9, 10.5]
print(lst)

lst.append("Python")
print(len(lst))
print(lst[0])
print(lst[-1])
print(lst[2:5])
lst.remove("Python")

d = {"city": "Москва", "temperature": "20"}
print(d["city"])
d["temperature"] = "15" 
print(d)

if "country" in d:
   print("Yes")
print(d.get("country", "Россия"))
d["date"] = "27.05.2019"
print(len(d))
 
