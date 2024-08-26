from datetime import datetime

users = [{ 'code' : "Usuario",'date' : "2005-01-01"},{ 'code' : "Usuario2",'date' : "2004-02-02"},{ 'code' : "Usuario3",'date' : "2004-03-03"}]

listDate = []


for user in users:
    listDate.append({"code": user["code"], "date": user["date"]})

listDate_sorted = sorted(listDate, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))

print("Usuários ordenados:")
for user in listDate_sorted:
    print("usuario:", user["code"], "data:", user["date"])
