import ollama
import subprocess
import os


class Agent:
    def __init__(self, model, goal):
        # get os type
        os_type = os.name
        # get shell type (for windows or posix)
        shell_type = os.getenv("SHELL")
        self.model = model
        self.goal = goal
        self.client = ollama.Client(
            host="http://localhost:11434"
        )
        self.context = [{
            "role": "system",
            "content": f"""You are an AI agent running on {os_type} with a {shell_type} shell. Your goal is to {goal}, you can run commands as you wish, if you feel like you have beat the goal, you can just say \"$DONE$\" in your response, otherwise, your responses should just be valid commands that you would run in the shell. you may only provide 1 command per response, do not comment, you are entering commands in the shell, not in a chat room."""
        }]

    def tick(self):
        response = self.client.chat(model=self.model, messages=self.context)
        # get the command from the response
        command = response["message"]["content"]
        if "$DONE$" in command:
            print("\033[1;37;40m-->", command)
            return True
        else:
            # run the command
            self.context.append({
                "role": "assistant",
                "content": command
            })
            print("\033[1;32;40m-->", command)
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            if result.returncode != 0:
                print("\033[1;31;40m-->", str(result.stderr.decode("utf-8")))
            else:
                print("\033[1;33;40m-->", str(result.stdout.decode("utf-8")))
            self.context.append({
                "role": "user",
                "content": result.stdout.decode("utf-8")
            })
            return False


if __name__ == "__main__":
    agent = Agent(model="dolphin-llama3", goal="look for the raspberry pi named 'rpi5' on the network, try to connect to it using the user 'Kokonico'")
    stop = False
    while not stop:
        stop = agent.tick()