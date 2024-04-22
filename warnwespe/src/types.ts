export type PlaceID = number;

export type PlaceInterface = {
  readonly id: PlaceID;
  words: Word;
  full: boolean;
  directions: Direction[];
};

interface PlayerInterface {
  id: number;
  name: string;
  active: boolean;
  word: Word | null;
  selectedMove: PlaceInterface | null;
  possibleMoves: PlaceInterface[];
  place: PlaceInterface;
}

interface Word {
  readonly id: WordID;
  content: PossibleWord;
  player: PlayerInterface | null;
  place: PlaceInterface | null;
  siblings: Word[];
}

interface GameInterface {
  places: PlaceInterface[];
  players: PlayerInterface[];
  playerIndex: number;
}

interface Riddle {
  words: Word[];
  solved: boolean;
  place: PlaceInterface;
}

export type Direction = [to: PlaceID, type: PossibleDirection];

export const PossibleDirections = ["Way", "River"] as const;
export type PossibleDirection = (typeof PossibleDirections)[number];

export const PossibleWords = [
  "Wald",
  "Warn",
  "Warm",
  "Wespen",
  "Westen",
  "Lilien",
  "Bienen",
  "Linien",
  "Licht",
  "Stich",
  "Nest",
  "Test",
  "Hummel",
  "Bummel",
  "Schummel",
  "Flug",
  "Zug",
] as const;

export type PossibleWord = (typeof PossibleWords)[number];

export const PossibleWordIDs = [
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
] as const;
export type WordID = (typeof PossibleWordIDs)[number];

export type { PlayerInterface, Word, GameInterface, Riddle };
