# You'll have to plan this one

## Real World
![Image](../IMGS/7.png)

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
*User*: turn the LED on  
*Agent*:  
&nbsp;&nbsp;&nbsp;&nbsp;plan loop:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act.interact_with(timed_button,"press") and then...  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;act.interact_with(button,"press")

::: In here the agent needs some temporal and sequential planning