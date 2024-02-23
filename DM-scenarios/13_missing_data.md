# What's this?

## Real World
![Image](../IMGS/6.png)

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
*User*: Understand the blank component
*Agent*: Goes on experimental loop to find out behaviour of component

::: Not a very complicated system, just a random logical gate