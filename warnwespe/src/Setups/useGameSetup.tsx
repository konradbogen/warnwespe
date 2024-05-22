import { useEffect, useState } from "react";
import { PlayerInterface, PlaceInterface } from "../types";

const defaultPlayerNames = ["Player 1"];

interface GameSetup {
  initPlaces: PlaceInterface[];
  initPlayers: PlayerInterface[];
  initBands: number[][];
}

const getGameData = async () => {
  let placesData = [1, 2, 3, 4];
  try {
    const placesSetup = placesData.map((index) => ({
      id: null,
      words: null,
      full: null,
      directions: null,
    })) as PlaceInterface[];
    const musiciansSetup = {
      ...musiciansData,
      anonymousMusicians: [
        ...musiciansData.anonymousMusicians.map(({ relationships, rest }) => ({
          ...rest,
          relationships: new Map(relationships),
        })),
      ] as AnonymousMusician[],
    } as MusicianSetup;

    return { musiciansSetup, placesSetup };
  } catch (error) {
    console.log(error);
    throw new Error("Error fetching Data");
  }
};

function playerFactory(
  player_names: string[],
  places: PlaceInterface[],
  musicians: Musician[],
  bands: MusicianID[][]
): PlayerInterface[] {
  const placesWithoutStage = places.filter((p) => p.name !== "stage");

  const availableMusiciansWith = PossibleMusicianIDs.reduce(
    (acc, val) => ({
      ...acc,
      [val]: [
        ...new Set(bands.filter((band) => band.some((m) => m === val)).flat()),
      ],
    }),
    {}
  ) as Record<MusicianID, MusicianID[]>;

  const players: PlayerInterface[] = player_names.map((n, i) => ({
    id: i,
    name: n,
    active: false,
    selectedMove: null,
    place:
      placesWithoutStage[Math.floor(Math.random() * placesWithoutStage.length)],
    bandInformation: {
      globalPossibleBands: bands,
      availableMusicians: [...PossibleMusicianIDs],
      band: [] as Musician[],
      playerPossibleBands: bands,
      availableMusiciansWith,
    },
  }));
  return players;
}

async function getGameSetup() {
  const { musiciansSetup, placesSetup } = await getGameData();
  const { bands } = musiciansSetup;
  const places = placesSetup;
  const identities = getIdentitiesFromAnonymous(musiciansSetup);
  const placesWithMusicians = distributeMusicians(identities, places);
  const players = playerFactory(
    defaultPlayerNames,
    placesWithMusicians,
    identities,
    bands
  );
  return { places: placesWithMusicians, players, bands };
}

function useGameSetup() {
  const [setup, setSetup] = useState<GameSetup | undefined>();
  const [loading, setLoading] = useState(true);
  const [, setRequested] = useState<boolean>(false);

  useEffect(() => {
    setRequested((requested) => {
      if (requested === false) {
        getGameSetup().then(({ places, players, bands }) => {
          setSetup((currSetup) => ({
            ...currSetup,
            initPlaces: places,
            initPlayers: players,
            initBands: bands,
          }));

          setLoading(false);
        });
        return true;
      }
      return true;
    });
  }, []);

  return { loading, setup };
}

export default useGameSetup;
