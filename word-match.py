# Step 1: Import the random module to use for shuffling lists
import random
# Step 2: Create a function to generate randomized matrices from English and Spanish word lists.

def generate_random_matrix(rows, cols, words1, words2):
   
    # Calculate the total number of words needed for the matrices
    total_words = rows * cols
    if total_words > len(words1) or total_words > len(words2):
        raise ValueError("Matrix size exceeds the number of available words.")
    
    paired_words = list(zip(words1, words2))
    random.shuffle(paired_words)
    
    english_words, spanish_words = zip(*paired_words)
    
    # Shuffle Spanish words to ensure they don't line up
    spanish_words = list(spanish_words)
    random.shuffle(spanish_words)
    
    matrix1 = []
    matrix2 = []

    for i in range(rows):
        row1 = english_words[i * cols: (i + 1) * cols]
        row2 = spanish_words[i * cols: (i + 1) * cols]
        matrix1.append(list(row1))
        matrix2.append(list(row2))
        
    return matrix1, matrix2


# Step 3: Display the English and Spanish word matrices side by side

def display_matrices(matrix1, matrix2):
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):

            # Print each word from both matrices in the same row
            word1 = matrix1[i][j] if j < len(matrix1[i]) else ""
            word2 = matrix2[i][j] if j < len(matrix2[i]) else ""
        
            # Align English words to the left with 20 spaces for readability
            print(f"{word1.ljust(20)} {word2}")
    print()  # Print a new line after each row


# Step 4: Define the match_words function to handle user input and check if the entered word pair is correct

def match_words(matrix1, matrix2, word_pairs):
    
    user_input = input("Enter a pair (English Spanish) or type 'quit' to exit or 'restart' to restart the game: ").strip()

    if user_input.lower() == 'quit':
        print("Game ended.")
        return None, None

    if user_input.lower() == 'restart':
        main()
        return None, None

    user_input = user_input.split()

    if len(user_input) != 2:
        print("Error: Please enter exactly two words.")
        return matrix1, matrix2
    
    english_word, spanish_word = user_input

    # Check if the pair matches any in the list of correct word pairs
    if (english_word, spanish_word) in word_pairs:
        print("Correct match!")
        incrementar()
        # Remove the matched words from the matrices
        matrix1, matrix2 = clear_matched_words(matrix1, matrix2, english_word, spanish_word)
        
        # Remove the matched pair from the word_pairs list
        word_pairs.remove((english_word, spanish_word))
    else:
        print("Incorrect match. Try again.")
        decrementar()
    return matrix1, matrix2


# Step 5: Define the clear_matched_words function to remove matched words from the matrices
def clear_matched_words(matrix1, matrix2, english_word, spanish_word):
      
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if matrix1[i][j] == english_word:
                matrix1[i][j] = ""  # Clear the matched English word
            if matrix2[i][j] == spanish_word:
                matrix2[i][j] = ""  # Clear the matched Spanish word

    return matrix1, matrix2
    
# Step 7: Define Score

# Declaración de una variable global de tipo entero
score = 0  # tipo int

def incrementar():
    global score  # Indicamos que usaremos la variable global
    score += 10
    print()
    print(f"Score up 10 points: {score}")

def decrementar():
    global score  # Indicamos que usaremos la variable global
    score -= 5
    print()
    print(f"Score down 5 points: {score}")

def mostrar():
    # Aquí no es necesario 'global' porque solo la leemos
    print(f"Your final Score is: {score}")


# Step 6: Define the main function to start and manage the word matching game
def main():
    
    # Define lists of English and Spanish words
    english_words = ['apple', 'strawberry', 'orange', 'grape', 'pear', 'peach']
    spanish_words = ['manzana', 'fresa', 'naranja', 'uva', 'pera', 'durazno']

    # Set the number of rows and columns for the matrices
    rows, cols = 3, 2

    # Generate randomized matrices from the word lists
    matrix1, matrix2 = generate_random_matrix(rows, cols, english_words, spanish_words)

    # Display the matrices side by side
    display_matrices(matrix1, matrix2)

    # Create a list of correct word pairs for checking matches
    word_pairs = list(zip(english_words, spanish_words))

     # Start the game loop
    while word_pairs:

        # Handle user input and update the matrices
        matrix1, matrix2 = match_words(matrix1, matrix2, word_pairs)

        if matrix1 is None:  # This happens if the user quits or restarts the game
            break

        # Display updated matrices
        display_matrices(matrix1, matrix2)
    
    # Congratulate the player
    if matrix1 is not None:  # Only if the game was not quit
        print("Congratulations! You've matched all the words!")
        mostrar()
# Start the game when launched
main()
