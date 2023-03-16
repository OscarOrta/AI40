import requests
import json

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
}

link= 'https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248e35cb3f806ce4f518ac9aace37c6bbfa&start=-98.40488,20.07636&end=-98.38588,20.07622,'
punto_inicio =input("Ingresa el punto de partida: ")
new_link=link.replace("-98.40488,20.07636",punto_inicio)
punto_final =input("Ingresa el punto de llegada: ")
new_link0=new_link.replace("-98.38588,20.07622",punto_final)
metodo=input("Ingresa el método de trasporte: ")
new_link1=new_link0.replace("driving-car", metodo)
call = requests.get(new_link1, headers=headers)

#p1=int(input("Cordenada uno: "))
#p2=int(input("Cordenada dos: "))

d = json.loads(call.text)
def impresiones():
    for i in d ["features"]:
        r = i["properties"]["segments"]
        for a in r:
            dis= a["distance"]/1000
            dur= a["duration"]/60
            print ("Distacia ",dis,"km ,","Duración ",dur,"minutos")
    p1=d["metadata"]["query"]["coordinates"][0]
    p2=d["metadata"]["query"]["coordinates"][1]
    print("Punto de inicio: ",p1, "Punto final: ", p2)
    print("Método de transporte: ",d["metadata"]["query"]["profile"])
impresiones()




"""#print(call.status_code, call.reason)
d = call.text 
print("R= ", end=" ")
for i in d[3023:3104]:
    print(i, end=" ")

print("")

print("R= ", end=" ")
for i in d[134:168]:
    print(i, end=" ")"""