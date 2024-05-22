/* eslint-disable @typescript-eslint/indent */
import React, {
  createContext,
  useContext,
  useMemo,
  PropsWithChildren,
  useEffect,
} from "react";

import { PlaceInterface, PlayerInterface } from "../types";
import useGamelogic, { GameAction, GameState } from "./useGameLogic";

type GameProps = {
  initPlaces: PlaceInterface[];
  initPlayers: PlayerInterface[];
  gameStarted: boolean;
};

interface TurnInterface {
  players: PlayerInterface[];
  playerIndex: number;
  activePlayer: PlayerInterface;
  selectedMove?: number;
}

export type { TurnInterface };

export type GameContext = {
  state: GameState;
  triggerLogic: React.Dispatch<GameAction>;
};

const gameContext = createContext<GameContext | null>(null);
export const useGame = () => {
  const context = useContext(gameContext);
  if (!context) throw new Error("must be used in GameContext");
  return context;
};

function Game({
  initPlaces,
  initPlayers,
  gameStarted,
  children,
}: PropsWithChildren<GameProps>) {
  const { state, triggerLogic } = useGamelogic({
    initPlayers,
    initPlaces,
  });

  useEffect(() => {
    if (gameStarted === true) console.log("GAME STARTED");
  }, [gameStarted]);

  const gameContextValues = {
    state,
    triggerLogic,
  };

  const gameContextMemo = useMemo(
    () =>
      ({
        ...gameContextValues,
      } as GameContext),
    [gameContextValues]
  );

  return (
    <gameContext.Provider value={gameContextMemo}>
      {children}
    </gameContext.Provider>
  );
}

export default Game;
