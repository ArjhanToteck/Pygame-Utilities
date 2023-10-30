from GameManager import GameManager
from Scene1 import Scene1

def main():
	# open first scene
	Scene1.start()

	# set game up
	GameManager.setUpGame()

if __name__ == '__main__':
	main()