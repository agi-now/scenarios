# Circuits

The environment contains circuit components that can be connected via wires. Components don't have spatial locations. 

## Components

- LED: will be turned on if it's pin has value of 1 or greater  
...

## Interfaces

The environment does not provide any visual information, so the components are not visible to an agent.
The only way to get information about components is to use Python API.

### API Methods

- env.list() -> list[Component]
    Returns a list of components.
    Some elements can be hidden, so they will not be shown using this function.

- env.probe_pin(pin_id: int) -> int
    Returns a pin value of a component given it's id and the pin id.

- env.interact(id: int, interaction: str = None) -> None
    Interacts with a component. If multiple interactions available - you must specify it's interaction id.

- env.create(component_type: str) -> int
    Creates a new component that is disconnected from everything.
    `component_type` is one of "LED", "Button" and others.

- env.connect(pin_start: int, pin_end: int)

### API Entities

- Component
    id: int
    fields: dict[str, any]
    input_pins: list[int]
    output_pins: list[int]
