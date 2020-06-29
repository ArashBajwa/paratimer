from countdown_timer import CountdownTimer

def main():
	timer = CountdownTimer()
	timer.startAt(1)
	print(timer.getTimeStepped())
	timer.step()
	print(timer.getTimeStepped())
	timer.step()
	print(timer.getTimeStepped())
	timer.step()

if __name__ == "__main__":
	main()