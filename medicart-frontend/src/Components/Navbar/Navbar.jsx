import React, { Component } from "react";
import { Button } from "./Button";
import { MenuItems } from "./MenuItems";

export default class Navbar extends Component {

state = {
    clicked: false
}
handleClick =()=>{
    this.setState({clicked: !this.state.clicked})
}

  render() {
    return (
      <div className="NavbarItems">
        <h1 className="navbar-logo">MEDIC<i className="fas fa-cart-plus"></i>RT   </h1>
        <div className="menu-icon" onClick={this.handleClick}>
    <i className={this.state.clicked ? 'fas fa-times' : 'fas fa-bars'}></i>
        </div>
        <ul className={this.state.clicked ? 'nav-menu active' : 'nav-menu'}>
        <button className="contact">Register</button>
          {MenuItems.map((item, index) => {
              <Button>Sign Up</Button>
              
            return (
                
              <li>
                <a className={item.cName} href={item.url}>
                  {item.title}
                </a>
              </li>
            );
          })}
          
        </ul>
        
      </div>
    );
  }
}
