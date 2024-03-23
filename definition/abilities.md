<!-- 
When adding an ability, check if 
- it makes sense for a human, symbolic agent, and an LLM 
- a regular person would say that they have this ability if asked
- you are adding it in a correct place, make sure the children are extensions/specifications of the parent. Remember that this is not a tree of dependencies/components - don't add children abilties because they are required to do the parent ability. For example `ability to store produral knowledge` should not be under the `ability to act`, it is indeed required to act, but it's not an expansion of the `ability to act`.
- it does not intersect different parent abilities, like the ability "to communicate" is about percieving what is being told to you, action of giving a response and mental process of coming up with an answer. Such abilities need to be divided into parts that don't span across multiple parent abilities.

tags:
- `explain` - please provide an example in the PR comment
- `invalid` - the entry is not formulated as an ability
- `remove` - the entry is not needed because it is invalid or unclear,it needs to be deleted or replaced
- `composite` - this ability spans across different parent abilities and needs to be split up
- `example` - not an ability, but it's example. replace with an actual ability when ready

It's a good idea to reolve all the tags before merging a PR.
-->

# Ability List

Ability ...

- 1\. to perceive information  
  - 1.1 to percieve visual information
    - 1.1.1 to percieve textual information
      - to percieve vertical textual information
    - 1.1.2 to percive brightness information
    - 1.1.3 to percive color information
    - 1.1.4 to percive texture information
    - 1.1.5 to percive proximity information
  - 1.2 to percive auditory information
  - 1.3 to percive tactile information
  - 1.4 to percive olfactory information
  - 1.5 to percive balance and orientation information

- 2\. to act on the external environment  
  - to follow instructions/algorithms/protocols
  - to coordinate your actions in a temporal pattern

  - 2.3 [discuss,composite] to communicate
    - to react accordingly to the sentence heard (IN)
      <!-- (This can be an instruction, a question, etc.) -->
    - to communicate ideas (OUT)
      - to ask questions (IN)
      - to answer questions (OUT)
    - to relate words with the concept they represent
      <!-- This ability is crucial to truly understand any sentence -->

- 3\. to learn  
  - to learn autonomously (Trial and error, experiment)
    - to infer knowledge
    - to manage new knowledge
  - to transfer abstract knowledge between systems
  - to generalise knowledge from an instance to a concept
  - to make frequent complex actions semiautomatic (Act solidification)

- ?\. [discuss] remember  
  - to manage temporal and long term memory
  - to be able to store, abstract and categorize any type of knowledge

- 4\. to think  
  - to abstract away details, reason about complex systems on a high level
  - to reason using logic
  - to do simulate the real world processes (to think about how the world will evolve)
    - to simulate using reasoning
    - to simulate using imagination
  - to plan
  - to think about the process of thinking (consciousness, meta congnition)
  - to think temporaly (to think about the order of actions. maybe add planning inside)

- 5\. to represent knowledge/memory  
  - 5.1 to represent knowledge about concepts (semantic)
    - 5.1.1 to represent hierarchies of concepts
    - 5.1.2 [discuss] to represent episodic knowledge about concepts ???
    - 5.1.3 to represent semantic knowledge about concepts
      - [example] people have one head
      - [example] blood transfers oxygen
    - 5.1.4 to represent associatians between concepts
      - 5.1.4.1 to represent associations between a concept of a color and another concept
  - 5.2 to represent knowledge about objects
    - 5.2.1 to represent episodic knowledge about objects
    - 5.2.2 to represent semantic knowledge about objects
  - 5.3 to represent spatial information
    - 5.3.1 to represent absolute abstract location of objects
    - 5.3.2 to represent categorical distances between objects
    - 5.3.3 to represent relative abstract location of objects
    - 5.3.4 to associate spatially close objects
  - 5.4 to represent temporal information
    - 5.4.1 to represent time of events
    - 5.4.2 to represent order of events
    - 5.4.3 to associate temporally close events
  - 5.5 to represent systems
  - 5.6 to represent cause -> effect relations
    - 5.6.1 to represent immediate cause -> effect relations
    - 5.6.2 to represent delayed cause -> effect relations
  - 5.7 to represent color information
    - 5.7.1 to represent conceptual color information
    - 5.7.2 to represent conceptual color brightness information
