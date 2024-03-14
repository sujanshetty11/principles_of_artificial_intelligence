import math

def calculate_probability_of_winning():
    # Get the material advantage for each player
    white_material_advantage = get_material_advantage('white')
    black_material_advantage = get_material_advantage('black')

    # Calculate the probability of white winning
    probability_white_wins = 1 / (1 + math.exp(black_material_advantage - white_material_advantage))

    # Calculate the probability of black winning
    probability_black_wins = 1 - probability_white_wins

    # Convert probabilities to percentages
    probability_white_wins *= 100
    probability_black_wins *= 100

    return probability_white_wins, probability_black_wins

def get_material_advantage(player):
    # Get the material value for each piece
    piece_values = {
        'pawn': 1,
        'knight': 3,
        'bishop': 3,
        'rook': 5,
        'queen': 9,
        'king': 0  # The king's value is not considered in this calculation
    }

    # Get the pieces for the specified player
    pieces = get_pieces(player)

    # Calculate the total material value for the player
    material_advantage = 0
    for piece in pieces:
        material_advantage += piece_values[piece]

    return material_advantage


def get_pieces(player):
    # In a real chess game, you would get the pieces from the current position
    # For simplicity, we'll just use a hardcoded example here
    if player == 'white':
        return ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'rook', 'knight', 'bishop',
                'queen', 'king']
    elif player == 'black':
        return ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'rook', 'knight', 'bishop',
                'king']
    else:
        raise ValueError("Invalid player")





# Calculate the probability of winning for each player
probability_white_wins, probability_black_wins = calculate_probability_of_winning()

# Print the results
print(f"Probability of white winning: {probability_white_wins:.2f}%")
print(f"Probability of black winning: {probability_black_wins:.2f}%")
