from pyautogui import click, locateOnScreen, moveTo, FAILSAFE, press, write
from time import sleep

# Safety
FAILSAFE = True  # Move mouse to corner to stop

def main():
    # Example usage
    print("Starting ravenquest minting script...")
    print("--------------------------------------")
    
    # Unnecessary steps, as we can just use the URL
    
    # # Navigate to the minting page
    # collection = locateOnScreen("images/collection.png", confidence=0.95)
    # moveTo(collection)  # Move to the top-left corner of the screen
    # click()
    # sleep(1.5)
    
    # dropdown = locateOnScreen("images/dropdown.png", confidence=0.95)
    # moveTo(dropdown)
    # click()
    # sleep(0.5)
    
    # cards = locateOnScreen("images/cards.png", confidence=0.95)
    # moveTo(cards)
    # click()
    # sleep(1)
    while True:
        try:
            menu = locateOnScreen("images/menu.png", confidence=0.95)
            moveTo(menu)
            click()
            sleep(0.5)
            
            mint = locateOnScreen("images/mint_to_blockchain.png", confidence=0.95)
            moveTo(mint)
            click()
            sleep(1)
            
            confirm = locateOnScreen("images/confirm.png", confidence=0.99)
            moveTo(confirm)
            click()
            sleep(0.2)
            
            confirm_final = locateOnScreen("images/confirm_final.png", confidence=0.99)
            moveTo(confirm_final)
            click()
            sleep(0.5)
            
            search = locateOnScreen("images/search.png", confidence=0.95)
            moveTo(search)
            click()
            sleep(0.1)
            press("backspace")
            sleep(0.1)
            write("https://ravenquest.io/en/myaccount/nft-inventory?assets=ravencard&size=0")
            sleep(0.1)
            press("enter")
            sleep(2)
        except Exception as e:
            print(e)
            break             

if __name__ == "__main__":
    main() 