# Turn on the LED

## Real World
LED connected to a button.

## World Model
Full representation of RW already is in agent's mind.
```js
LED {
  id="led-1",
  input_pin=0,
}

Button {
  id="btn-1",
  output_pin=0,
}

WireConnection {
  pin_start=InstanceFieldReference("btn-1", "output_pin"),
  pin_end=InstanceFieldReference("led-1", "input_pin"),
}
```

## Interaction
*User*: Turn on the LED  
*Result*: LED turns on because the agent pressed the button.