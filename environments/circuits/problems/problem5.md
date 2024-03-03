---
id: 5
ideas: 
---
# Undefined "the LED" reference

## Description

A user asks an agent "is the LED on?".  
The agent does not have anything in it's world model, meaning that it doesn't know any LED components.  
Because of this the agent will fail to understand the meaning of "the LED".  

The agent has two options:
- use the API in order to list all items and find the LED user is talking about  
- ask the user for the LED id  
