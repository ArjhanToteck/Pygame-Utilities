from GameManager import GameManager
from GameObject import GameObject
from Vector2 import Vector2

def main():
    # set game up
    GameManager.setUpGame()

    test = GameObject(imagePath = "test.png", size = Vector2(5, 5))
    print(test.image)

if __name__ == '__main__':
    main()