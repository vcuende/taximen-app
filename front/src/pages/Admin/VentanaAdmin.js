import "../../assets/css/cssAdmin/VentanaAdmin.css";
import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

function VentanaAdmin() {
    const aparecePopUp = (event) =>{
        document.getElementById("popUpAdmin").style.animationName = "aparecer"
        var estado = ""
        document.getElementById("popUpAdmin").style.display = "flow"
        for (var x of taxis){
            if (x.ID == event.target.id){
                estado = x.ESTADO
            }
        }
        document.getElementById("popUpAdmin").innerHTML = "ESTADO DE TAXI "+event.target.id +": </br>" +estado
    
       
    }
    const desaparecePopUp = () =>{
        document.getElementById("popUpAdmin").style.display =  "none"
    }

    const manager = useHistory();
    if(window.usuarioLogueado == "Ninguno"){
        manager.push("/")
    }

    const handleClick = (event) => {
        const idBoton = event.target.id
        var cositas = []
        for (var x of taxis){
            if (x.ID == idBoton){
                document.getElementById("datitos").innerHTML = 
                "<p className='titulo'>ID: </p>" + String(x.ID) +"<br /><p className='titulo'>UBICACION:  </p>" + String(x.UBICACION) +"<br /><p className='titulo'>DESTINO:  </p>" + String(x.DESTINO) + "<br /><p className='titulo'>ESTADO:  </p>" + String(x.ESTADO) 
            }
        }
    };

    const [taxis, setTaxis] = useState([])
    const fetchTaxis = async () => {
        const response = await fetch("http://localhost:8000/taxis")
        const taxis = await response.json()
        setTaxis(taxis.data)
    }

    useEffect(() => {
        fetchTaxis()
    }, [])
    var listaTaxis = []
    for (var x of taxis) {
        listaTaxis.push(<button id={x.ID} className="TaxiLabelAdmin" onClick={handleClick} onMouseEnter={aparecePopUp} onMouseLeave={desaparecePopUp}> TAXI {x.ID} <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M7.49991 0.876892C3.84222 0.876892 0.877075 3.84204 0.877075 7.49972C0.877075 11.1574 3.84222 14.1226 7.49991 14.1226C11.1576 14.1226 14.1227 11.1574 14.1227 7.49972C14.1227 3.84204 11.1576 0.876892 7.49991 0.876892ZM1.82707 7.49972C1.82707 4.36671 4.36689 1.82689 7.49991 1.82689C10.6329 1.82689 13.1727 4.36671 13.1727 7.49972C13.1727 10.6327 10.6329 13.1726 7.49991 13.1726C4.36689 13.1726 1.82707 10.6327 1.82707 7.49972ZM8.24992 4.49999C8.24992 4.9142 7.91413 5.24999 7.49992 5.24999C7.08571 5.24999 6.74992 4.9142 6.74992 4.49999C6.74992 4.08577 7.08571 3.74999 7.49992 3.74999C7.91413 3.74999 8.24992 4.08577 8.24992 4.49999ZM6.00003 5.99999H6.50003H7.50003C7.77618 5.99999 8.00003 6.22384 8.00003 6.49999V9.99999H8.50003H9.00003V11H8.50003H7.50003H6.50003H6.00003V9.99999H6.50003H7.00003V6.99999H6.50003H6.00003V5.99999Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg></button>)
    }

    return (
        <div className="total">
            <div className="ventanaAdmin">
                <ul className="ListaTaxisAdmin">
                    {listaTaxis}
                </ul>
            </div>
            <div  id = "datitos" className="Ventana">
                <p >Seleccione un taxi para ver sus datos</p>
            </div>
        </div>
    );
}

export default VentanaAdmin;
