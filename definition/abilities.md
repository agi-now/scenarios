<!-- 
When adding an ability, check if 
- it makes sense for a human, symbolic agent, and an LLM 
- a regular person would say that they have this ability if asked
- you are adding it in a correct place, make sure the children are extensions/specifications of the parent. Remember that this is not a tree of dependencies/components - don't add children abilities because they are required to do the parent ability. For example `ability to store procedural knowledge` should not be under the `ability to act`, it is indeed required to act, but it's not an expansion of the `ability to act`.
- it does not intersect different parent abilities, like the ability "to communicate" is about perceiving what is being told to you, action of giving a response and mental process of coming up with an answer. Such abilities need to be divided into parts that don't span across multiple parent abilities.

tags:
- `explain` - please provide an example in the PR comment
- `invalid` - the entry is not formulated as an ability
- `remove` - the entry is not needed because it is invalid or unclear,it needs to be deleted or replaced
- `composite` - this ability spans across different parent abilities and needs to be split up
- `example` - not an ability, but it's example. replace with an actual ability when ready

It's a good idea to resolve all the tags before merging a PR.
-->

# Ability List

Ability ...

- 1\. to perceive information  
  - to perceive your own actions
  - to perceive visual information
    - to understand non-verbal cues
    - to perceive textual information
      - to perceive vertical textual information
      - to perceive handwritten textual information
    - to perceive brightness information
    - to perceive color information
    - to perceive texture information
    - to perceive proximity information
    - to perceive shape
    - to perceive movement
    - to identify objects
      - to do visual chunking <!-- [Check reference 1 in the bottom] -->
  - to perceive auditory information
    - to perceive frequency information
    - to perceive volume information
    - to perceive speech
  - to perceive body related information
    - to perceive skin related information
      - to perceive damage information
      - to perceive pressure information
      - to perceive temperature information
      - to perceive texture information
    - to perceive muscles related information
      - to perceive position of muscles
        - to perceive balance and orientation information
      - to perceive velocity of muscles
      - to perceive strength of muscles
        - to perceive weight information
        - to perceive stiffness information
        - to perceive force being applied
  - to perceive olfactory information
  - to perceive taste information

- 2\. to act on the external environment  
  - to follow instructions/algorithms/protocols
  - to coordinate your actions in a temporal pattern
  - to communicate ideas
    - to speak
      - to ask questions
      - to make statements
    - to write
    - to visually represent information
      <!-- It's like drawing, but faster, variable and the agent can do it with its body, like a screen on its face great way of communicating ideas-->
    - to use body language
  - to manipulate objects with precision
  - [observation] people can continue one action with another without initially planning to do so, just using the association (based on past experience, automatically join action sequences/chunks; weaker version of chunking).

- ?\. [discuss] remember  
  - to manage temporal and long term memory
  - to be able to store, abstract and categorize any type of knowledge

- 4\. to think  
  - to abstract away details, reason about complex systems on a high level
    - to relate words with the concept they represent
  - to reason using logic
  - to do simulate the real world processes (to think about how the world will evolve)
    - to simulate using reasoning
    - to simulate using imagination
  - to plan
    - [observation] Planning does not make us to follow the plan perfectly, we can still deviate from it without mentally changing the plan, so planning is not some built-in functionality, we can actively think about the plan in order to steer our actions. So the planning is not a main mechanism people use to chain actions. It feels more associative, than deterministic.
  - to think about the process of thinking (consciousness, meta cognition)
  - to think temporally (to think about the order of actions. maybe add planning inside)
  - to react accordingly to perceived data
    - to react accordingly to a sentenced perceived
  - to form speech
    - to form questions
    - to form statements
    - to form recursive speech structures
      - to form recursive noun phrases
    - to construct narrative
  - to understand speech
    - to understand recursive speech structures
    - to understand references
      - to understand pronoun references
      - to understand "a \<noun\>" references
      - to understand "the \<noun\>" references
  - to be aware of the context of the other agents
  - to understand spatial concepts
    - to understand the relation between the absolute and conceptual distances
    <!-- 1km if far for a person to travel by foot, but it's near for a spaceship -->
  - to understand temporal concepts

- 5\. to work with memory
  - to form memories (learn)  
    - to do frequent complex actions semiautomatic (motor chunking) <!-- [Check reference 1 in the bottom] -->
    - to learn autonomously (Trial and error, experiment)
      - to infer knowledge
      - to manage new knowledge
    - to be able to abstract any system
    - to generalize knowledge from an instance to a concept
  - to encode memories
    - to represent knowledge about concepts
      - to represent relationships between concepts
        - to represent composition relationships between concepts
          one concept is a part of another concept <!-- What's this?, a line break? a children?-->
        - to represent hierarchies between concepts
        - to represent associations between concepts
          - to represent associations between a concept of a color and another concept
      - to represent a function of a concept
        <!-- possible this is some kind of relation between concepts -->
        - [example] blood transfers oxygen
    - to represent knowledge about objects
    - to represent spatial information
      - to represent absolute abstract location of objects
      - to represent categorical distances between objects
      - to represent relative abstract location of objects
    - to represent temporal information
      - to represent time of events
      - to represent order of events
    - to represent systems
    - to represent cause -> effect relations
      - to represent immediate cause -> effect relations
      - to represent delayed cause -> effect relations
    - to represent any perceived objects and attributes
      - to represent color information
        - to represent conceptual color information
        - to represent conceptual color brightness information
  - to retrieve memories
    - to retrieve spatially close object concepts
    - to retrieve temporally close event concepts

<!-- PATHWAYS: Learn might be one; Communicate -->

<!--  REFERENCES

1: https://en.wikipedia.org/wiki/Chunking_(psychology)

-->