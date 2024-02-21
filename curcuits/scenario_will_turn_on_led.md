# Will pressing button B turn on the LED

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
  label="A",
  output_pin=0,
}

Button {
  id="btn-2",
  label="B',
  output_pin=0,
}

WireConnection {
  pin_start=InstanceFieldReference("btn-1", "output_pin"),
  pin_end=InstanceFieldReference("led-1", "input_pin"),
}
```

## Interaction
*User*: Will pressing button B turn on the LED?  
*Agent*: \<negative answer\>