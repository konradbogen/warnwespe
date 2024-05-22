import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { useGame } from "./Game/Game";
import Game from "./Game/Game";

function App() {
  let positions = pentagon();
  const { triggerLogic } = useGame();

  function handleClick() {
    console.log ("CLICK")
  }

  return (
    <Game
      initPlaces={setup.initPlaces}
      initPlayers={setup.initPlayers}
      gameStarted={gameStarted}
    >
      <div className="App">
        <div className="outer-container">
          {positions.map((pos, index) => (
            <div
              key={index}
              className="item"
              style={{ left: pos.left, top: pos.top }}
              onClick={() => handleClick()}
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
    </Game>
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
