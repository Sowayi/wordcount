#function receives an argument in form of a sentence
def word_count (a_sentence):

    #creates an empty dictionary 
    word_counter= {}
    
    #each individual word is analyzed after the sentence is split
    words=sentence.split

    for word in words:
             
        for word_outliner in ["."," " '\n', '\t']:
                 
        # The removes from list the word outliners such as space
        
            words = [word.split(word_outliner)[0]]

            if not word.isdigit():

                    word_counter= {word:words.count}
             
            elif word.isdigit():

                     word_counter.update({int(word):words.count(word)})
