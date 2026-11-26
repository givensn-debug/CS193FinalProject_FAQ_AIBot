# CS193FinalProject_FAQ_AIBot
A Terraria FAQ chatbot that answers questions given to about Terraria the game.

### The Problem
Terraria is a confusing game and I don't want to navigate the wiki get time I want to be reminded about something. I know a little bit about Terraria so I also don't need the whole wiki page just the summary of the thing. I just want a program that able to help me find out about this Terraria item, bosses, or npcs.

### How It Works
First start with the input of the user's question then the program trims it so it doesn't have as much to deal with. Then using a list of common words that are in questions it removes those words until the question is condensided into only one or two words. Then it searchs those terms in the Terraria wiki to find the best matching title that shows up. Then by grabing that title it goes into that article and pulls the first summary bit that in the wiki articles. Returns that summary as the answer to the user's question. 

### Tech Stack
Python, Intellij, Requests Library, Terraria Wiki

### Setup
1. Clone the Repo with: git clone https://github.com/givensn-debug/CS193FinalProject_FAQ_AIBot
2. Create a virtual environment:
   python3 -m venv .venv
3. Activate it:
    - Windows: `.venv\Scripts\activate`
    - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies:
   pip install -r requirements.txt

### RoadMap
Items:
- X Takes in User's Questions
- X Scans questions for keywords to understand how to answer them
- 0 Plans out a hierarchy so more complex questions can be answered
- 0 Answers questions from a database of already answered questions
- X Redirects users to related websites
- X Pulls from databases to refine answers
- 0 Scale it out bigger so conversations flow better.
- X Makes answers more accuracate to the question.
- 0 Make the Bot understand context
- X Gives out more contextial answers
- X Able to answer questions in trial runs
- X Answers are useful to users
- 0 Switch to RAG based AI
- X Uses a database that isn't my own and pulls from that

Added Feature
- X Redirects to specific article in a database or wiki