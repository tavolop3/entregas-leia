from environment import Environment
from agent import Agent

if __name__ == "__main__":
    env = Environment()
    ag = Agent(env)
    ag.start(1000)
    print(ag.get_performance())