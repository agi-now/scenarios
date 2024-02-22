# Text to World model and Knowledge base update

## Interactions
*User*: Button is an object  
*Result*:
- KB += Button -> Object

*User*: LED is an electronic component
*Result*:
- KB += LED -> electronic_component

*User*: LEDs are turned on when input_pin value is greater than 0
*Result*:
- KB += LED
- KB: LED.fields += input_pin(holds numeric value)
- KB: LED.fields += lit(holds boolean value)
- KB: LED.link += when self.fields[input_pin] > 0: self.fields[lit] = True

::: Agent can now say whether any LED is lit or not, given its input_pin value

*User*: Buttons output_pin value is equal to 1 when it's pressed  
*Result*:
- KB += Button
- KB: Button.fields += output_pin(holds numeric value)
- KB: Button.fields += pressed(hold boolean value)
- KB: Button.link += when self.fields[pressed] == True: self.fields[output_pin] = 1