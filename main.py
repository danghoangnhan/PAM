from component.button import ButtonElement
from component.screen import StartScreen
from psychopy import visual, core, event


# Create a window
win = visual.Window([800, 600], color="white")

# Create and initialize the first screen
current_screen = StartScreen(win)

while current_screen is not None:
    current_screen.draw()
    win.flip()
    response = event.waitKeys()
    
    if response and current_screen.elements:
        for element in current_screen.elements:
            if isinstance(element, ButtonElement) and 'space' in response:
                if element.action:
                    current_screen = element.action()

# Cleanup
win.close()
core.quit()





