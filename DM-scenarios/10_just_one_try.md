# Plan beforehand

## Real World
![Image](../IMGS/8.png)

## World Model
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
*User*: Turn the LED on, you can only do 2 actions  
*Agent*: plans everything before acting  

::: In here we discourage the agent from experimenting and accomplishing the goal thanks to probability, it has to reason all actions before carrying them out