def calculate_probability(board):
    # Assign scores to each piece
    piece_values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 100}

    white_score = 5 
    black_score = 0

    # Iterate through the board and calculate scores
    for row in board:
        for piece in row:
            if piece.isupper():  # White piece
                white_score += piece_values.get(piece, 0)
            elif piece.islower():  # Black piece
                black_score += piece_values.get(piece.upper(), 0)

    total_score = white_score + black_score

    # Calculate probabilities based on scores
    white_probability = white_score / total_score if total_score != 0 else 0
    black_probability = black_score / total_score if total_score != 0 else 0

    return white_probability, black_probability

# Example usage
chess_board = [
    "rnbqkbnr",
    "pppppppp",
    "........",
    "........",
    "........",
    "........",
    "PPPPPPPP",
    "RNBQKBNR"
]

white_prob, black_prob = calculate_probability(chess_board)

print(f"White Probability: {white_prob:.2%}")
print(f"Black Probability: {black_prob:.2%}")
