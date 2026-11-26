import requests

wikiUrl="https://terraria.wiki.gg/api.php"
headers={"User-Agent":"MyTerrariaFAQBot/1.0 (student_project)"}
def extractKeywords(question: str ):
    #this list of words will be removed so the question only has a search question
    stopWords={"how","do","i","get","craft","make","find","summon","defeat","kill","what","is","the","a","an","to","in","terraria","of","for","where","can","you","collect","my","game","please","for","with","about","during","before",""}
    #grabs the keywords out of the user's question
    words=question.lower().replace("?","").replace("!","").strip().split()
    keywords=[]
    for word in words:
        if word not in stopWords:
            keywords.append(word)
    if keywords:
        keywords=" ".join(keywords)
        return keywords
    else:
        words=" ".join(words)
        return words

def wikiSearch(term: str)->tuple[str,str,str]:
    #intializes the parameters of the web title
    titleParams={"action":"query","list":"search","srsearch":term,"format":"json","srlimit":1}
    #grabs the title of the article that can answer the question
    response=requests.get(wikiUrl,params=titleParams,headers=headers).json()
    searchResponses=response.get("query",{}).get("search",[])
    if not searchResponses:
        return "","",""
    title=searchResponses[0]["title"]

    #does the same thing but for the summary instead
    summaryParams={"action":"query","prop":"extracts|info","inprop":"url","exintro":True,"explaintext":True,"titles":title,"format":"json"}
    sumResponse=requests.get(wikiUrl,params=summaryParams,headers=headers).json()
    pages=sumResponse.get("query",{}).get("pages",{})
    summary=""
    link=""
    for page in pages.values():
        summary+=page.get("extract","")
        link+=page.get('fullurl'," ")
    return title, summary, link

def main():
    choice=print(
    '''Welcome to my Terraria Chat Bot for the finial project for CS1930. 
Please Ask about any item, boss, enemies, or npcs(Enter "exit" or "quit" to leave)\n''')
    while True:
        question=input("What is your question: ")
        if question.lower()=="exit" or question.lower()=="quit":
            print("Thanks and Goodbye")
            break
        term=extractKeywords(question)
        title, summary, link =wikiSearch(term)
        if summary:
            print("\n",summary)
            if link != "":
                print("If that didn't help with your question go to", link ,"\n")
        else:
            print("Please repharse or change your question")

main()