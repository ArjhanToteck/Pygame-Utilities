from GameManager import GameManager
from GameObject import GameObject

def main():
    # set game up
    GameManager.setUpGame()

    test = GameObject(imagePath="test.png")
    print(test.image)

if __name__ == '__main__':
    main()