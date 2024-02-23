## Interaction
*User*: LEDs are turned on when input_pin value is greater than 0  
*Result*:
- KB += LED
- KB: LED.fields += input_pin(holds numeric value)
- KB: LED.fields += lit(holds boolean value)
- KB: LED.link += when self.fields[input_pin] > 0: self.fields[lit] = True

::: Agent can now say whether any LED is lit or not, given its input_pin value