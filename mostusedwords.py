paragraph= "You're a son of a , you know that? She bought her first new car and you hit her with a drunk driver.  What, is that supposed to be funny? \"You can\'t conceive, nor can I, the appalling strangeness of the mercy of God,\" says Graham Greene. I don\'t know whose ass he was kissing there, because I think you\'re just vindictive. What was Josh Lyman, a warning shot? That was my son. What did I ever do to Yours but praise His glory, praise His name? There\'s a tropical storm that\'s gaining speed and power. They say we haven\'t had a storm this bad since you took out that tender ship of mine in the North Atlantic last year. 68 crew, you know what a tender ship does? It fixes the other ships, doesn\'t even carry guns, it just goes around and fixes the other ships, delivers the mail, that\'s all it can do. Gratias tibi ago, domine. Yes, I lied. I committed a sin, I\'ve committed many sins. Have I displeased you, you feckless thug? 3.8 million new jobs, that wasn\'t good? Bailed out Mexico, increased foreign trade? 30 million new acres for conservation? Put Mendoza on the bench? We\'re not fighting a war, I\'ve raised three children, that\'s not enough to buy me out of the doghouse? Haec credam a deo pio? A deo iusto, a deo scito? Cruciatus in crucem. Tuus in terra servus, nuntius fui. Officium perfeci. Cruciatus in crucem. Eas in crucem!  You get Hoynes!"
words=paragraph.split() #splits the paragraph string into a list of words

count=dict() #makes new dictionary
for eachword in words: # for each word in the paragraph
    count[eachword]=count.get(eachword,0)+1 #add one to the count for each word, and for each new word create new count with default value 0 

vklist=list() #create empty list for the flipped tuples to go
for k,v in count.items(): #for each tuple created by count.items
    ntuple=(v,k) #creae a new tuple written as v,k
    vklist.append(ntuple) #and add it to vklist

vklist=sorted(vklist, reverse=True) #sort list largest to smallest value

mostused10=list() #create empty list
for v,k in vklist[:10]: #for the first 10 v,k of vklist
    fliptuple=(k,v) #flip each to k,v and assign to fliptuple
    mostused10.append(fliptuple) #append to empty list

print(mostused10) #print list of 10 most used words

#SHORT VERSION OF CODE:
print(sorted([(v,k) for k,v in count.items()], reverse=True))