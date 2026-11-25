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
