# Signup automation using Selenium

> By: Suyash Nepal

<video src="https://github.com/suynep/vrittechQAtask/" controls width="640" height="360">
</video>

## General Info on the scripts
> The scripts RELY on Firefox being installed, and no fallback for Chrome or other browsers have been added at present! ENSURE FIREFOX IS INSTALLED BEFORE RUNNING!

- Core Browser interaction logic lies in `interactor.py`
- For the OTP retrieval/post, the logic lies in `emailmodule.py`
- Fully based on the `selenium` library for browser automation; `mailslurp-client` library for email related operations
> **WARNING**: I've exposed my `API` key *(which is a dummy, but nevertheless...)* intentionally so as to make it easier for the assessors to test the script(s) locally.


## Running the scripts locally

I've added instructions for Linux/MacOS machines primarily 

### Using `uv` (Recommended)

`uv` is a blazing-fast python package manager written in Rust. Using `uv` should be the norm! *(i love `uv`)*

#### Linux/macOS

##### `uv` installation

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh     # install uv
```
> You may need to restart your shell for `uv` to start working properly

##### Local setup

```bash
git clone https://github.com/suynep/vrittechQAtask.git
cd vrittechQAtask/
uv sync
uv run interactor.py
```

#### Windows

#### `uv` installation

In PowerShell, run:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Now, clone and run `interactor.py` after running `uv sync` in the cloned local repo.


### Using `pip`


#### Linux/macOS

##### Local setup + running

```bash
git clone https://github.com/suynep/vrittechQAtask.git
cd vrittechQAtask/
python3 -m virtualenv .venv    # BEFORE RUNNING: ensure that virtualenv package is installed
source ./.venv/bin/activate
pip3 install -r requirements.txt     # or pip instead of pip3, whatever it's called
python3 interactor.py
```
