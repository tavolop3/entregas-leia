from agent import Agent
from environment import Environment

if __name__ == "__main__":
    env = Environment()
    print("Entorno inicial:")
    print(env)
    x, y = env.get_dimensions()
    agent = Agent(env, x-1, y-1)
    print("Modelo interno inicial del agente:")
    print(agent.str_model())
    agent.action(20)
