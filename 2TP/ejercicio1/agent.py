import time
import random
from environment import Environment
from environment import RoomState
from environment import Room


class Perception:
    """
    Esta clase representa Una percepción del agente.
    """

    def __init__(self, state: RoomState):
        self.state = state

    def is_clean(self) -> bool:
        return self.state == RoomState.CLEAN

    def is_dirty(self) -> bool:
        return self.state == RoomState.DIRTY

    def is_pit(self) -> bool:
        return self.state == RoomState.PIT

    def is_breeze(self) -> bool:
        return self.state == RoomState.BREEZE


class Sensor:
    """
    Esta clase representa modela los sensores del agente.
    """
    def perceive(self, room: Room) -> Perception:
        """
        Este método simula la percepción del agente.

        Args:
            room (Room): la habitación a analizar

        Returns:
            Perception: la percepción del agente

        """
        return Perception(room.state)


class Actuator:
    """
    Esta clase modela los actuadores del agente.
    """

    def all_pit(self, model: list[list[RoomState]], movs, x, y) -> bool:
        """
        Este método verifica a partir del estado interno
        si todas las casillas adyacentes son pozos.
        Args:
            model (list[list[RoomState]]): Estado interno del agente
            x (int): coordenado x del agente.
            y (int): coordenada y del agente.

        Returns:
            bool: True si todas las casillas adyacentes son pozos, False en caso contrario.
        """
        for m in movs.values():
            if model[x + m[0]][y + m[1]] != RoomState.PIT:
                return False
        print("Todas las casillas son pozos")
        return True

    def act(
        self,
        x: int,
        y: int,
        env: Environment,
        perception: Perception,
        model: list[list[RoomState]],
    ) -> tuple[int, int]:
        """
        Este método modela el accionar del agente.

        Args:
            x: coordenada x del agente.
            y: coordenada y del agente.
            env: Ambiente en donde se encuentra el agente.
            perception: Percepción del agente.
            model: Estado interno del agente.

        Returns:
            tuple: Retorna la nueva posición del agente en el ambiente.
                -int: coordenada x del agente.
                -int: coordenada y del agente.
        """

        # Verificar si la habitación está limpia o sucia
        if perception.is_clean():
            print(f"Agente: la habitación [{env.rooms[x][y].name}] está limpia")
        elif perception.is_dirty():
            print(f"Agente: la habitación [{env.rooms[x][y].name}] está sucia... limpiando")
            env.rooms[x][y].state = RoomState.CLEAN

        # Actualizar el estado interno del agente despúes de accionar sobre la habitación y con la nueva percepción
        model[x][y] = perception.state

        # Realizar el movimiento a otra habitación
        max_x, max_y = env.get_dimensions()
        dx, dy, movs = random_direction(x, y, max_x, max_y)

        # Si en el estado interno se verifica que todas las casillas adyacentes son pozos
        # se elige cualquier dirección aleatoria. Caso contrario, se elige una dirección aleatoria que no sea un pozo.
        if self.all_pit(model, movs, x, y):
            dx, dy, movs = random_direction(x, y, max_x, max_y)
        else:
            while model[dx][dy] == RoomState.PIT:
                dx, dy, movs = random_direction(x, y, max_x, max_y)

        env.rooms[dx][dy].occupy()
        env.rooms[x][y].vacate()

        return dx, dy

def random_direction(x, y, dim_x, dim_y) -> tuple[int, int, dict]:
    """
    Este método selecciona una dirección aleatoria para moverse en el ambiente.
    Args:
        x: coordenada x del agente.
        y: coordenada y del agente.
        dim_x: límite de la coordenada x.
        dim_y: límite de la coordenada y.

    Returns:
        tuple: Retorna la nueva posición del agente en el ambiente.
            -int: coordenada x del agente.
            -int: coordenada y del agente.
            -dict: Diccionario con las direcciones posibles.
    """
    # Lista de movimientos posibles
    movs = {
        "left": (0, -1),
        "right": (0, 1),
        "up": (-1, 0),
        "down": (1, 0),
    }

    # Eliminar direcciones que no se pueden tomar debido a las fronteras del mapa
    if x == 0:
        movs.pop("up", None)  # Eliminar 'up' si estamos en la fila superior
    if x == dim_x - 1:
        movs.pop("down", None)  # Eliminar 'down' si estamos en la fila inferior
    if y == 0:
        movs.pop("left", None)  # Eliminar 'left' si estamos en la columna más a la izquierda
    if y == dim_y - 1:
        movs.pop("right", None) # Eliminar 'right' si estamos en la columna más a la derecha

    # Seleccionar una dirección aleatoria
    direction = random.choice(list(movs.keys()))
    dx, dy = movs[direction]

    x += dx
    y += dy

    return x, y, movs


class Agent:

    def __init__(self, env: Environment, x: int, y: int) -> None:
        """
        Constructor de la clase Agent.

        Args:
            env: El entorno de la aspiradora.
            x: posición inicial en x del agente.
            y: posición inicial en y del agente.
        """
        self.env = env
        self.model = self.init_model()
        self.x = x
        self.y = y

    def init_model(self) -> list[list[RoomState]]:
        """
        Inicializa el estado interno del agente.
        Returns:
            list[list[RoomState]]: El estado interno del agente. Es una matriz que representa el entorno.
        """
        rows, cols = self.env.get_dimensions()
        model = [[RoomState.UNKNOWN for _ in range(cols)] for _ in range(rows)]
        return model

    def action(self, steps: int) -> None:
        """
        Este método simula N (steps) pasos del agente en el entorno.
        Args:
            steps: cantidad de pasos a simular.
        """
        for _ in range(steps):
            print(f"====Paso {_}=======")
            sensor = Sensor()
            actuator = Actuator()
            perception = sensor.perceive(self.env.rooms[self.x][self.y])
            self.x, self.y = actuator.act(self.x, self.y, self.env, perception, self.model)
            print(f"Agente: me movi a la habitación [{self.env.rooms[self.x][self.y].name}]")
            print(self.env)
            perception = sensor.perceive(self.env.rooms[self.x][self.y])
            if perception.is_pit():
                print("Agente: Me caí en un pozo... :(")
        print("Fin de la simulación")
        print("Geografía aprendida:")
        print(self.str_model())

    def str_model(self) -> str:
        to_string = ""
        for row in self.model:
            for room in row:
                to_string += f"[{room.value}] "
            to_string += "\n"
        return to_string