# Turn on the LED

## Real World
LED connected to a button.

## World Model
Full representation of RW already is in agent's mind.
```js
LED {
  id="led-1",
  lit=False,
  input_pin=0,
}

Button {
  id="btn-1",
  pressed=False
  output_pin=0,
}

WireConnection {
  pin_start=InstanceFieldReference("btn-1", "output_pin"),
  pin_end=InstanceFieldReference("led-1", "input_pin"),
}
```

## Interaction
*User*: Turn on the LED  
*Agent*: act.interact_with(Button,"press")

::: LED turns on because the agent pressed the button.



::: Some notes here:

::: - "press" is a concept associated with provoking the event "press" to a button
::: - Besides several things, Agent knows that wire conections have the property of transmitting pin values