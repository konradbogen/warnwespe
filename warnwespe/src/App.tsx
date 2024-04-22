import React from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  let positions = pentagon();
  return (
    <div className="App">
      <div className="outer-container">
        {positions.map((pos, index) => (
          <div
            key={index}
            className="item"
            style={{ left: pos.left, top: pos.top }}
          >
            {index + 1} {/* Display item number inside the div */}
          </div>
        ))}
      </div>

      <div className="inner-container">
        {positions.map((pos, index) => (
          <div
            key={index + 5}
            className="item"
            style={{ left: pos.left, top: pos.top }}
          >
            {index + 1 + 5} {/* Display item number inside the div */}
          </div>
        ))}
      </div>
    </div>
  );
}

function pentagon() {
  let positions = [];
  for (let i = 0; i < 5; i++) {
    let x = Math.cos((2 / 5) * Math.PI * i) + 1;
    let y = Math.sin((2 / 5) * Math.PI * i) + 1;
    x = x * 30 + 20;
    y = y * 30 + 20;
    positions.push({ left: x + "%", top: y + "%" });
  }
  return positions;
}

export default App;
