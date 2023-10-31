import os
try:
    from fastapi import FastAPI
except:
    os.system("pip install fastapi")
    import fastapi
from fastapi.middleware.cors import CORSMiddleware
import smtplib
import json
import math
import os, uuid

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your system."}



@app.get("/taxis", tags=["taxis"])
async def getTaxis() -> dict:
    with open('back/taxis.json', encoding='UTF-8') as taxis:
        data = json.load(taxis)
        return { "data": data }



@app.post("/user", tags=["users"])
async def getUsername(correo: dict) -> dict:
    with open('back/users.json', encoding='UTF-8') as users:
        data = json.load(users)
        userName = ""
        for u in data:
            if u['CORREO'] == correo['CORREO']:
                return { "message": u['NOMBRE'] }



@app.post("/activate", tags=["users"])
async def getActivation(user: dict) -> dict:
    message = ""
    with open('back/users.json', encoding='UTF-8') as users:
        data = json.load(users)
        contador = 0
        for u in data:
            contador += 1
            if u['CORREO'] == user['CORREO']:
                if u['PASSWORD'] == user['PASSWORD']:
                    if u['ACTIVO'] == False:
                        u['ACTIVO'] = True
                        message = "Su cuenta ha sido activada correctamente"
                        break
                    else:
                        message = "Su cuenta ya ha sido activada"
                else:
                    message =  "La combinación que ha introducido no es correcta"
    users.close()
    tempfile = os.path.join(os.path.dirname('back/users.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as users:
        json.dump(data, users, indent=4)
    os.remove('back/users.json')
    os.rename(tempfile, 'back/users.json')
    users.close()
    return { "message": message }



@app.post("/login", tags=["login"])
async def login(login: dict) -> dict:
    wrongPwd = False
    nonExist = True
    notActive = False
    password = login['PASSWORD']
    correo = login['CORREO']
    with open('back/users.json', encoding='UTF-8') as users:
        data = json.load(users)
        for u in data:
            if correo == u['CORREO']:
                nonExist = False
                if password != u['PASSWORD']:
                    wrongPwd = True
                if u['ACTIVO'] != True:
                    notActive = True
    if nonExist:
        return { "message": "El usuario introducido no existe" }
    if wrongPwd:
        return { "message": "La contraseña introducida es incorrecta" }
    if notActive:
        return { "message": "Por favor active primero su usuario" }
    users.close()
    return { "message": "Logged"}



@app.post("/users", tags=["users"])
async def addUsers(user: dict) -> dict:
    ids = 0
    #Vamos a leer los IDs de cada usuario para saber que id poner al nuevo
    with open('back/users.json', encoding='UTF-8') as usersR:
        data = json.load(usersR)
        for u in data:
            ids = u['ID']+1
            if u['CORREO'] == user['CORREO']:
                return { "message": "El correo introducido ya existe en el sistema" }
        user["ID"] = ids
    usersR.close()
    with open('back/users.json', 'w', encoding='UTF-8') as users:
        data.append(user)
        json.dump(data, users, indent = 4, separators=(',',': '))
    users.close()
    #Envio correo
    #Conectamos a gmail
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login("taximenis2","Taximen123")
    
    # Creamos correo
    remitente = "Desde TAXIMEN <registro@taximen.org>" 
    asunto = "Registro en TAXIMEN!" 
    mensaje = """Hola """+ user["NOMBRE"] +"""!\n\nConfirme que se ha registrado en TAXIMEN con el telefono """+ user["TELEFONO"] +""" y el numero de tarjeta """ + user["TARJETA"] +""". """ + "Pinchando en este enlace: http://localhost:3000/activate"
    email = "Subject: {}\n\n{}".format(asunto, mensaje)

    #Enviamos correo y cerramos conexión con gmail
    server.sendmail("taximenis2", user["CORREO"], email)
    server.quit()
    print(user)
    print(users)
    return {
        "message": { "Usuario añadido correctamente, por favor, compruebe su email" }
    }



@app.post("/solicitudes", tags=["solicitudes"])
async def addSolicitud(solicitud: dict) -> dict:
    # Calculamos Asignazione
    posXTaxi = 0
    posYTaxi = 0
    posXDes = 0
    posYDes = 0
    candidato = 0
    distancia = -1
    existeDestino = False
    #Vemos si existe el destino
    with open('back/destinos.json') as destinos:
            data2 = json.load(destinos)
            for d in data2:
                if d['NOMBRE'] == solicitud['DESTINO']:
                    existeDestino = True
                    posXDes = d['POSX']
                    posYDes = d['POSY']
                    break
    destinos.close()
    #Si no existe el destino, mandamos el error bien bacano
    if existeDestino == False:
        return { "message": "No existe el destino" }
    #Anadimos solicitud
    ids = 0
    with open('back/solicitudes.json') as solicitudesR:
        data = json.load(solicitudesR)
        for s in data:
            ids = s['ID']+1
        solicitud["ID"] = ids
    solicitudesR.close()
    #Vemos que taxi esta mas cerca con nuestro algoritmo bien refachero
    with open('back/taxis.json') as taxis:
        data3 = json.load(taxis)
        for t in data3:
            if t['ESTADO'] == "Libre":
                for d in data2:
                    #Sacamos coordenadas Taxi
                    if d['NOMBRE'] == t['UBICACION']:
                        posXTaxi = d['POSX']
                        posYTaxi = d['POSY']
                dProvisional = math.sqrt(math.pow(abs(posXDes - posXTaxi), 2) + math.pow(abs(posYDes - posYTaxi), 2))
                if distancia == -1:
                    distancia = dProvisional
                    candidato = t['ID']
                if dProvisional < distancia:
                    distancia = dProvisional
                    candidato = t['ID']
    taxis.close()
    if candidato == -1:
        return { "message": { "No hay taxis libres" } 
        }
    print(solicitud['DESTINO'] + ":", "Taxi con ID:", candidato)
    solicitud['ID_TAXI'] = candidato
    with open('back/solicitudes.json', 'w') as solicitudes:
        data.append(solicitud)
        json.dump(data, solicitudes, indent = 4, separators=(',',': '))
    solicitudes.close()
    return { 
        "message": "Solicitud añadida correctamente", "data": ids 
    }



@app.get("/solicitudes", tags=["solicitudes"])
async def getSolicitudes() -> dict:
    with open('back/solicitudes.json') as solicitudes:
        data = json.load(solicitudes)
    solicitudes.close()
    return { "data": data }



@app.get("/informe", tags=["solicitudes"])
async def getInforme() -> dict:
    with open('back/solicitudes.json') as solicitudes:
        data = json.load(solicitudes)
        if not data:
            return { "message": "No hay solicitudes, pruebe a añadir una" }
    solicitudes.close()
    return { "message": "OK", "data": data }



@app.get("/destinos", tags=["destinos"])
async def getDestinos() -> dict:
    with open('back/destinos.json') as destinos:
        data = json.load(destinos)
    destinos.close()
    return { "data": data }


@app.post("/validar", tags=["solicitudes"])
async def validarAsignacion(solicitud: dict) -> dict:
    res = "No se ha podido validar"
    with open('back/solicitudes.json', encoding='UTF-8') as solicitudes:
        data = json.load(solicitudes)
        with open('back/taxis.json', encoding='UTF-8') as taxis:
            data2 = json.load(taxis)
        for s in data:
            if s['ID'] == solicitud['ID']:
                if(s['VALIDADA']) == False:
                    for t in data2:
                        if t['ID'] == s['ID_TAXI']:
                            if(t['ESTADO'] == "Libre"):
                                t['ESTADO'] = "Ocupado"
                                t['DESTINO'] = s['DESTINO']
                                s['VALIDADA'] = True
                                res = "Validada con éxito"
                                break
                            res = "Taxi ocupado"
                    break
                res = "Ya ha sido validada"
    solicitudes.close()
    taxis.close()
    tempfile = os.path.join(os.path.dirname('back/solicitudes.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as solicitudes:
        json.dump(data, solicitudes, indent=4)
    os.remove('back/solicitudes.json')
    os.rename(tempfile, 'back/solicitudes.json')
    solicitudes.close()
    tempfile = os.path.join(os.path.dirname('back/taxis.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as taxis:
        json.dump(data2, taxis, indent=4)
    os.remove('back/taxis.json')
    os.rename(tempfile, 'back/taxis.json')
    taxis.close()
    return { "message": res }
    


@app.post("/confirmar", tags=["solicitudes"])
async def confirmar(solicitud: dict) -> dict:
    id = solicitud['ID']
    with open('back/solicitudes.json', encoding='UTF-8') as solicitudes:
        data = json.load(solicitudes)
        for s in data:
            if s['ID'] == id:
                s['CONFIRMADA'] = True
                break
    solicitudes.close()
    tempfile = os.path.join(os.path.dirname('back/solicitudes.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as solicitudes:
        json.dump(data, solicitudes, indent=4)
    os.remove('back/solicitudes.json')
    os.rename(tempfile, 'back/solicitudes.json')
    solicitudes.close()
    return { "message": "Solicitud confirmada correctamente" }



@app.post("/cancelar", tags=["solicitudes"])
async def cancelar(solicitud: dict) -> dict:
    id = solicitud['ID']
    with open('back/solicitudes.json', encoding='UTF-8') as solicitudes:
        data = json.load(solicitudes)
        with open('back/taxis.json', encoding='UTF-8') as taxis:
            data2 = json.load(taxis)
        for s in data:
            if s['ID'] == id:
                for t in data2:
                    if t['ID'] == s['ID_TAXI']:
                        t['ESTADO'] = "Libre"
                        s['VALIDADA'] = False
                        break
    solicitudes.close()
    taxis.close()
    tempfile = os.path.join(os.path.dirname('back/solicitudes.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as solicitudes:
        json.dump(data, solicitudes, indent=4)
    os.remove('back/solicitudes.json')
    os.rename(tempfile, 'back/solicitudes.json')
    solicitudes.close()
    tempfile = os.path.join(os.path.dirname('back/taxis.json'), str(uuid.uuid4()))
    with open(tempfile, 'w') as taxis:
        json.dump(data2, taxis, indent=4)
    os.remove('back/taxis.json')
    os.rename(tempfile, 'back/taxis.json')
    taxis.close()
