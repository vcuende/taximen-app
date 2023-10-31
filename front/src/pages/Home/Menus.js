import React from "react";
import Registro from "./Registro";
import Login from "./Login";
import ZonaTaxi from "./ZonaTaxi";
import "../../assets/css/cssHome/menus.css";
function Menus() {
  return (
    <div className="menus">
      <div className="reg">
        <Registro />
      </div>
      <div className="login">
        <Login />
      </div>
      <div className="ZonaTaxi">
        <ZonaTaxi />
      </div>
    </div>
  );
}

export default Menus;
