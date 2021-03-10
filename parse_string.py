str= "X-DSPAM-Confidence: 0.8475"
sstr=str.find(":")
nstr=str[sstr+1:]
nstr=float(nstr) #float removes the whitespace. can also use strip
print(nstr)