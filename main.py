from GameManager import GameManager
from StoreView import StoreView

def main():
	# open first scene
	StoreView.start()

	# set game up
	GameManager.setUpGame()

	# game loop
	while GameManager.running == True:
		GameManager.nextFrame()

if __name__ == '__main__':
	main()