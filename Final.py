import numpy as np
import re
fp=open("HODwoutenters.txt","r")
contents=fp.read()
contents.replace("\n", " ")
seeker = re.compile("[\.!?]")
sentences = seeker.split(contents)
total = 0
for k in sentences:
    words = k.split(" ")
    length = len(words)
    total += length
    
average = total / len(sentences)
print("The average sentence in this document is",average,"words.")
print()
print("There are",len(sentences),"sentences in this document.")
print()

import string
import operator
search_word = input("Provide word:   ")
frequency = {}
document_text = open("HODwoutenters.txt", "r")
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,25}\b', text_string)

for word in match_pattern:
  count = frequency.get(word,0)
  frequency[word] = count + 1
    

sorted_frequencies = sorted(frequency.items(), key=operator.itemgetter(1), reverse = True)

isWord = 0

for word, frequency in frequency.items():
    if word == search_word:
        isWord += 1
        print("This word appears",frequency,"time(s).")

if isWord != 1:
    print("Sorry! This word does not appear in this document.")

print()

prepositions = ("aboard", "along", "amid", "as", "beneath", "beyond", "but", "concerning", "considering", "despite", "except", "following", "like", "minus", "next", "onto", "opposite", "outside", "past", "per", "plus", "regarding", "round", "save", "since", "than", "underneath", "unlike", "until", "upon", "versus", "via", "within", "wihtout")

preps = 0

pronouns = ("I", "we", "you", "he", "she", "it", "they", "me", "us", "her", "him", "it", "them", "mine", "ours", "yours", "hers", "his", "theirs", "my", "our", "your", "her", "their", "myself", "yourself", "herself", "himself", "itself", "ourselves", "yourselves", "themselves", "myself", "yourself", "herself", "himself", "itself", "ourselves", "yourselves", "themselves", "all", "another", "any", "anybody", "anyone", "anything", "both", "each", "either", "everybody", "everyone", "everything", "few", "many", "most", "neither", "nobody", "none", "nothing", "one", "other", "others", "several", "some", "somebody", "someone", "something", "such", "that", "these", "this", "those", "what", "whatever", "which", "whichever", "who", "whoever", "whom", "whomever", "whose", "as", "what", "thou", "thee", "thy", "thine", "ye")

pros = 0

for k in sentences:
    words = k.split(" ")
    for k in words:
        if k in prepositions:
            preps += 1
        if k in pronouns:
            pros += 1
        
print("There are",preps,"common prepositions in this document.")
print()

print("There are",pros,"common pronouns in this document.")
print()

  
#proper nouns
fp=open("HODwoutenters.txt","r")
contents=fp.read()
contents=contents.replace("--","  ")
contents=contents.replace(","," ")
seeker = re.compile("[\.!?]")
book=seeker.split(contents)
words=[]
for x in book:
    for j in x.split():
        words.append(j)
print(words[0])

capped = [k for k in words if "A" <= k[0] <= "Z"]
#print(capped)
capped = [k for k in capped if k not in["I", "The", "A","In","We","On","He","It","At","Between","Besides","Afterwards",
                                       "For","And","No","They","But","I","Only","For","His","Yes;","Oh","No,","Did","Well"
                                       "Then","I,","Or","You","If","Who","What","Lights","Their",'YOU', 'AGREE', 'THAT', 'YOU', 'HAVE', 'NO',
                                        'REMEDIES', 'FOR', 'NEGLIGENCE,','NEGLIGENCE', 'STRICT', 'LIABILITY,', 'BREACH', 'WARRANTY',
                                        'OR', 'BREACH', 'OF', 'CONTRACT', 'EXCEPT', 'THOSE', 'PROVIDED', 'IN', 'PARAGRAPH',
                                        'F3', 'YOU', 'AGREE', 'THE', 'FOUNDATION,', 'TRADEMARK', 'OWNER,','Knights'
                                        , 'AND', 'ANY', 'DISTRIBUTOR', 'UNDER', 'THIS', 'AGREEMENT', 'WILL', 'NOT', 'BE',
                                        'LIABLE', 'TO', 'YOU', 'FOR', 'ACTUAL,', 'DIRECT,', 'INDIRECT,', 'CONSEQUENTIAL,',
                                        'PUNITIVE', 'OR', 'INCIDENTAL', 'DAMAGES', 'EVEN', 'YOU', 'GIVE', 'NOTICE', 
                                         'POSSIBILITY', 'SUCH', 'DAMAGE', 'LIMITED', 'RIGHT', 'OF','Light','Imagine',
                                        'REPLACEMENT', 'OR', 'REFUND', 'F', 'Except', 'WITH','Sandbanks,',"Here","There's",
                                        'NO', 'OTHER', 'WARRANTIES', 'OF', 'ANY', 'KIND,', 'EXPRESS', 'OR', 'IMPLIED,',
                                        'INCLUDING', 'BUT', 'NOT', 'LIMITED', 'TO', 'WARRANTIES','MERCHANTIBILITY', 'An',
                                         'FITNESS', 'FOR', 'ANY', 'PURPOSE', 'F', 'Some', 'If', 'INDEMNITY','Forthwith','Hunters','One'
                                       ,"Well,","Other","Then","Why","Street", "This","So","She","Its","From","Yes,","Not","Oh","There"
                                       ,"Therefore","Oh,","These","Then","Nothing", "I've","My","Was","By","Is","It's","When","Before","Two","All"
                                       ,"Don't", "One's",'People','While','Deal','Once','Good-by','Still','V-shaped','E',
                                       'Within','Well','As','To','Most','See','Sometimes','Finally','Often',"I'll",'I;','Her','After',
                                       'Behind','Like', 'Just','Am',"That's","Hadn't",'Do',"Can't",'Six','Moreover','Very','Everyone','Certainly'
                                       ,'Yes','Rivets','Fine']]
