import ollama
import subprocess
import os
import re


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
            "content": f"You are an AI agent running on {os_type} with a {shell_type} shell. Your goal is to {goal}, you can run commands as you wish, if you feel like you have beat the goal, you can just say \"$DONE$\" in your response, otherwise, your responses should just be valid commands that you would run in the shell. you may only provide 1 command per response, do not comment or speak, you are entering commands in the shell and receiving feedback from the shell. Good luck!"
        }]

    def tick(self):
        response = self.client.chat(model=self.model, messages=self.context)
        # get the command from the response
        command = response["message"]["content"]
        if "$DONE$" in command:
            print("\033[1;37m-->", command)
            return True
        else:
            # run the command
            self.context.append({
                "role": "assistant",
                "content": command
            })
            print("\033[1;32m-->", command)
            consent = input("Do you want to run this command? (y/n): ")
            if consent.lower() == "n":
                print("\033[1;31m-->", "User denied command execution")
                self.context.append({
                    "role": "user",
                    "content": "System denied command execution"
                })
                return False
            for command in re.split(r'[;\n]', command):
                if "$DONE$" in command:
                    print("\033[1;37m-->", command)
                    return True
                if command.startswith("cd "):
                    directory = command.split(" ")[1].split("\n")[0]
                    try:
                        os.chdir(directory)
                    except FileNotFoundError:
                        pass  # do nothing
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                if result.returncode != 0:
                    print("\033[1;31m-->", end="")
                else:
                    print("\033[1;33m-->", end="")

                output = result.stdout.decode("utf-8") + "\n" + result.stderr.decode("utf-8")
                # remove ansii color codes from output
                output_noansii = re.sub(r"\033\[\d+;\d+m", "", output)

                print(output_noansii)
                self.context.append({
                    "role": "user",
                    "content": output_noansii
                })

            return False