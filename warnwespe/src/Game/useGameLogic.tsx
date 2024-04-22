import { useEffect, useReducer } from "react";
import { PlayerInterface, PlaceInterface, Word } from "../types";

type CuedAction = { type: "LISTEN" };

export type GameAction =
  | { type: "ON_PLACE_UPDATE"; place: PlaceInterface }
  | { type: "ON_TURN_END" }
  | { type: "ON_PICKUP"; pickedWord: Word }
  | { type: "ON_DROP"; droppedWord: Word }
  | {
      type: "ON_MOVE_SELECT";
      moveSelection: PlaceInterface | null;
    }
  | {
      type: "ON_INTERACT_END";
    };

export type GameState = {
  players: PlayerInterface[];
  places: PlaceInterface[];
  playerIndex: number;
  activePlayer: PlayerInterface;
  cued: CuedAction | null;
};

type GameProps = {
  initPlaces: PlaceInterface[];
  initPlayers: PlayerInterface[];
};

function updatePlayer(
  indexPlayerToUpdate: number,
  updatetValues: Partial<PlayerInterface>,
  oldState: GameState
): GameState {
  const { players: oldPlayers } = oldState;
  const newPlayers = oldPlayers.map((player) => {
    if (player.id === indexPlayerToUpdate) {
      return {
        ...player,
        ...updatetValues,
      };
    }
    return player;
  });
  return {
    ...oldState,
    players: newPlayers,
    activePlayer: newPlayers[oldState.playerIndex],
  };
}

function movePlayerBySelection(
  idPlayerToMove: number,
  state: GameState
): GameState {
  const { players: oldPlayers, places: oldPlaces } = state;
  const playerToMove = oldPlayers.find(
    (player) => player.id === idPlayerToMove
  );
  if (playerToMove === undefined) {
    throw new Error("Couldnt Find Player From Index");
  }
  const { selectedMove } = playerToMove;
  const newPlace = selectedMove;
  if (newPlace !== null) {
    const newState = updatePlayer(
      idPlayerToMove,
      { place: newPlace, selectedMove: null },
      state
    );
    return newState;
  }
  return state;
}

function onTurnEnd(state: GameState): GameState {
  const { players: oldPlayers, playerIndex: oldIndex } = state;
  const newState = movePlayerBySelection(oldIndex, state);
  const newIndex = (oldIndex + 1) % oldPlayers.length;
  return {
    ...newState,
    playerIndex: newIndex,
  };
}

const playerReducer = (state: GameState, action: GameAction): GameState => {
  const { activePlayer } = state;
  switch (action.type) {
    case "ON_TURN_END": {
      return onTurnEnd(state);
    }
    case "ON_MOVE_SELECT": {
      const stateWithMoveSelected = updatePlayer(
        activePlayer.id,
        { selectedMove: action.moveSelection },
        state
      );
      return movePlayerBySelection(activePlayer.id, stateWithMoveSelected);
    }
    default:
      return state;
  }
  return state;
};

function useGameLogic(initializer: GameProps) {
  const { initPlaces, initPlayers } = initializer;
  const [state, triggerLogic] = useReducer(playerReducer, {
    players: initPlayers,
    places: initPlaces,
    playerIndex: 0,
    activePlayer: initPlayers[0],
  } as GameState);
  return { state, triggerLogic };
}

export default useGameLogic;
