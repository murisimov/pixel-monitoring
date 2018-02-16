### Real-time monitoring of pixel color for specific window

##### Works as command line utility.

---

##### Positional arguments are:
- **Window name substring**. Will grab the first match
- **Alert message**. Text-to-speech library will play it when desired color reached
- **RGB deviation** (optional). For instance, if set to `5` with target color `(5, 5, 5)` it will match RGB range from `(0, 0, 0)` to `(10, 10, 10)`

---

##### How to use it:
- Run script (details below), see `press enter when mouse cursor is at the target color` message
- Go to desired window, place the cursor right at the pixel
- Switch back to terminal without moving mouse, press `ENTER`, it will ask you if the color is right (can be checked [here](https://www.w3schools.com/colors/colors_rgb.asp))
- When you're okay with the color, type `y` and press `ENTER`
- Now, when the current color of that pixel will fit into `RGB deviation`, you will hear the `Alert message`.
- Ta-da!

---
##### Prerequisites:
- `Ubuntu 14.04/16.04` (only those two tested)
- `python3.5` +


---
##### Installation
- `sudo apt-get -y install build-essential mpg321 xdg-utils`
- Install right into system (not recommended): `pip install -r requirements.txt`
- Install into virtualenv: `bash install.sh`, **or** `3.5 ~/.envs`, where `3.5` and `~/.envs` are python version and directory for virtualenvs. These are default values, arguments are optional.

---

##### Example usage:

- For plain installation: `python3.5 run.py 'My Social Network Page' 'message received' 5`
- For virtualenv installation:
  - Without entering virtualenv:
    - `/home/$USER/.envs/pixel-monitoring/bin/python3.5 run.py 'My Social Network Page' 'message received' 5`
  - Entering virtualenv:
    - `source /home/$USER/.envs/pixel-monitoring/bin/activate`
    - `python3.5 run.py 'My Social Network Page' 'message received' 5`
    - `deactivate`
