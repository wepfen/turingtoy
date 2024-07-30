The aim is to implement turing machine engine from https://turingmachine.io/


# Setup

## Start a venv

`python -m venv venv`
`source .devenv/bash_init.sh`

## Install requirements.txt

`python -m pip install -r requirements.txt`

## Install poetry packages

`poetry install`

## Install nox (only for testing)

`yay -S python-nox`

or

`apt install nox`

Test with `nox -s tests`, if it crash, install python3.9 as alt install. 

```python
def run_turing_machine(
    machine: Dict,
    input_: str,
    steps: Optional[int] = None,
) -> Tuple[str, List, bool]
```


