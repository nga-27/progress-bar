# progress-bar

A simple-to-use progress bar for python terminal applications, adapted from a post on stack overflow.

[Credit to this post](https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters)

<img alt="magical progress bar" src="./static/progress_bar.jpeg" width=500 />

###### Image created by Bing Image Creator (Dall-E 3)

---

# Installation

Installation is fairly straightforward:

```sh
pip install progress_bar@git+ssh://git@github.com/nga-27/progress-bar@v0.1.0
```

Note, for those using `zsh` terminal, you may need to add quotes around the repo string _after_ `pip install` portion.

To add to a python setup.py file:

```python
REQUIRES = [
    'progress_bar @ git+ssh://git@github.com/nga-27/progress-bar@main'
]
```

---

# Usage

An example code snippet of someone wanting a progress bar named "some name" that upticks every second for 10 seconds would have something like the following:

```python
import time
from progress_bar import ProgressBar

max_num_ticks = 10
timer = ProgressBar(max_num_ticks, name="some name", use_stopwatch=True)

timer.start()
for _ in range(max_num_ticks):
    timer.uptick()
    time.sleep(1)
```
