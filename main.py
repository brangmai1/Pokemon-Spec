import random


class ActivePlayers:
    players = []

    def get_active_players(self):
        return len(self.players)

    # def check_pokemon_status(self, pokemon_index):
    #     print(f'Name: \t\t{self.players[pokemon_index]["name"]}')
    #     print(f'Type: \t\t{self.players[pokemon_index]["type"]}')
    #     print(f'Gender: \t{self.players[pokemon_index]["gender"]}')
    #     print(f'Ability: \t{self.players[pokemon_index]["ability"]}')
    #     print(f'Move: \t\t{self.players[pokemon_index]["move"]}')
    #     print(f'Health: \t{self.players[pokemon_index]["health"]}')


class Player:

    def __init__(self, name="", gender="None", nature="player", pokemon_list=0, bag=0, money=0.00):
        self.name = name
        self.gender = gender
        self.nature = nature
        self.pokemon_list = pokemon_list
        self.bag = bag
        self.money = money


class Pokemon:
    # Pokemons and their characteristic are taken
    # from the website: https://www.thetrueindians.com/animation/list-of-all-pokemon-characters/
    pokemon_bag = ([
        {"name": "Pikachu", "type": "Electric", "gender": "Male", "ability": "Static", "move": "Run", "health": 100},
        {"name": "Raichu", "type": "Electric", "gender": "Male", "ability": "Static", "move": "Fly", "health": 100},
        {"name": "Nidoran", "type": "Poison", "gender": "Female", "ability": "Poison", "move": "Run", "health": 100},
        {"name": "Jigglypuff", "type": "Fairy", "gender": "Female", "ability": "Competitive", "move": "Run",
         "health": 100},
        {"name": "Wigglytuff", "type": "Fairy", "gender": "Female", "ability": "Competitive", "move": "Jump",
         "health": 100},
        {"name": "Zubat", "type": "Poison", "gender": "Male", "ability": "Inner Focus", "move": "Fly", "health": 100},
        {"name": "Golbat", "type": "Poison", "gender": "Male", "ability": "Inner Focus", "move": "Fly", "health": 100},
        {"name": "Olddish", "type": "Poison", "gender": "Female", "ability": "Chlorophyll", "move": "Fly",
         "health": 100},
        {"name": "Venomoth", "type": "Bug", "gender": "Male", "ability": "Tinted Lens", "move": "Fly", "health": 100},
        {"name": "Psyduck", "type": "Water", "gender": "Male", "ability": "Damp", "move": "Swim", "health": 100},
        {"name": "Mankey", "type": "Fighting", "gender": "Male", "ability": "Vital Spirit", "move": "Fly",
         "health": 100},
        {"name": "Slowpoke", "type": "Water", "gender": "Male", "ability": "Own Tempo", "move": "Run", "health": 100},
        {"name": "Slowbro", "type": "Water", "gender": "Female", "ability": "Own Tempo", "move": "Run", "health": 100}])

    # def __init__(self, name, type_of_pokemon, gender, ability, moves, health):
    #     self.name = name
    #     self.type_of_pokemon = type_of_pokemon
    #     self.gender = gender
    #     self.nature = ability
    #     self.moves = moves
    #     self.health = health

    # def add_pokemon(self, name, type_of_pokemon, gender, ability, moves, health):
    #     new_pokemon = [name, type_of_pokemon, gender, ability, moves, health]
    #     self.pokemon_bag.append(new_pokemon)

    def display_pokemons(self):
        num = 1
        for pokemon in self.pokemon_bag:
            print(f'{num}. {pokemon["name"]}')
            num = num + 1

    def get_pokemon(self, pokemon_index):
        return self.pokemon_bag[pokemon_index]

    def total_pokemon(self):
        return len(self.pokemon_bag)

    def check_pokemon_status(self, pokemon_index):
        print(f'Name: \t\t{self.pokemon_bag[pokemon_index]["name"]}')
        print(f'Type: \t\t{self.pokemon_bag[pokemon_index]["type"]}')
        print(f'Gender: \t{self.pokemon_bag[pokemon_index]["gender"]}')
        print(f'Ability: \t{self.pokemon_bag[pokemon_index]["ability"]}')
        print(f'Move: \t\t{self.pokemon_bag[pokemon_index]["move"]}')
        print(f'Health: \t{self.pokemon_bag[pokemon_index]["health"]}')


class CpuTrainers:
    def __init__(self, name, pokemon_list, money, gifts, fun_facts):
        self.name = name
        self.pokemon_list = pokemon_list
        self.money = money
        self.gifts = gifts
        self.fun_facts = fun_facts


