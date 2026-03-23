"""
Test class for Hangman implementation.

@author xt0fer
@version 1.0.0
@date 5/27/21 11:02 AM
"""
from python.wordguess import WordGuess
import python.wordguess as WordGuess

class TestHangman:  
    """Test class for Hangman - ready for test implementation."""
    pass
def test_get_random_word():
    """Test get random word method for Hangman game."""
    word = WordGuess.get_random_word(WordGuess.word_list)
    assert word in WordGuess.word_list

def test_display_word_progress():
    """Test display word progress method for Hangman game."""
    word = "hangman"
    guessed_letters = {'a', 'n'}
    expected_display = "_ a n _ _ a n"
    
    # Capture the output of the display_word_progress function
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    WordGuess.display_word_progress(word, guessed_letters)
    
    sys.stdout = sys.__stdout__  # Reset redirect.
    
    actual_display = captured_output.getvalue().strip()
    
    assert actual_display == expected_display