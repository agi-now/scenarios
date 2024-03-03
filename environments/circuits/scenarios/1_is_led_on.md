---
problems: 1
---

# Is the LED on?

## Real World

```python
led = end.create("LED")
button = env.create("Button")
env.connect(
    button.output_pin,
    led.input_pin,
)
# button is being held
env.interact(button.id, "PressDown")
```

## Agent's World View

No information about the real world

## Agent Knowledg

- API-related knowledge

## API Limitations

Disabled & Forgotten:  
- env.create
- env.connect
- env.disconnect
- env.interact

## Interaction
*User*: Is the led on?  
*Agent*: \< Some positive answer \>
