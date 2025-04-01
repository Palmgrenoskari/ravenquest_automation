from pyautogui import click, locateOnScreen, moveTo, FAILSAFE, press, write
from time import sleep

# Safety
FAILSAFE = True  # Move mouse to corner to stop

def main():
    
    # True = minting, False = depositting
    is_minting = True
    if is_minting:
        print("Starting ravenquest minting script...")
        print("--------------------------------------")
    else:
        print("Starting ravenquest depositting script...")
        print("--------------------------------------")
    
    if is_minting:
        while True:
            try:
                menu = locateOnScreen("images/menu.png", confidence=0.95)
                moveTo(menu)
                click()
                sleep(0.5)
                
                mint = locateOnScreen("images/mint_to_blockchain.png", confidence=0.9)
                moveTo(mint)
                click()
                sleep(1.2)
                
                confirm = locateOnScreen("images/confirm.png", confidence=0.98)
                moveTo(confirm)
                click()
                sleep(0.3)
                
                confirm_final = locateOnScreen("images/confirm_final.png", confidence=0.98)
                moveTo(confirm_final)
                click()
                sleep(0.7)
                
                search = locateOnScreen("images/search.png", confidence=0.95)
                moveTo(search)
                click()
                sleep(0.1)
                press("backspace")
                sleep(0.1)
                write("https://ravenquest.io/en/myaccount/nft-inventory?assets=ravencard&rarity=2&name=")
                sleep(0.1)
                press("enter")
                sleep(2.5)
            except Exception as e:
                print(e)
                break
    else:
        while True:
            try:
                location = locateOnScreen("images/deposit.png", confidence=0.97)
                moveTo(location)
                click()
                sleep(10)
                
                approve = locateOnScreen("images/approve.png", confidence=0.97)
                moveTo(approve)
                click()
                sleep(15)
                click()
                sleep(10)
                
            except Exception as e:
                print(e)
                break

if __name__ == "__main__":
    main() 