import json

from typing import (
    Dict,
    List,
    Optional,
    Tuple,
)

import poetry_version

__version__ = poetry_version.extract(source_file=__file__)


def run_turing_machine(
    machine: Dict,
    input_: str,
    steps: Optional[int] = None,        
) -> Tuple[str, List, bool]: #output, execution_history, accpeted

    offset = 10 # nombre de caractère blank que je décide d'afficher
    ruban = machine.get("blank")*offset + input_ + machine.get("blank")*offset

    state = machine.get("start state")
    reading = ruban[offset]
    position = 0
    memory = " "*offset + input_ + " "*offset
    execution_history = []


    while state not in machine["final states"]:

        

            
        history = {
            "state" : state,
            "reading" : reading,
            "position" : position,
            "memory" : memory.strip(),
            "transition" : machine['table'][state][reading]
        }

        execution_history.append(history)

        instructions = machine['table'][state][reading]

        # si le caractère lu est une clé vers un dict
        if isinstance(instructions, dict):

            for instruction in instructions:
            
                if instruction == 'write':
                    ruban = list(ruban)
                    ruban[position+offset] = instructions[instruction]
                    ruban = "".join(ruban)

                    memory = list(memory)
                    memory[position+offset] = instructions[instruction]
                    memory = "".join(memory)
                    
                if instruction == 'L':
                    position-=1
                    state = instructions[instruction]

                if instruction == 'R':
                    position+=1
                    state = instructions[instruction]
                    
            
        # si le caractère lu est une clé vers une str
        if isinstance(instructions, str):
                    
            if instructions == 'L':
                position-=1

            if instructions == 'R':
                position+=1
        reading = ruban[position+offset]

    return memory.strip(), execution_history, True

