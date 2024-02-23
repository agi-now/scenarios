## Interaction
*User*: Buttons output_pin value is equal to 1 when it's pressed  
*Result*:
- KB += Button
- KB: Button.fields += output_pin(holds numeric value)
- KB: Button.fields += pressed(hold boolean value)
- KB: Button.link += when self.fields[pressed] == True: self.fields[output_pin] = 1
