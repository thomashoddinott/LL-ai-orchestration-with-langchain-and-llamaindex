### AI Orchestration Frameworks
A software tool to:
- help coordinate the overall operation of AI applications
- hide the when the specific details and boiler plate code needed to talk to the APIs

### Retrieval-augmented generation (RAG)
![alt text](image.png)
![alt text](image-1.png)

### AI-Centric vs Code-Centric Prompts
e.g.
![alt text](image-2.png)

| Approach            | Pros                                                                 | Cons                                                                 |
|----------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| **AI-centric** (LLM handles sorting) | ✅ Simple pipeline — minimal code needed.<br>✅ Quick to prototype.<br>✅ Good for fuzzy or subjective sorting (“by importance”, “by tone”). | ❌ Unreliable — LLM may mis-sort or ignore instructions.<br>❌ Hard to verify errors automatically.<br>❌ Limited recovery options (requires re-prompting or manual fix). |
| **Code-centric** (sort in Python) | ✅ Deterministic and testable results.<br>✅ Clear error handling and logging possible.<br>✅ Keeps logic separate — LLM generates data, code processes it. | ❌ Requires parsing/validation (e.g., JSON).<br>❌ More plumbing and error-handling code.<br>❌ Slightly higher latency or complexity. |

**Rule of Thumb**
For anything for which you would have written code, even before you heard of LLM's, choose a code-centric approach.

### LLM function calling

**Warning** 
- Limit access, supervise everything

### ReAct Agent Framework
![alt text](image-3.png)