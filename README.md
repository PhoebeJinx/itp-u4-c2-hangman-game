# Hangman Game

Today we are going to re-create the game 'Hangman' in Python!

It is broken down into several small functions that, when combined and
completed, form a working game!

We're providing the main function `start_new_game`, that just relies on your other smaller functions to work.

These are the functions that you have to implement:

### Mask Word

```bash
$ py.test tests.py -k mask_word
```

Given a word like `'Python'`, it returns it "masked" (replacing real characters with asterisks): `'******'`


### Uncover Word

```bash
$ py.test tests.py -k uncover_word
```

This is probably one of the most challenging ones (it has many exceptional cases). Given an answer word (like `'Python'`) a masked word (like `'******'` or `'*y****'`) and a guessed letter (`'n'` for example) it returns a new masked word replacing the asterisks with the guessed letter **IF** the letter is present in the word to answer. Examples:

```python
_uncover_word('Python', '******', 'y')  # '*y****'  # Match
_uncover_word('Python', '*y****', 'n')  # '*y***n'  # Match

_uncover_word('Python', '******', 'x')  # '******'  # Miss
_uncover_word('Python', '*y****', 'x')  # '*y****'  # Miss
```

### Get Random Word

```bash
$ py.test tests.py -k get_random_word
```

Receives a list of words and returns one from the list randomly.


### Guess Letter

```bash
$ py.test tests.py -k guess
```

Probably the most "important" (or "general") function. We recommend you to deal with this function **after** you've completed the other ones.

It receives a `game` object and a letter to guess. It has several different scenarios. For example, the guessed word is a match or a miss, the game is won or lost, or the game was already over.
