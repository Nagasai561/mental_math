# TUI-based Mental Math Trainer

A terminal-based mental math practice tool that generates random arithmetic problems, speaks them out loud using text-to-speech, and accepts typed answers.

## Dependencies
- Python 3.10+
- espeak-ng 
- libespeak1

On Debian/Ubuntu, we can install the latter two via:

```bash
sudo apt install espeak-ng libespeak1
```

Create a python's virtual environment and install required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

## Configuration

Configuration is done via the `config.yaml` file. You can control how often different types of problems appear by adjusting the probabilities in this file.

