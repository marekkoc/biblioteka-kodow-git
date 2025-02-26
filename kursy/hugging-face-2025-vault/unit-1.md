---
Utworzono: 2025-02-12T06:37:00 <br>
Zmodyfikowano: 2025-02-20T06:37:00 <br>

Źródło: https://huggingface.co/learn/agents-course/unit1/introduction <br>

tags: <br>
Katalog:


---
# Unit 1.  [Introduction to Agents](https://huggingface.co/learn/agents-course/unit1/introduction)


## [What are LLMs?](https://huggingface.co/learn/agents-course/unit1/what-are-llms)

Darmowy kurs w którym można się dowiedzieć więcej na tema LLM [free Natural Language Processing Course](https://huggingface.co/learn/nlp-course/chapter1/1)


The Agent Workflow:

Think → Act → Observe.


## [Understanding AI Agents through the Thought-Action-Observation Cycle - Hugging Face Agents Course](huggingface.co/learn/agents-course/unit1/thoughts)

### The Re-Act Approach

- A key method is the ReAct approach, which is the concatenation of “Reasoning” (Think) with “Acting” (Act).

- ReAct is a simple prompting technique that appends “Let’s think step by step” before letting the LLM decode the next tokens.

 - Indeed, prompting the model to think “step by step” encourages the decoding process toward next tokens that generate a plan, rather than a final solution, since the model is encouraged to decompose the problem into sub-tasks.

- This allows the model to consider sub-steps in more detail, which in general leads to less errors than trying to generate the final solution directly.

- The (d) is an example of Re-Act approach where we prompt "Let's think step by step"


##  [Observe: Integrating Feedback to Reflect and Adapt](https://huggingface.co/learn/agents-course/unit1/observations)

 - Observations are how an Agent perceives the consequences of its actions.
   
 - They provide crucial information that fuels the Agent’s thought process and guides future actions.