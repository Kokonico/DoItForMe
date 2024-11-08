# DoitForMe
> abuse AI to run commands on your computer for you

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
