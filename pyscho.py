from psychopy import visual, core, event

# Create a window
win = visual.Window([800, 600], color="white")

# Define text stimuli for each screen
test_name_text = visual.TextStim(win, text="Test Name", pos=(0, 0))
audio_list_text = visual.TextStim(win, text="Audio List", pos=(0, 0))
thanks_text = visual.TextStim(win, text="Thank you for participating!", pos=(0, 0))

# Create buttons
start_button = visual.Rect(win, width=0.2, height=0.1, fillColor="green", pos=(0, -0.2))
next_button = visual.Rect(win, width=0.2, height=0.1, fillColor="blue", pos=(0.4, -0.4))
prev_button = visual.Rect(win, width=0.2, height=0.1, fillColor="blue", pos=(-0.4, -0.4))
action_button = visual.Rect(win, width=0.2, height=0.1, fillColor="blue", pos=(0, -0.4))

# Create audio stimuli
audio_files = ["audio1.wav", "audio2.wav", "audio3.wav", "audio4.wav", "audio5.wav"]
audio_stimuli = [visual.SoundStim(win, sound=file) for file in audio_files]

# Create answer buttons
answer_buttons = []
for i in range(5):
    x_pos = (i - 2) * 0.2  # Adjust positions for 5 buttons
    answer_button = visual.Rect(win, width=0.2, height=0.1, fillColor="red", pos=(x_pos, 0.2))
    answer_buttons.append(answer_button)

# Define experiment flow
screens = [test_name_text, audio_list_text, thanks_text]
buttons = [start_button, next_button, prev_button, action_button] + answer_buttons
current_screen = 0

while current_screen < len(screens):
    for button in buttons:
        button.draw()
    screens[current_screen].draw()
    win.flip()
    response = event.waitKeys()

    if screens[current_screen] == test_name_text and 'space' in response:
        current_screen += 1
        continue
    if screens[current_screen] == audio_list_text:
        if 'space' in response:
            audio_stimuli[current_audio].play()
        elif '1' in response:
            # Handle answer 1
        elif '2' in response:
            # Handle answer 2
        elif '3' in response:
            # Handle answer 3
        elif '4' in response:
            # Handle answer 4
        elif '5' in response:
            # Handle answer 5
        elif 'right' in response:  # Move to next question
            current_audio += 1
        elif 'left' in response:  # Return to previous question
            current_audio -= 1
        elif 'space' in response:  # Action button
            current_screen += 1

# Cleanup
win.close()
core.quit()
