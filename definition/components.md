# Agent Components/Processes

- Raw Data Processing
    - Text Processing
    - Vision
    - Hearing
- Abstract Data Representation
    - World Model Representation  
        This component models the state of the real world.
    - Knowledge Representation
    - Plan Representation
    - Goal Representation
    - Action Representation
        - Fuzzy Action Sequence Representation
            A sequence of actions might be continued differently depending on the context. So it's not a proper list, more like a weighted graph, where the weight decides on the next action to take when several options are present and context influences the weight.
- Abstract Data Processing
    - Memory Retrieval
        - Context-aware Associative Concept Retrieval
    - Learning
- Acting
