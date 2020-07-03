import tkinter as tk
from countdown_timer import CountdownTimer
from time import time, sleep 

def main():
	root = tk.Tk()
	root.title("Paratimer")
	root.geometry("250x100")
	root.attributes('-topmost', True)
	root.configure(background="#000a12")

	countdownTimer = CountdownTimer()
	timeLabel, commandEntry = create_ui_widgets(root)

	setup_events(root, countdownTimer, timeLabel, commandEntry)

	root.mainloop()

def create_ui_widgets(root):
	timeLabel = tk.Label(root)
	timeLabel.config(font=("Courier", 32), background="#000a12", foreground="#ffffff")
	timeLabel["text"] = "0:00:00"
	timeLabel.pack(fill = tk.BOTH, expand = True)

	commandEntry = tk.Entry(root)
	commandEntry.config(font=("Arial Bold", 16), background="#4f5b62", foreground="#000a12")
	commandEntry.pack(fill = tk.X)

	return timeLabel, commandEntry

def setup_events(root, countdownTimer, timeLabel, commandEntry):
	isCountingDown = False
	isFocused = True

	def handle_command_entered(event):
		global isCountingDown
		global isFocused

		command = commandEntry.get().lower()
		commandLength = len(command)
		commandEntry.delete(0, 'end')
		if commandLength < 1:
			return
		if command == "stop":
			isCountingDown = False
		elif command == "start":
			isCountingDown = True
			root.after(1000, update_timer)
		elif command[0: 10] == "countdown " and commandLength > 10:
			print("something's happening")
			timeInput = command[10:].split(':')
			formatOfTime = len(timeInput)
			secondsToCountdownFrom = 0

			if formatOfTime == 1:
				secondsToCountdownFrom += int(timeInput[0])
			elif formatOfTime == 2:
				secondsToCountdownFrom += int(timeInput[1]) + int(timeInput[0]) * 60
			elif formatOfTime == 3:
				secondsToCountdownFrom += int(timeInput[2]) + int(timeInput[1]) * 60 + int(timeInput[0]) * 60 ** 2
			else:
				return

			countdownTimer.countdown_from(secondsToCountdownFrom)
			timeLabel["foreground"] = "#fAfffA"
			timeLabel["text"] = countdownTimer.get_time_stepped()
			isCountingDown = False
		elif command == "quit" or command == "exit":
			root.destroy()


		
	def update_timer():
		global isCountingDown

		if isCountingDown == False:
			timeLabel["text"] = countdownTimer.get_time_stepped()
			return

		countdownTimer.step()
		if countdownTimer.steppedBeyondZero:
			timeLabel["foreground"] = "#f44336"
		else:
			timeLabel["foreground"] = "#ffffff"
		timeLabel["text"] = countdownTimer.get_time_stepped()

		root.after(1000, update_timer)

	def on_focused(event):
		global isFocused
		isFocused = True
		root.overrideredirect(False)
		timeLabel.config(font=("Courier", 32))
		commandEntry.pack(fill = tk.X)
		
	def update_after_unfocused():
		global isFocused
		if isFocused == False:
			root.overrideredirect(True)
			commandEntry.pack_forget()
			timeLabel.config(font=("Courier", 44))

	def on_unfocused(event):
		global isFocused
		isFocused = False
		root.after(5000, update_after_unfocused)




	root.bind("<FocusIn>", on_focused)
	root.bind("<FocusOut>", on_unfocused)

	root.bind('<Return>', handle_command_entered)	

if __name__ == "__main__":
	main()