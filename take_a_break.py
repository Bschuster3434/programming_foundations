import webbrowser
import time

total_breaks = 3
minutes_to_break = 120

for i in range(total_breaks):
	time.sleep(60 * minutes_to_break)
	webbrowser.open("https://www.youtube.com/watch?v=JMJ6KfB_GLc")