<!-- 
When adding an ability, check if 
- it makes sense for a human, symbolic agent, and an LLM 
- a regular person would say that they have this ability if asked
- you are adding it in a correct place, make sure the children are extensions/specifications of the parent. Remember that this is not a tree of dependencies - don't add children abilties because they are required to do the parent ability. For example `ability to store produral knowledge` should not be under the `ability to act`, it is indeed required to act, but it's not an expansion of the `ability to act`.

tags:
- `explain` - please provide an example in the PR comment
- `invalid` - the entry is not formulated as an ability
- `remove` - the entry is not needed because it is invalid or unclear,it needs to be deleted or replaced

It's a good idea to reolve all the tags before merging a PR.
-->

# Ability List

Ability ...

- 1\. to perceive
  - 1.1 [explain] to simplify perceived entities or their attributes into single simpler ones
  - 1.2 to see
    - 1.2.1 to read text
  - 1.3 to hear
  - 1.4 [explain] to be able to identify and abstract any object or concept

- 2\. to make decisions
  - [explain,invalid] Association cause -> effect
  - to reason using logic
  - to do simulate the real world
  - to plan
    - [explain] to do mental logic processes
      - [explain] to compare something

- 3\. to communicate
  - to react accordingly to the sentence heard (IN)
    <!-- (This can be an instruction, a question, etc.) -->
  - to communicate ideas (OUT)
    - to ask questions (IN)
    - to answer questions (OUT)
  - to relate words with the concept they represent
    <!-- This ability is crucial to truly understand any sentence -->
- 4\. to learn
  - to learn autonomously (Trial and error, experiment)
    - to infer knowledge
    - to manage new knowledge

- 5\. to act
  - to make frequent complex actions semiautomatic (Act solidification)
  - to follow instructions/algorithms/protocols
  - to coordinate your actions in a temporal pattern

- 6\. [remove] to represent and remember
  - [remove] to understand time
    - to understand sequenciation
    - to understand time linked events
  - [remove] to store semantic memories
  - [remove] to store episodic memories
  - to manage temporal and long term memory
  - to be able to store, abstract and categorize any type of knowledge

- 6\. to represent knowledge
  - 6.1 to represent conceptual knowledge
    - 6.1.1 to represent conceptual hierarchies
  - 6.2 to represent spatial information
    - 6.2.1 to represent absolute abstract location of objects
    - 6.2.2 to represent categorical distances between objects
    - 6.2.3 to represent relative abstract location of objects
    - 6.2.4 to associate spatially close objects
  - 6.3 to represent temporal information
    - 6.3.1 to represent time of events
    - 6.3.2 to represent order of events
    - 6.3.3 to associate temporally close events
