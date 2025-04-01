from pyautogui import click, locateOnScreen, moveTo, FAILSAFE, press, write, keyDown, keyUp
from time import sleep

# Safety
FAILSAFE = True  # Move mouse to corner to stop

def main():
    
    ### Parameters ###
    # Modify these for your preferences
    
    # True = minting, False = depositting
    is_minting = True
    
    # Rarity of the NFT to mint
    # [all, uncommon, grand, rare, arcane, mythic, legendary]
    rarity = "all"
    
    ###################################################
    
    rarity_mapping = {
        "all": 0,
        "uncommon": 2,
        "grand": 3,
        "rare": 4,
        "arcane": 5,
        "mythic": 6,
        "legendary": 7,
    }
    
    rarity_index = rarity_mapping[rarity]
    minting_url = f"https://ravenquest.io/en/myaccount/nft-inventory?assets=ravencard&rarity={rarity_index}&name="

    if is_minting:
        print("Starting ravenquest minting script...")
        print("--------------------------------------")
        
        retries = 0
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
                write(minting_url)
                sleep(0.1)
                press("enter")
                sleep(2.5)
            except Exception as e:
                if retries < 3:
                    retries += 1
                    keyDown("ctrl")
                    press("L")
                    keyUp("ctrl")
                    sleep(0.1)
                    press("backspace")
                    sleep(0.1)
                    write(minting_url)
                    sleep(0.1)
                    press("enter")
                    sleep(2.5)
                else:
                    break
    else:
        print("Starting ravenquest depositting script...")
        print("--------------------------------------")
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