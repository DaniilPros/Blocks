from Controler import *


root = Tk(className="Blocks")
root['bg'] = 'orange'
root['cursor'] = 'hand2'
root.wm_attributes('-fullscreen', True)
root.update_idletasks()
game = Game(root, 10)
game.start()

root.mainloop()
