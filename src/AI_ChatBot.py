import requests

wikiUrl="https://terraria.wiki.gg/"
headers={"User-Agent":"MyTerrariaFAQBot/1.0 (student_project)"}
#this list of words will be removed so the question only has a search question
stopWords={"how","do","i","get","craft","make","find","summon","defeat","kill","what","is","the","a","an","to","in","terraria","of","for","where","can","you","collect","my"}

def extract_keywords(question: str ):
    #grabs the keywords out of the user's question
    words=question.lower().replace("?","").replace("!","").strip().split()
    keywords=[]
    for word in words:
        if word not in stopWords:
            keywords.append(word)
    if keywords:
        return keywords
    else:
        return words


def main():
    choice=print(
    '''Welcome to my Terraria Chat Bot for the finial project for CS1930. 
    Please Ask about any item, boss, enemies, or npcs(Enter "exit" or "quit" to leave)\n''')
    while True:
        question=input("What is your question: ")
        if question.lower()=="exit" or question.lower()=="quit":
            print("Thanks and Goodbye")
            break
        term=extract_keywords(question)
        print(term)


main()