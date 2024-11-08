import argparse
from .agent import Agent


def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("goal", type=str, help="The goal of the agent")
    parser.add_argument("--model", type=str, required=False, help="The model to use for the agent",
                        default='dolphin-llama3')
    args = parser.parse_args()
    # create agent
    agent = Agent(model=args.model, goal=args.goal)
    # run agent
    solved = False
    while not solved:
        solved = agent.tick()

if __name__ == "__main__":
    main()
