# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked pretty normal at first. After typing a number it said "Press enter to apply" but pressing enter doesn't work. Then after running one number it didn't show up in the History.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The game starts off giving you 8 attempts but says "Attempts left: 7" as if I already used an attempt.
It doesn't always update correctly when you submit a guess. For example the attempts don't subtract by one or the hint isn't shown.
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
 1.
 Input: Select Hard difficulty; read the info banner
 Expected Behavior: Banner says "Guess a number between 1 and 50" 
 Actual Behaviour: Banner always says "Guess a number between 1 and 100" regardless of difficulty
 Console: none — st.info hardcodes "1 and 100" instead of using {low} and {high}

 2.
 Input: Win or lose a game, then click New Game
 Expected Behavior: Game resets fully and lets you play again
 Actual Behaviour: Shows "You already won / Game over. Start a new game." and blocks play immediately
 Console: none — st.session_state.status is never reset to "playing" in the new_game block
 
 3.
 Input: On your 2nd guess (even attempt), enter a number whose string sort differs from numeric sort — e.g., secret = 50, guess = 6
 Expected Behavior: Hint: "📉 Go LOWER!" (6 < 50)
 Actual Behaviour: Hint: "📈 Go HIGHER!" — because "6" > "5" lexicographically
 Console: none — on even attempts the secret is cast to str, triggering the TypeError fallback which uses string comparison
 
 4.
 Input: Make a guess that is Too High on attempt 2, 4, or 6
 Expected Behavior: Score should decrease (wrong guess penalty)
 Actual Behaviour: Score increases by 5 points
 Console: none — update_score awards +5 for "Too High" when attempt_number % 2 == 0, which is the opposite of the intended penalty

 
1. I clicked "New Game" and it wouldn't restart and said "Game over. Start a new game to try again"

2. I guessed on the first try because it tells you the answer but it said my final score was a 70.

3. If you win it doesn't let you start a new game even though it says to.

4. It'll tell you to go higher when the number is truly lower and vice versa

5. I put in 700 and it told me to "Go HIGHER!" but I already went about the limit.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
