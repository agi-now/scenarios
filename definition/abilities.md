<!-- 
When adding an ability, check if 
- it makes sense for a human, symbolic agent, and an LLM 
- a regular person would say that they have this ability if asked
- you are adding it in a correct place, make sure the children are extensions/specifications of the parent. Remember that this is not a tree of dependencies/components - don't add children abilties because they are required to do the parent ability. For example `ability to store produral knowledge` should not be under the `ability to act`, it is indeed required to act, but it's not an expansion of the `ability to act`.

tags:
- `explain` - please provide an example in the PR comment
- `invalid` - the entry is not formulated as an ability
- `remove` - the entry is not needed because it is invalid or unclear,it needs to be deleted or replaced

It's a good idea to reolve all the tags before merging a PR.
-->

# Ability List

Ability ...

- 1\. to perceive
  - 1.1 to see
    - 1.1.1 to read text
  - 1.2 to hear

- 2\. to communicate
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

- 4\. to act
  - to make frequent complex actions semiautomatic (Act solidification)
  - to follow instructions/algorithms/protocols
  - to coordinate your actions in a temporal pattern

- ?\. [discuss] remember
  - to manage temporal and long term memory
  - to be able to store, abstract and categorize any type of knowledge

- 5\. to think
  - to abstract away details, reason about complex systems on a high level
  <!-- - to make decisions -->
  - to reason using logic (reason = fancy think)
  - to do simulate the real world processes (to think about how the world will evolve)
    - to simulate using reasoning
    - to simulate using imagination
  - to plan (to think about your next actions)
  - to think about the process of thinking (consciousness, meta congnition)
  - to think temporaly (to think about the order of actions. maybe add planning inside)

- 6\. to represent knowledge/memory
  - 6.1 to represent knowledge about concepts (semantic)
    - 6.1.1 to represent hierarchies of concepts
    - [discuss] to represent episodic knowledge about concepts ???
    - to represent semantic knowledge about concepts
  - 6.2 to represent knowledge about objects
    - to represent episodic knowledge about objects
    - to represent semantic knowledge about objects
  - 6.3 to represent spatial information
    - 6.3.1 to represent absolute abstract location of objects
    - 6.3.2 to represent categorical distances between objects
    - 6.3.3 to represent relative abstract location of objects
    - 6.3.4 to associate spatially close objects
  - 6.4 to represent temporal information
    - 6.4.1 to represent time of events
    - 6.4.2 to represent order of events
    - 6.4.3 to associate temporally close events
  - 6.5 to represent systems
  - 6.6 to represent cause -> effect relations
    - 6.6.1 to represent immediate cause -> effect relations
    - 6.6.2 to represent delayed cause -> effect relations
