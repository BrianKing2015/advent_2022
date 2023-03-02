# day 2 rock, paper, scissors

def read_file(input_file):
    rounds = []
    with open(input_file, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip("\n")
            enemy_move = line.split(" ")[0]
            my_move = line.split(" ")[1]
            rounds.append(second_outcome_per_round(enemy_move, my_move))

        return sum(rounds)


def win_lose_draw_per_round(enemy_move, my_move):
    inputs = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    points_per_shape = {'rock': 1, 'paper': 2, 'scissors': 3}
    points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}
    enemy_move = inputs[enemy_move]
    my_move = inputs[my_move]
    
    if enemy_move == my_move:
        return points_per_outcome['Draw'] + points_per_shape[my_move]
    elif enemy_move == "rock" and my_move == "scissors":
        return points_per_outcome['Lose'] + points_per_shape[my_move]
    elif enemy_move == "rock" and my_move == "paper":
        return points_per_outcome['Win'] + points_per_shape[my_move]
    elif enemy_move == "paper" and my_move == "rock":
        return points_per_outcome['Lose'] + points_per_shape[my_move]
    elif enemy_move == "paper" and my_move == "scissors":
        return points_per_outcome['Win'] + points_per_shape[my_move]
    elif enemy_move == "scissors" and my_move == "paper":
        return points_per_outcome['Lose'] + points_per_shape[my_move]
    elif enemy_move == "scissors" and my_move == "rock":
        return points_per_outcome['Win'] + points_per_shape[my_move]
    else:
        raise ValueError("Invalid input")
    

def second_outcome_per_round(enemy_move, my_move):
    inputs = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    points_per_shape = {'rock': 1, 'paper': 2, 'scissors': 3}
    points_per_outcome = {'lose': 0, 'draw': 3, 'win': 6}
    enemy_move = inputs[enemy_move]
    my_move = inputs[my_move]
    
    if (enemy_move, my_move) in [("rock", "draw"), ("paper", "lose"), ("scissors", "win")]:
        return points_per_outcome[my_move] + points_per_shape["rock"]
    elif (enemy_move, my_move) in [("rock", "win"), ("paper", "draw"), ("scissors", "lose")]:
        return points_per_outcome[my_move] + points_per_shape["paper"]
    else:
        return points_per_outcome[my_move] + points_per_shape["scissors"]

if __name__ == "__main__":
    input_file = "real_input.txt"
    print(read_file(input_file))
