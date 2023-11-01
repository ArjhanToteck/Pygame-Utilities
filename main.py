from GameManager import GameManager
from StoreView import StoreView

def main():
	# open first scene
	StoreView.start()

	# set game up
	GameManager.setUpGame()

if __name__ == '__main__':
	main()