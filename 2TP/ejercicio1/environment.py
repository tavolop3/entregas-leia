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
            # [Room("01", P), Room("02", B), Room("03", B), Room("04", D)],
            # [Room("05", B), Room("06", B), Room("07", P), Room("08", B)],
            # [Room("09", C), Room("10", B), Room("11", C), Room("12", D)],
            # [Room("13", C), Room("14", C), Room("15", D), Room("16", D)]
            [Room("01", P), Room("02", P), Room("03", P)],
            [Room("04", P), Room("05", D), Room("06", P)],
            [Room("07", P), Room("08", D), Room("09", P)],
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
