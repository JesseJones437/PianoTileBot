import pyautogui
import PIL
from PIL import Image
import time
import pynput
from pynput import keyboard

Play = True
listOfTilePos = []

def playFalse(key):
    if key == keyboard.Key.esc:
        global Play
        Play = False
        #print(Play)
        #stop listener
        return False  
    
def getMouseLoc(key):
    if key == keyboard.Key.shift:
        global listOfTilePos
        listOfTilePos.append(pyautogui.position())
        #print(listOfTilePos)


#works for piano tile games with solid color keys
if __name__ == '__main__':
    #print(pyautogui.size())

    #sets up number of tiles and their positions
    completedSetUp = False
    print('How many tiles are there in each row?')
    numTiles = int(input())
    print('Press left ''shift'' over each tile in the row, left to right')
    listenerMousePos = keyboard.Listener(on_press = getMouseLoc)
    listenerMousePos.start()
    while not completedSetUp:
        if len(listOfTilePos) == numTiles:
            completedSetUp = True
    listenerMousePos.stop()
    time.sleep(1)

    #will find out what tile it needs to press instead of being told initial tile like in commented code below
    counter = 0
    baseCase = pyautogui.screenshot(region=(listOfTilePos[0][0],listOfTilePos[0][1],1,1))
    baseCaseRGB = baseCase.convert('RGB')
    baseColorTile = baseCaseRGB.getpixel((0,0))
    for y in range(1, numTiles):
        colorCompareTo = pyautogui.screenshot(region=(listOfTilePos[y][0],listOfTilePos[y][1],1,1))
        colorCompareToRGB = colorCompareTo.convert('RGB')
        colorOfTile = colorCompareToRGB.getpixel((0,0))
        if baseColorTile == colorOfTile:
            counter = counter + 1
        else:
            playTile = colorOfTile
    if counter == 0:
        playTile = baseColorTile
        
    """
    #sets up the color to click
    print('Which of the first tiles is the color that should be clicked?')
    #list index starts at 0, subtracting 1 lets player start counting at 1 instead of 0 
    tileToGetColor = int(input()) - 1
    colorPic = pyautogui.screenshot(region=(listOfTilePos[tileToGetColor][0],listOfTilePos[tileToGetColor][1],1,1))
    playValueRGB = colorPic.convert('RGB')
    playTile = playValueRGB.getpixel((0,0))
    #print(playTile)
    """
    
    print('Press the ''esc'' key to exit')
    listenerExit = keyboard.Listener(on_press = playFalse)
    #start to listen on a separate thread
    listenerExit.start()
    
    print('starts in 3')
    time.sleep(3)
    print('starting')
    while Play:
        for x in range(0, numTiles):
            #takes screenshot at given tile positions to test if it is the tile to click on
            rowImage = pyautogui.screenshot(region=(listOfTilePos[x][0],listOfTilePos[x][1],1,1))
            rgbImage = rowImage.convert('RGB')
            #rowImage.show()
            #print(Play)
            #time.sleep(2)
                
            RGB = rgbImage.getpixel((0,0))
                
            if RGB == playTile:
                pyautogui.click(listOfTilePos[x][0], listOfTilePos[x][1])
                
    print('done')


                            






