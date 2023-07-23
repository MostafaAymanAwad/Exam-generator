# -*- coding: utf-8 -*-
"""Fix Sense2vec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C7aWMCyxBEw57uIO69lKNiVcoEG179YO
"""

!pip install sense2vec==2.0.0
!pip install spacy
!pip install word2number
!pip install nltk

!wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2019_lg.tar.gz.001
!wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2019_lg.tar.gz.002
!wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2019_lg.tar.gz.003
!cat s2v_reddit_2019_lg.tar.gz.* > s2v_reddit_2019_lg.tar.gz
!tar -xvf  s2v_reddit_2019_lg.tar.gz

from sense2vec import Sense2Vec
import spacy
import re
from word2number import w2n
from collections import OrderedDict
import nltk
from nltk.stem import WordNetLemmatizer

spacy.cli.download('en_core_web_lg')
nlp = spacy.load('en_core_web_lg')
s2v = nlp.add_pipe('sense2vec')
s2v.from_disk("s2v_reddit_2019_lg")

# ps = PorterStemmer()

ps = WordNetLemmatizer()

def common(s0, s1):
  s0 = remove_non_alphanumeric(s0.lower())
  s1 = remove_non_alphanumeric(s1.lower())
  s0Words = s0.split(' ')
  s1Words = s1.split(' ')
  return len(list(set(s0Words)&set(s1Words)))

def remove_non_alphanumeric(word):
    pattern = r'[^\w]'
    return re.sub(pattern, ' ',word)


def sense2vec_get_words(context):
  doc=nlp(context)
  output2 = []

  for ent in doc.ents:
    try:
      output = set()
      most_similar=ent._.s2v_most_similar(15)
      for (word,label),score in most_similar:

        if label == ent.label_:
          append_word = word.lower()

          append_word = append_word.replace('/', ' ').replace('-', ' ')
          new_append_word = remove_non_alphanumeric(append_word)
          new_word = remove_non_alphanumeric(ent.text.lower())

          new_word2=''
          if ent.label_=='CARDINAL':
            new_word2=str(w2n.word_to_num(new_word))

          new_word2 = remove_non_alphanumeric(new_word2.lower())

          if new_append_word not in new_word and new_word not in new_append_word and common(new_word,new_append_word) == 0 and  common(new_word2,new_append_word) == 0:
              output.add(append_word.title())
            # else:
            #   output.add(append_word.title())

      output2.append( [ent.text,list(OrderedDict.fromkeys(output))])
    except Exception as e:
      print(f"An error occurred: {str(e)}")

  print(output2)
  return output2

# context = " Software quality assurance (SQA)  is the ongoing process that ensures the software product meets and complies with the organization's established and standardized quality specifications, Focuses on process standard, projects audit, and procedures for development, Focuses on evaluating and improving the processes to deliver quality products It is typically accomplished by using well-planned standard systems, covering processes and tools for quality control to assure the reliability and dependability of the product. "
# context = "Vitamin B12 is synthesized solely by microorganisms In humans, the only source for humans is food of animal origin , e.g., meat, fish, and dairy products.* Vegetables, fruits, and other foods of nonanimal origin doesn't contain Vitamin B12 .* Daily requirements of vitamin Bp is about 1-3 pg. Body stores are of the order of 2-3 mg, sufficient for 3-4 years if supplies are completely cut off."
context="As at most other universities, Notre Dame's students run a number of news media outlets. The nine student-run outlets include three newspapers, both a radio and television station, and several magazines and journals. Begun as a one-page journal in September 1876, the Scholastic magazine is issued twice monthly and claims to be the oldest continuous collegiate publication in the United States. The other magazine, The Juggler, is released twice a year and focuses on student literature and artwork. The Dome yearbook is published annually. The newspapers have varying publication interests, with The Observer published daily and mainly reporting university and other news, and staffed by students from both Notre Dame and Saint Mary's College. Unlike Scholastic and The Dome, The Observer is an independent publication and does not have a faculty advisor or any editorial oversight from the University. In 1987, when some students believed that The Observer began to show a conservative bias, a liberal newspaper, Common Sense was published. Likewise, in 2003, when other students believed that the paper showed a liberal bias, the conservative paper Irish Rover went into production. Neither paper is published as often as The Observer; however, all three are distributed to all students. Finally, in Spring 2008 an undergraduate journal for political science research, Beyond Politics, made its debut."
distractors = sense2vec_get_words(context)

import nltk
from nltk.tokenize import sent_tokenize

def tokenize_sentences(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    return sentences

# Example usage
text = "This is the first sentence. This is the second sentence. And this is the third sentence. this info. about the internet."
sentences = tokenize_sentences(text)
print(sentences)