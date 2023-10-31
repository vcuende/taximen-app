import json
import math
import os, uuid


# ids = 0
# with open('back/users.json') as usersR:
#     data = json.load(usersR)
#     for u in data:
#         ids = u['ID']+1
#     usersR.close()
# with open('back/users.json', 'w', encoding='UTF-8') as users:
#     user = {'ID': ids, 'NOMBRE': 'Alberto', 'CORREO': 'gondor@gmail.com', 'TELEFONO': '693258741', 'TARJETA': '789654123654'}
#     data.append(user)
#     json.dump(data, users, indent = 4, separators=(',',': '))
#     print(user["NOMBRE"])
#     users.close()



# with open('back/taxis.json', encoding='UTF-8') as taxis:
#     data = json.load(taxis)
#     print(data)

    # solicitud = {
    # "ID": 3,
    # "NOMBRE": "Sexualizator",
    # "ORIGEN": "Madrid",
    # "DESTINO": "Isengard",
    # "FECHA": "30/11/2021",
    # "HORA": "23:47"
    # }

    # with open('back/solicitudes.json') as solicitudesR:
    # data = json.load(solicitudesR)
    # solicitudesR.close()
    # with open('back/solicitudes.json', 'w') as solicitudes:
    # data.append(solicitud)
    # json.dump(data, solicitudes, indent = 4, separators=(',',': '))
    # solicitudes.close()


    # posXTaxi = 0
    # posYTaxi = 0
    # posXDes = 0
    # posYDes = 0
    # candidato = 0
    # distancia = 0
    # with open('back/destinos.json') as destinos:
    #     data2 = json.load(destinos)
    #     for d in data2:
    #         if d['NOMBRE'] == solicitud['DESTINO']:
    #             posXDes = d['POSX']
    #             posYDes = d['POSY']
    # destinos.close()
    # with open('back/taxis.json') as taxis:
    # data3 = json.load(taxis)
    # for t in data3:
    #     for d in data2:
    #         #Sacamos coordenadas Taxi
    #         if d['NOMBRE'] == t['UBICACION']:
    #             posXTaxi = d['POSX']
    #             posYTaxi = d['POSY']
    #     dProvisional = math.sqrt(math.pow(abs(posXDes - posXTaxi), 2) + math.pow(abs(posYDes - posYTaxi), 2))
    #     if distancia == 0:
    #         distancia = dProvisional
    #         candidato = t['ID']
    #     if dProvisional < distancia:
    #         distancia = dProvisional
    #         candidato = t['ID']
    # taxis.close()
    # print(solicitud['DESTINO'] + ":", "Taxi con ID:", candidato)

    # asignacion = {
    #     "ID": 0,
    #     "NOMBRE": solicitud['NOMBRE'],
    #     "ID_TAXI": candidato,
    #     "ESTADO": "Activa"
    # }

    # ids = 0
    # with open('back/asignaciones.json') as asignacionesR:
    # data4 = json.load(asignacionesR)
    # for a in data4:
    #     ids = a['ID']+1
    # asignacion['ID'] = ids
    # asignacionesR.close()
    # with open('back/asignaciones.json', 'w') as asignaciones:
    # data4.append(asignacion)
    # json.dump(data4, asignaciones, indent = 4, separators=(',',': '))
    # asignaciones.close()


# with open('back/solicitudes.json') as solicitudes:
#         data = json.load(solicitudes)
#         for s in data:
#             if s['VALIDADA'] == False:
#                 print("NOMBRE:", s['NOMBRE'], "ORIGEN:",  s['ORIGEN'], "DESTINO:", s['DESTINO'])
# solicitudes.close()

# with open('users.json', 'r', encoding='UTF-8') as users:
#     data = json.load(users)
#     contador = 0
#     for u in data:
#         contador += 1
#         if u['CORREO'] == "4ntorg@gmail.com" and u['PASSWORD'] == "12345":
#             if u['ACTIVO'] == False:
#                 u['ACTIVO'] = True
# users.close()
# tempfile = os.path.join(os.path.dirname('users.json'), str(uuid.uuid4()))
# with open(tempfile, 'w') as users:
#     json.dump(data, users, indent=4)
# os.remove('users.json')
# os.rename(tempfile, 'users.json')

solicitud = {
    "ID": 0,
    "VALIDADA" : False
}

with open('back/solicitudes.json', encoding='UTF-8') as solicitudes:
        data = json.load(solicitudes)
        for s in data:
            if s['ID'] == solicitud['ID']:
                s['VALIDADA'] = True
                break
solicitudes.close()
tempfile = os.path.join(os.path.dirname('back/solicitudes.json'), str(uuid.uuid4()))
with open(tempfile, 'w') as solicitudes:
    json.dump(data, solicitudes, indent=4)
os.remove('back/solicitudes.json')
os.rename(tempfile, 'back/solicitudes.json')
solicitudes.close()