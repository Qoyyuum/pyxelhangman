# Pyxel Hangman

A retro-style Hangman game built with [Pyxel](https://github.com/kitao/pyxel) and Python.

## Features

- Random quotes as hidden words
- Keyboard input (A-Z)
- Lives and hangman drawing
- Restart with F5, quit with ESC

## Project structure

- `pyproject.toml` — packaging metadata and `pyxelhangman` console script
- `src/pyxelhangman/game.py` — main game logic (rendering, input, game state)
- `src/pyxelhangman/quotes.py` — quote provider
- `src/pyxelhangman/__init__.py` — package entrypoint
- `src/pyxelhangman/main.py` — runway script for pyxel package/play and ambient imports

## Setup

### uv (recommended)
1. Sync package installs
   ```powershell
   uv sync
   ```

or

### pip

2. Create and activate venv
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -U pip
   pip install -e .
   ```

3. Install dependencies manually (optional):
   ```powershell
   pip install -r requirements.txt
   ```

## Run locally

```powershell
uv run pyxel play .\pyxelhangman.pyxapp  # if packaged
# or direct package/play cycle:
uv run pyxel package .\src\pyxelhangman .\src\pyxelhangman\main.py
uv run pyxel play .\pyxelhangman.pyxapp
```
or if not in uv
```
python -m pyxel play .\pyxelhangman.pyxapp
```

## Package command

- Build bundle:
  `uv run pyxel package .\src\pyxelhangman .\src\pyxelhangman\main.py`
- Play bundle:
  `uv run pyxel play .\pyxelhangman.pyxapp`

## Install as command

After `pip install -e .` you can run:

```powershell
pyxelhangman
```
