import React from "react";
import "./assets/css/App.css";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Home from "./pages/Home/Home";
import Admin from "./pages/Admin/Admin";
import User from "./pages/User/User";
import Activate from "./pages/Activate/Activate";
import Taxi from "./pages/Taxi/Taxi";
import icono from "./assets/img/icono.png";

function App() {
  return (
    <div>
      <header>TAXIMEN <img alt= "icono" height="70px" src={icono}></img></header>
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/admin" component={Admin} />
          <Route exact path="/user" component={User} />
          <Route exact path="/activate" component={Activate} />
          <Route exact path="/taxi" component={Taxi} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