class GridTiles:
    grid_array = []

    def __init__(self):
        for row in range(10):
            self.grid_array.append([])
            for col in range(10):
                pokeball = random.randint(1, 20)
                if pokeball < 2:
                    self.grid_array[-1].append('B')
                else:
                    self.grid_array[-1].append('_')

    def set_player_position(self, x, y):
        self.grid_array[x][y] = "X"

    def update_position(self, x, y):
        if self.grid_array[x][y] == 'B':
            print("Great!! You found a Pokeball.")
        self.grid_array[x][y] = "_"

    def get_size(self):
        return self.grid_array[0]

    def battle_ground(self):
        for row in range(len(self.grid_array)):
            print("[", end="")
            for col in range(len(self.grid_array)):
                if col == len(self.grid_array) - 1:
                    print(self.grid_array[row][col], end="")
                else:
                    print(self.grid_array[row][col], end=", ")
            print("]")


def game_initialization():
    first_player = input("Enter your ID: ")
    player_one = Player(first_player)
    active_players = ActivePlayers()
    active_players.players.append(player_one)

    second_player = str(random.randint(1, 90))
    player_two = Player(second_player)
    active_players.players.append(player_two)
    print("\nWelcome to Pokemon world!!\n")
    print(f'You are: player {player_one.name}')
    print(f'Your opponent is: player {player_two.name}')
    print("\nChoose your pokemon to start off your Pokemon world adventure.")


def pokemon_list():
    pokemon = Pokemon()
    pokemon.display_pokemons()


def battle(player1, player2):
    print(f"Player one: {player1}")
    print(f"Player two: {player2}")


def game_on(row, col, grid):
    grid.set_player_position(row, col)
    grid.battle_ground()

def ask_direction(condition):
    if not condition:
        print("\nWhich way do you want to go?")
    else:
        print("The chosen path is blocked. Choose a different direction.")
    print("L/R/U/D for left/right/up/down or 'e' to exit.")
    # print("'l' for left\t'r' for right\n'u' for up\t\t'd' for down")
    # print("'e' for exit")
    chosen_direction = input("Enter your choice: ")
    return chosen_direction.lower()


game_initialization()

repeat_game = True

#while repeat_game:
pokemon_list()

my_pokemon = Pokemon()
your_pokemon_index = (int(input("Enter your choice of pokemon number: ")) - 1)
print(your_pokemon_index)
my_current_pokemon = my_pokemon.get_pokemon(your_pokemon_index)
print(f"\nStatus of your pokemon")
print('************************\n')
my_pokemon.check_pokemon_status(your_pokemon_index)

opponent_pokemon = Pokemon()
opponent_pokemon_index = random.randint(0, opponent_pokemon.total_pokemon())
print(opponent_pokemon_index)
opponent_current_pokemon = opponent_pokemon.get_pokemon(opponent_pokemon_index)
print(f"\nStatus of your opponant's pokemon")
print('**************************************\n')
opponent_pokemon.check_pokemon_status(opponent_pokemon_index)

boot_on_the_ground = ActivePlayers()
# print(f"Active players: {boot_on_the_ground.get_active_players()}")
# player_one = boot_on_the_ground.players[0]["name"]
# player_two = boot_on_the_ground.players[1]["name"]
# battle(player_one, player_two)

# battle_ground = GridTiles()
# battle_ground.show_battle_ground()

row = 2
col = 2
player_position = [row, col]
my_grid = GridTiles()
game_on(player_position[0], player_position[1], my_grid)

road_blocked = False
while True:
    direction = ask_direction(road_blocked)
    road_blocked = False

    if direction == 'l':
        if col - 1 < 0:
            road_blocked = True
        else:
            my_grid.update_position(row, col)
            col -= 1
            game_on(row, col, my_grid)

    elif direction == 'r':
        if (col + 1) > 9:
            road_blocked = True
        else:
            my_grid.update_position(row, col)
            col += 1
            game_on(row, col, my_grid)

    elif direction == 'u':
        if (row - 1) < 0:
            road_blocked = True
        else:
            my_grid.update_position(row, col)
            row -= 1
            game_on(row, col, my_grid)

    elif direction == 'd':
        if (row + 1) > 9:
            road_blocked = True
        else:
            my_grid.update_position(row, col)
            row += 1
            game_on(row, col, my_grid)

    elif direction == 'e':
        print("Good bye.")
        break

print("\n\n")


