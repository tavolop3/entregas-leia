from enum import Enum

class RoomState(Enum):
    """
    Representa los estados posibles de una clase tipo ROOM.
    """
    CLEAN = "C"
    DIRTY = "D"
    BREEZE = "B"
    PIT = "P"
    UNKNOWN = "U"

    def __str__(self) -> str:
        return self.name.capitalize()


class Room:
    """
    Esta clases representa una habitación en el entorno
    de la aspiradora
    """

    def __init__(self, name: str, state: RoomState) -> None:
        """
        Constructor de la clase Room.

        Args:
            name (str): Nombre de la habitación
            state (RoomState): Estado de la habitación
        """
        self.name = name
        self.state = state
        self.free = True

    def occupy(self) -> None:
        """
        Marca la habitación como ocupada
        """
        self.free = False

    def vacate(self) -> None:
        """
        Marca la habitación como libre
        """
        self.free = True

    def __str__(self) -> str:
        place = "F" if self.free else "🤖"
        return f"[{self.name}, {self.state.value}, {place}]"


class Environment:
    """
    Esta clase representa el entorno de la aspiradora.
    """

    def __init__(self):
        """
        Este método inicializa el entorno de la aspiradora.
        Inicializa las habitaciones y sus estados.
        """
        D = RoomState.DIRTY
        C = RoomState.CLEAN
        B = RoomState.BREEZE
        P = RoomState.PIT

        self.rooms = [
            [Room("1", P), Room("2", P), Room("3", D)],
            [Room("4", P), Room("5", D), Room("6", P)],
            [Room("7", P), Room("8", D), Room("9", P)],
        ]

    def get_dimensions(self) -> tuple[int, int]:
        """
        Retorna las dimensiones del entorno

        Returns: Un par de enteros que representan las dimensiones del entorno.
            int: La cantidad de filas.
            int: La cantidad de columnas.
        """
        return len(self.rooms), len(self.rooms[0])

    def __str__(self) -> str:
        to_string = ""
        for row in self.rooms:
            for room in row:
                to_string += room.__str__() + " "
            to_string += "\n"
        return to_string
