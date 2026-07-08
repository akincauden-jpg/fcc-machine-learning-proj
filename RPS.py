
"""Hint: To defeat all four opponents, your program may need to have 
multiple strategies that change depending on the plays 
of the opponent."""

# no rnn, just simple pattern recognition + prediction

# find all times the last 5-move pattern appears,
# if none, try 4-move pattern, then 3-move pattern, then 2-move pattern
# count what came after the pattern

def player(prev_play, opponent_history=[]):
   
    if prev_play == '':
        opponent_history.clear() #new player, clear history
        return "R"  # default first move

    opponent_history.append(prev_play) # after first turn

    
    counter = {'R': 'P', 'P': 'S', 'S': 'R'} # what beats what
    guess = "R"
    history_string = "".join(opponent_history)

    for pattern_len in [5, 4, 3, 2]:
        if len(history_string) <= pattern_len:
            continue

        recent_pattern = history_string[-pattern_len:]
        possible_next_moves = []

        for i in range(len(history_string) - pattern_len): # the num of total without pattern
            past_pattern = history_string[i:i + pattern_len]

            if past_pattern == recent_pattern:
                next_move = history_string[i + pattern_len]
                possible_next_moves.append(next_move)

        if possible_next_moves:
            counts = {'R': possible_next_moves.count('R'), 
                      'P': possible_next_moves.count('P'), 
                      'S': possible_next_moves.count('S')
                      }
            
            prediction = max(counts, key=counts.get)
            guess = counter[prediction]
            break # IMPORTANT: break after finding the first pattern match

    return guess


   

