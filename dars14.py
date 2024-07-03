import json
#1-misol
data = {"Model" : "Gentra", "Rang" : "Qizil", "Yil":2024, "Narh":15000}
data_json = json.dumps(data)
print(data_json)

#2-misol
talaba_json = """{"ism":"Shaydo","familiya":"Bekturdiyeva","tyil":2009}"""
talaba = json.loads(talaba_json)
print(f"Talabaning ismi: {talaba['ism']}")
print(f"Talabaning familiyasi: {talaba['familiya']}")
print(f"Talabaning yili: {talaba['tyil']}")

#3-misol
with open('data.json','w') as f:
    json.dump(data,f)

with open('talaba.json','w') as f:
    json.dump(talaba,f)
