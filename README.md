# DoitForMe
> abuse AI to run commands on your computer for you

## WARNING
I do ***NOT*** take responsibility for any damage caused by this software.
This software should ***NOT*** be used in a production environment.
This software is ***NOT*** secure and should ***NOT*** be used on any system that contains sensitive information.
This software is ***NOT*** intended to be used by anyone, and should ***NOT*** be used by anyone.
This software is ***NOT*** intended to be used for any purpose, and should ***NOT*** be used for any purpose.
By using this software, you agree that I am not responsible for the inevitable destruction of your system.

## Installation
```bash
pip3.12 install doitforme
```

## Usage
```bash
difm "print the contents of README.md"
```

## Requirements
- Python 3.13
- Ollama server available, anywhere works
- No self-preservation instincts

## How to set up
1. Install [Ollama](https://ollama.com/download)
2. Run ollama in the background using `ollama serve`
3. Download the AI model you wish to use using `ollama run <model_name>`, you can find the models [here](https://ollama.com/search).
4. Install this package using `pip3.13 install doitforme`
5. Run `difm` followed by the command you want to run
