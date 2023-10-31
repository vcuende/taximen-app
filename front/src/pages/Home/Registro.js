import React, { useState } from "react";
import "../../assets/css/cssHome/Registro.css";



function Registro() {
  const [datos, setDatos] = useState({
    nombre: "",
    correoReg: "",
    tlf: "",
    tarjeta: "",
    password: ""
  });

  const handleChangeReg = (event) => {
    setDatos({
      ...datos,
      [event.target.name]: event.target.value,
      [event.target.name]: event.target.value,
      [event.target.name]: event.target.value,
      [event.target.name]: event.target.value,
      [event.target.name]: event.target.value
    });
  };

  const enviarDatos = async () => {
    const newUser = {
      "ID": 0,
      "NOMBRE": datos.nombre,
      "CORREO": datos.correoReg,
      "TELEFONO": datos.tlf,
      "TARJETA": datos.tarjeta,
      "PASSWORD": datos.password,
      "ACTIVO": false
    }

    const response = await fetch("http://localhost:8000/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newUser)
    })

    const resultado = await response.json()
    alert(resultado['message'])
  }

  return (
    <div>
      <h1>¿No tienes una cuenta aún?
        ¡Regístrate aqui!</h1>
      <div className="campos">
        <form className="formulario">
          <label className="nombre" >
            <input type="text" onChange={handleChangeReg} name="nombre" placeholder="Nombre" />
          </label>
          <label className="correo">
            <input type="email" onChange={handleChangeReg} name="correoReg" placeholder="Correo Electrónico" />
          </label>
          <label className="tlf">
            <input type="tel" onChange={handleChangeReg} name="tlf" placeholder="Nº de Teléfono" />
          </label>
          <label className="tarjeta">
            <input type="text" onChange={handleChangeReg} name="tarjeta" placeholder="Nº de Tarjeta de Crédito" />
          </label>
          <label className="password">
            <input type="password" onChange={handleChangeReg} name="password" placeholder="Contraseña" />
          </label>
        </form>
        <button className="regBtn" onClick={enviarDatos}>Regístrame  <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.5 1C4.22386 1 4 1.22386 4 1.5C4 1.77614 4.22386 2 4.5 2H12V13H4.5C4.22386 13 4 13.2239 4 13.5C4 13.7761 4.22386 14 4.5 14H12C12.5523 14 13 13.5523 13 13V2C13 1.44772 12.5523 1 12 1H4.5ZM6.60355 4.89645C6.40829 4.70118 6.09171 4.70118 5.89645 4.89645C5.70118 5.09171 5.70118 5.40829 5.89645 5.60355L7.29289 7H0.5C0.223858 7 0 7.22386 0 7.5C0 7.77614 0.223858 8 0.5 8H7.29289L5.89645 9.39645C5.70118 9.59171 5.70118 9.90829 5.89645 10.1036C6.09171 10.2988 6.40829 10.2988 6.60355 10.1036L8.85355 7.85355C9.04882 7.65829 9.04882 7.34171 8.85355 7.14645L6.60355 4.89645Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg></button>
      </div>
    </div>
  );
}

export default Registro;
