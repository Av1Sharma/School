"""
A simple application displaying a message that can be hidden with a key press.

The purpose of this lab is to familiarize you with the basics of the game2d package.
This will help you get started on the last assignment.

<YOUR NAME HERE>
<DATE HERE>
"""
from game2d import *

#### CONSTANTS ####

# The initial width of the game display
GAME_WIDTH  = 840
# The initial height of the game display
GAME_HEIGHT = 630

class LabApp(GameApp):
    """
    The application class for this lab.
    
    Displays a Hello World message.

    Press any key to hide or show the message.
    """
    # HIDDEN ATTRIBUTES
    # Attribute _message: The message to display on the screen
    # Invariant: _message is a GLabel or None
    #
    # Attribute _visible: Whether the message is visible
    # Invariant: _visible is a bool
    
    def start(self):
        """
        Initializes the application.
        
        This method is distinct from the built-in initializer __init__ (which 
        you should not override or change). This method is called once the 
        game is running.
        """
        self._message = GLabel(text='Hello World!', font_name='CuteFrog.ttf',
                               font_size=64, x=self.width/2, y=self.height/2)
        self._visible = True
    
    def update(self,dt):
        """
        Updates the game objects each frame.
        
        Toggles the message visibility whenever any key is pressed.
        """
        if self.input.is_key_pressed(''):
            self._visible = not self._visible
    
    def draw(self):
        """
        Draws the game objects to the view.
        
        Every single thing you want to draw in this game is a GObject. To draw a 
        GObject g, simply use the method g.draw(self.view). It is that easy!
        """
        if self._visible:
            self._message.draw(self.view)


# Application code
if __name__ == '__main__':
    # Create and run the lab application
    LabApp(width=GAME_WIDTH,height=GAME_HEIGHT).run()
