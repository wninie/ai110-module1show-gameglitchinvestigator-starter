# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
The hints were broken, it seems like it is hinting the opposite. For example the number to be guessed was 15, and I guessed 1, the hint would tell me to go lower. On the other hand if I guessed 89, the hint would tell me to go higher. I also noticed that you can only play this game once. Once you press the new game button, it will reset your "attempts left" but you won't be able to submit a new guess. 

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|NewGame| Restart game      |Restart but cant |
|       |                   | submit guesses  |
-------------------------------------------------
| 100   | Go lower hint     | Go higher hint  |                         |
| 0     | go higher hint    | Go lower hint   |                        |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude!
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  I had asked about the logic of the hints and why they were wrong. It then showed me the code and explained what the logic error was and event went beyond to say why this might've happend. I then went and looked at the code in app.py and it seemed to make sense. I knew what the bug was and how to fix it before I had asked so I think this just confirmed/verfiyed it for me.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  It wasn't misleading or incorrect but when I had asked it to make pytest, it was doing a lot of things that I had to look over. Many I googled because I wasn't sure about the bash commands it was using, after I made sure that it was okay to proceed, it would make the commands and continue.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I played the game myself many times and ran the test!
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  A manual test I did was just playing the game and trying to guess the right number based on the hints. This showed me that my code no longer had misleading hints because the code outputed the right hint. It also showed me that I am still a little confused on how the point system works but I do know that if your number was too high, your points would still be -=5.
- Did AI help you design or understand any tests? How?
 It did! It wrote the test for me when I prompted it to write specific cases and would tell me if this was a good test or not and why.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would it explain it as like, every time you interact with the app like when you click a button, streamlit reruns the entire script from the top to the bottom. And state is like a box that saves your variables between the runs so your variabls do not reset all everytime you click a button.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I liked how we started a new chat for each feature/fix, I think having AI be focused on one thing gave clean suggestions and I will continue to do that from now on.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I want to go slower next time so I fully understand all the code before AI is able to touch anything
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project changed my thinking about AI generated code because I honestly always think its correcct and I can just trust it blindly but there were many times where I was a bit skeptical while doing this projected which led me to double checking things.
