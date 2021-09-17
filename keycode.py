import curses

# Main Function
def main(stdscr):

	while True:
		key = stdscr.getch()
		stdscr.erase()
		stdscr.refresh()
		stdscr.addstr(0, 0, "Key Code > " + str(key) + " | Key > " + chr(key))

# Curses Wrapper
curses.wrapper(main)
