import spacy


def cleanup(token, lower = True):
    if lower:
       token = token.lower()
    return token.strip()

nlp = spacy.load('en')

# doc5 = nlp(u"Rami Eid is studying at Stony Brook University in New York")
#
# for ent in doc5.ents:
#     print(ent, ent.label, ent.label_)
#
#
# doc6 = nlp(u"Natural language processing (NLP) deals with the application of computational models to text or speech data.")
#
# for np in doc6.noun_chunks:
#     print(np)


#########
document = nlp(open('/Users/stevenliu/Desktop/NSWSC/NSWSC_1997_359.html').read())
for np in document.noun_chunks:
    print(np)

# labels = set([w.label_ for w in document.ents])
# for label in labels:
#     entities = [cleanup(e.string, lower=False) for e in document.ents if label == e.label_]
#     entities = list(set(entities))
#     print(label, entities)
#########