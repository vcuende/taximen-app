import "../../assets/css/cssTaxi/Taxi.css";
import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

function Taxi() {
  const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));
  var id = -1;
  const manager = useHistory();
  if (window.taxiLogueado == -1) {
    manager.push("/");
  }
  id = window.taxiLogueado;
  const [solicitudes, setSolicitudes] = useState([]);
  const fetchSolicitudes = async () => {
    const response = await fetch("http://localhost:8000/solicitudes");
    const solicitudes = await response.json();
    setSolicitudes(solicitudes.data);
  };

  const comprobar = () => {
    fetchSolicitudes();
    for (var x of solicitudes) {
      if (x.ID_TAXI == id) {
        if (x.VALIDADA == true) {
          window.solicitudTaxi = x;
          document.getElementById("TextoPopUpTaxi").innerHTML =
            "El trayecto asignado es:</br>" +
            "Cliente: " +
            x.NOMBRE +
            "</br>" +
            "Origen: " +
            x.ORIGEN +
            ", &emsp; Destino: " +
            x.DESTINO +
            "</br>" +
            "Fecha: " +
            x.FECHA +
            ", &emsp; Hora: " +
            x.HORA;
          document.getElementById("btnRefTaxi").style.display = "none";
          document.getElementById("PopUpTaxi").style.display = "block";
          document.getElementById("textoTaxi").innerHTML =
            "Viaje asignado, confirme para iniciar.";
        }
      }
    }
  };
  const confirmar = async () => {
    fetchSolicitudes();
    var validada = false;
    for (var x of solicitudes) {
      if (x.ID_TAXI == id) {
        if (x.VALIDADA == true) {
          validada = true;
          window.solicitudTaxi.CONFIRMADA = true;
          const response = await fetch("http://localhost:8000/confirmar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(window.solicitudTaxi),
          });
          const resultado = await response.json();
          alert(resultado["message"]);
          if (resultado["message"] == "Solicitud confirmada correctamente") {
            document.getElementById("PopUpTaxi").style.display = "none";
            document.getElementById("textoTaxi").innerHTML =
              "Conduzca con precaución. <br/>¡Buen viaje!";
          }
        }
      }
    }
    if (!validada) {
      alert("La solicitud ya no se encuentra disponible.");
    }
  };

  return (
    <div>
      <p id="textoTaxi" className="textoTaxi">
        Bienvenido taxi, espera a que se te asigne un cliente.
      </p>
      <button className="solBtn" id="btnRefTaxi" onClick={comprobar}>
        Refrescar
      </button>
      <div id="PopUpTaxi" className="PopUpTaxi">
        <div id="TextoPopUpTaxi"></div>
        <button id="taxiConfirma" className="solBtn" onClick={confirmar}>
          Confirmar
        </button>
      </div>
    </div>
  );
}

export default Taxi;
