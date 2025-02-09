import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fireworks():
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
    height = 20
    width = 80
    bomb_height = height

    # Bomb going up
    while bomb_height >= 0:
        clear_screen()
        for i in range(height):
            if i == bomb_height:
                print(' ' * 20 + '⊹')
                print(' ' * 20 + '|')
                print(' ' * 30 + '        ⊹')
                print(' ' * 30 + '       /')
                print(' ' * 25 + ' ⊹')
                print(' ' * 25 + '  \ ')
            else:
                print()
        bomb_height -= 1
        time.sleep(0.1)

    # Explosion
    explosion_text = """
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡆⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀
⠀⠀⠀   ⠠⢤⣦⠤⠀⠀⠉⢏⠀⠠⣤⣦⠄⠀⡸⠁⠀⠀⠀⣠⠹⠛⠏⠀⠀⠀⠀
   ⠀⣠⠀⠀⠉⠈⠐⢄⠀⠀⠈⢆⠀⠉⡏⠀⠰⠁⠀⠀⠠⠊⠀⠀⠠⢤⣦⡤⠀⠀
   ⠘⠛⠋⠒⠂⠤⢀⠀⠁⠀⣀⠀⠀⠀⠣⢤⣦⡤⠀⠁⠀⡀⠤⠒⠉⠈⠈⠁⠀         ⢀
   ⠀⠀⢠⣶⡄⠀⣀⣀⠀⠙⠛⢋⡀⠀⠀⡸⠉⠁⠀⠀⣁⡀⠠⠤⠄⠾⠷⠂⠀    ⢀⢀⠄⠌⡓⡄⠑⡄⡀⠀⠠⠄
   ⣀⣤⣀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠀⠀⠀⠁⢤⣶⡄⠀⠀⣀⣀⡀⣀⣠⣀ ⠄⣀⢤⠤⠕⡪⠀⠠⢊⠁⢀⠀⠢⠈⠁
   ⠘⠉⠁⠀⠀⠀⢀⡠⠄⠂⠀⡠⠀⠀⠀⠐⢄⠀⠀⠂⠠⠄⣀⠀⠀⠀⠀⠘⠛⠃ ⢨⠔⢁⠠⠤⠀⢐⡢⠉⠉⠑⢮⡢⡀
                                 ⠈⠒⠁⡴⡡⠀⢀⠔⠀⠀⠉⢂⢢⠀⠡⠈⢀⠀⠀⠀
   ⠀⠀⠀⣶⣶⠉⠁⠀⢀⣄⠞⠀⠀⠀⡄⠀⠀⠑⠄⡀⠀⠀⠀⠉⢳⣾⡖⠀⠀   ⡔⢡⠁⠀⢸⠀⠆⠀⠂⢸⡀⡇
⠀⠀⠀   ⠀⠀⠀⠀⠀⠙⠛⠃⠀⠠⣴⣦⠄⠀⠈⠝⠛⠅⠀⠀⠀⠀⠀⠀⠀⠀ ⠠ ⠀⠀⠀⢰⠀⠆⠀⠀⠀⠸⠁
⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠁⠈   ⢀          ⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⢀⢀⠄⠌⡓⡄⠑⡄⡀⠀⠠⠄⠀⠀   
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⣀⢤⠤⠕⡪⠀⠠⢊⠁⢀⠀⠢⠈⠁⠀
⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠔⢁⠠⠤⠀⢐⡢⠉⠉⠑⢮⡢⡀⠀⠀  
⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠈⠒⠁⡴⡡⠀⢀⠔⠀⠀⠉⢂⢢⠀⠡⠈⢀⠀⠀    
⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⡔⢡⠁⠀⢸⠀⠆⠀⠂⢸⡀⡇⠀⠀⠀⠀⠀
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⢰⠀⠆⠀⠀⠀⠸⠁⠀⠀⠀
⠀            ⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡄⠀
"""

    for _ in range(50):
        clear_screen()
        colored_text = ""
        for char in explosion_text:
            if char != "\n":
                colored_text += random.choice(colors) + char + '\033[0m'
            else:
                colored_text += char
        print(colored_text)
        time.sleep(0.1)

def main():
    print("Fireworks Explosion!")
    fireworks()

if __name__ == "__main__":
    main()
