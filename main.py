from StoreView import StoreView

from Engine import *

def main():
	# set game up
	GameManager.setUpGame(Vector2(50, 50), Vector2(1280, 720))
	
	# open first scene
	StoreView.start()

	# game loop
	while GameManager.running == True:
		GameManager.nextFrame()

if __name__ == '__main__':
	main()