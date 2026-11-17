# CS 1110 labs

This repository collects Python lab exercises and small practice programs from CS 1110. The folders are organized by lab number; the code is coursework and practice material, not a packaged application.

## Contents

- `lab1/`, `lab3/`, `lab4/`, `lab5/`: introductory programs and string or dice exercises.
- `lab6/`: string functions and debugging practice; some functions are intentionally faulty exercise material.
- `lab7/`, `lab9/`, `lab11/`, `lab12/`, `lab13/`: functions involving strings, time objects, debugging, lists, and iteration.
- `BackendOA/`: a small pretest script.

Some folders include course-provided test or exercise files. The assignment handouts and course instructions define the expected behavior; this repository does not include all assignment specifications.

The Python exercise index below is regenerated from the source files when a lab file changes on `main`. Descriptions come from module docstrings; files without docstrings are labeled as exercises or supporting scripts. The workflow preserves this README's manually written sections.

<!-- BEGIN AUTO-GENERATED LAB INDEX -->
### Python exercise index

#### `lab1/`

- [`hello1.py`](lab1/hello1.py) — Python exercise or supporting script.
- [`hello2.py`](lab1/hello2.py) — A window displaying Hello World.

#### `lab11/`

- [`lab11.py`](lab11/lab11.py) — A module to demonstrate errors and error debugging.

#### `lab12/`

- [`lab12.py`](lab12/lab12.py) — Python exercise or supporting script.

#### `lab13/`

- [`clamp.py`](lab13/clamp.py) — Python exercise or supporting script.
- [`devowel.py`](lab13/devowel.py) — Python exercise or supporting script.
- [`lesser_than.py`](lab13/lesser_than.py) — Python exercise or supporting script.
- [`removeall.py`](lab13/removeall.py) — Python exercise or supporting script.
- [`uniques.py`](lab13/uniques.py) — Python exercise or supporting script.

#### `lab15/`

- [`lab15.py`](lab15/lab15.py) — A module with several recursive functions using divide-and-conquer
- [`test15.py`](lab15/test15.py) — Course-provided test or exercise checks.

#### `lab16/`

- [`lab16.py`](lab16/lab16.py) — A module with several recursive functions
- [`person.py`](lab16/person.py) — A class to rerpresent a genealogical tree
- [`test16.py`](lab16/test16.py) — Course-provided test or exercise checks.

#### `lab17/`

- [`lab17.py`](lab17/lab17.py) — The functions for Lab 17.
- [`test17.py`](lab17/test17.py) — Course-provided test or exercise checks.

#### `lab18/`

- [`bjack.py`](lab18/bjack.py) — A module for a very simple approximation of the game Blackjack
- [`card.py`](lab18/card.py) — A module providing a class for playing cards
- [`test.py`](lab18/test.py) — Course-provided test or exercise checks.

#### `lab19/`

- [`leng.py`](lab19/leng.py) — The class definition for the class lab
- [`test.py`](lab19/test.py) — Course-provided test or exercise checks.

#### `lab20/`

- [`card.py`](lab20/card.py) — A module providing a class for playing cards
- [`classroom.py`](lab20/classroom.py) — Python exercise or supporting script.
- [`test.py`](lab20/test.py) — Course-provided test or exercise checks.
- [`wild.py`](lab20/wild.py) — A module providing a class for playing cards with Jokers

#### `lab21/`

- [`card.py`](lab21/card.py) — A module providing a class for playing cards
- [`test.py`](lab21/test.py) — Course-provided test or exercise checks.
- [`wild.py`](lab21/wild.py) — A module providing a class for playing cards with Jokers

#### `lab23/`

- [`app.py`](lab23/app.py) — A simple application displaying a text and an image.
- [`flip1.py`](lab23/flip1.py) — A module the plays a coin flip contest.
- [`flip2.py`](lab23/flip2.py) — A module the plays a coin flip contest.
- [`__init__.py`](lab23/game2d/__init__.py) — A module to support simple 2D game development.
- [`app.py`](lab23/game2d/app.py) — The primary class for 2D game support.
- [`gobject.py`](lab23/game2d/gobject.py) — The base classes for 2D game support.
- [`gpath.py`](lab23/game2d/gpath.py) — Auxiliary drawables for 2D game support.
- [`grectangle.py`](lab23/game2d/grectangle.py) — The most important drawables for 2D game support.
- [`gsprite.py`](lab23/game2d/gsprite.py) — A module to support flipbook animation.
- [`gtile.py`](lab23/game2d/gtile.py) — A module to support image tiling.
- [`gview.py`](lab23/game2d/gview.py) — The view and input classes for 2D game support.
- [`sound.py`](lab23/game2d/sound.py) — Sound classes for 2D game support.

#### `lab3/`

- [`dice.py`](lab3/dice.py) — A simple die roller

#### `lab4/`

- [`dice.py`](lab4/dice.py) — A simple die roller
- [`dicefun.py`](lab4/dicefun.py) — Python exercise or supporting script.

#### `lab5/`

- [`quotes.py`](lab5/quotes.py) — The module for first_inside_quotes

#### `lab6/`

- [`europeanize.py`](lab6/europeanize.py) — Python exercise or supporting script.
- [`funcs.py`](lab6/funcs.py) — Functions for handling Strings
- [`quotes.py`](lab6/quotes.py) — The module for first_inside_quotes
- [`test.py`](lab6/test.py) — Course-provided test or exercise checks.
- [`tests.py`](lab6/tests.py) — Course-provided test or exercise checks.

#### `lab7/`

- [`extra.py`](lab7/extra.py) — Additional problem for more practice
- [`lab07.py`](lab7/lab07.py) — Module for implementing Lab 07 functions.
- [`testex.py`](lab7/testex.py) — Course-provided test or exercise checks.

#### `lab9/`

- [`clock.py`](lab9/clock.py) — Module that provides a simple Time class
- [`extras.py`](lab9/extras.py) — Additional problems for more practice
- [`lab09.py`](lab9/lab09.py) — Module for implementing Lab 09 functions.
- [`test09.py`](lab9/test09.py) — Course-provided test or exercise checks.
- [`testex.py`](lab9/testex.py) — Course-provided test or exercise checks.

<!-- END AUTO-GENERATED LAB INDEX -->
## Running a file

Use Python 3 from the repository root. For example:

```sh
python3 lab3/dice.py
python3 lab7/lab07.py
```

Some files only define functions and print nothing when run. Import or call those functions from a Python shell or the relevant course test file. The Kivy example in `lab1/hello2.py` needs Kivy installed; most other exercises use only the Python standard library. There is no shared dependency file or single test command for this collection.

## Notes

Exercises may be incomplete, retain assignment scaffolding, or contain bugs that are part of a debugging task. Review a file and its lab instructions before using it as a reference implementation. Keep course-provided test files with the exercise they belong to.