print(capped) #list of proper nouns
print()
print(len(capped)) #number of proper nouns
print()

#conjunctions
import re
fp=open("HODwoutenters.txt","r")
contents=fp.read()
seeker = re.compile("[\.!?]")
book=seeker.split(contents)
words=[]
for x in book:
    for j in x.split():
        words.append(j)

Corrdinating = [k for k in words if k in ["For","for","And","and","But","but","Or","or","Yet","yet","So","so"]]
print("The number of Corrdinating Conjunctions is", len(Corrdinating))
print()

Subordinating = [k for k in words if k in ["after","although","as","as if","if","in order that","in case",
                                          "as long as","as much as","as soon as","lest","once","only if",
                                          "as though","because","before","provided that","since","so that",
                                          "by the time", "even if",  "even though","than","that","though","till",
                                           "unless","until","when","whenever","where","wherever","while"]]
print("The number of Subordinating Conjunctions is", len(Subordinating))
print()

Correlative = [k for k in words if k in ["both","either","neither","not only","whether"]]

print("Here is a sorted word frequency list:",sorted_frequencies)


#pronouns
fp=open("HODwoutenters.txt","r")
contents=fp.read()
contents=contents.replace(","," ")
seeker = re.compile("[\.!?]")
book=seeker.split(contents)
words=[]
for x in book:
    for j in x.split():
        words.append(j)

Demonstrative = [k for k in words if k in ["this","This","These","these","that","That","Those","those"]]
print("The number of Demonstrative Pronouns is", len(Demonstrative))

Personal= [k for k in words if k in ["I","me","Me","we","We","Us","us","you","You","She","she","Her","her","he","Him","him","He","It","it","they","They","Them","them"]]
print("The number of Personal Pronouns is", len(Personal))

Relative= [k for k in words if k in ["That","that","which","Which","Who","who","Whom","whom","Whose","whose","Whichever","whichever","Whoever","whoever","Whomever","whomever"]]
print("The number of Relative Pronouns is", len(Relative))


Indefinite= [k for k in words if k in ["anyone","Anyone","anybody","Anybody","Anything","anything","Each","each","either","Either","everybody","Everybody","Everyone","everyone","everything","Everything","neither","Neither","Nobody","nobody","no one","No one","Nothing","nothing","one","One","somebody","Somebody","someone","Someone","something","Something",
                                      "both","Both","few","Few","many","Many","several","Several"
                                      ,"all","All","any","Any","most","Most","none","None","some","Some"]]
print("The number of Indefinite Pronouns is", len(Indefinite))

Reflexive= [k for k in words if k in ["myself","Myself","ourselves","Ourselves","yourself","Yourself","Yourselves","yourselves","himself","Herself","herself","Herself","itself","Itself","themselves","Themselves"]]
print("The number of Reflexive Pronouns is", len(Reflexive))


Interrogative= [k for k in words if k in ["what","who","which","whom","whose","What","Who","Which","Whom","Whose"]]
print("The number of Interrogative Pronouns is", len(Interrogative))


Possessive= [k for k in words if k in ["my","our","your","his","her","its","their","My","Our","Your","His","Her","Its","Their","mine","yours","hers","ours","theirs","Mine","Yours","Hers","Ours","Theirs"]]
print("The number of Possessive Pronouns is", len(Possessive))


SubjectandObject= [k for k in words if k in ["I","you","she","he","it","we","they","She","He","It","We","You","They"
                                            ,"me","her","him","us","them","Me","Her","Him","Us","Them"]]
print("The number of SubjectandObject Pronouns is", len(SubjectandObject))







