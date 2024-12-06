from agent import Agent
from environment import Environment

if __name__ == "__main__":
    env = Environment()
    print(env)
    agent = Agent(env, 2, 0)
    print(agent.str_model())
    agent.action(20)
