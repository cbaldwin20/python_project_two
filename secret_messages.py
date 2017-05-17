from play import Play 

def cls():
    """adds two line spaces"""
    print("")
    print("")
         
while True:
    start = Play()
    cls()
    print("'{}'' is now...".format(start.sentence))
    cls()
    #prints the final output
    print(start)
    cls()
    to_continue = input("Do you want to do another sentence? Enter"
                        " 'yes' or 'no': ")
    to_continue = to_continue.strip()
    if to_continue.upper() in ["NO", "QUIT", "EXIT", "N", "Q"]:
        cls()
        print("Goodbye.")
        break
    else:
        continue
