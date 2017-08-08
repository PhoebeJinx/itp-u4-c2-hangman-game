from exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['cat', 'dog', 'elephant', 'pig', 'horse', 'hippo', 'tiger', 'deer', 'squirrel', 'bear']


def _get_random_word(list_of_words):
    
    if not list_of_words:
        raise InvalidListOfWordsException
    else: 
        random_word = random.choice(list_of_words)
    return random_word


def _mask_word(word):

    if not word:
        raise InvalidWordException
    else:
        mask_word = len(word) * "*"
    return mask_word

def _uncover_word(answer_word, masked_word, character):
    
    #Exception - 1
    if not answer_word:
        raise InvalidWordException
    
    if not masked_word:
        raise InvalidWordException
        
    if len(character) > 1:
        raise InvalidGuessedLetterException
        
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    
    if character.lower() in answer_word.lower():
        
        # find position(s) of character in answer_word
        char_positions = []
        
        for idx, char in enumerate(answer_word):
            if char.lower() == character.lower():
                char_positions.append(idx)
        
        #convert masked_word to list    
        conv_maskword_to_list = list(masked_word)
        
        #replace asterisk with character
        for num in char_positions:
            conv_maskword_to_list[num] = character.lower()
        
        # convert list back to string
        output = ''
        for char in conv_maskword_to_list:
            output += char
        #masked_word = output
        
        return output
    
    else:
        return masked_word

def guess_letter(game, letter):
    
    if game["remaining_misses"] == 0:
        raise GameFinishedException
        
    if game["answer_word"] == game["masked_word"]:
        raise GameFinishedException 
    
    guess = _uncover_word(game["answer_word"], game["masked_word"], letter)
    
    if guess == game["masked_word"]:
        game["remaining_misses"] = game["remaining_misses"] - 1
   
    game["masked_word"] = guess
    game["previous_guesses"].append(letter.lower()) 
    
    if guess == game["answer_word"]:
        raise GameWonException
     
    if game["remaining_misses"] == 0:
        raise GameLostException
    
    return game
    

def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS
    
    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
