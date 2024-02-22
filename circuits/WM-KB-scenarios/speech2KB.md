# Button is an object

## Interactions
*User*: Button is an object  
*Result*:
- KB += Button -> Object

*User*: LEDs are turned on when input_pin value is greater than 0  
- KB += LEDs
- KB: LEDs.fields += input_pin(holds numeric value)
- KB: LEDs.fields += ON/OFF
- KB: LEDs.link += self.input_pin > 0 then LEDs.fields = ON

::: Agent can now say whether any LED is ON or not, given its input_pin value

    LED is an electronic component
- KB += LED -> electronic_component

*User*: Buttons output_pin value is equal to 1 when it's pressed  
*Result*: Agent can now understand that while pressing a button it's output pin will be equal to 1
