import curses
import time

def main(stdscr):
    curses.mousemask(True)
    while True:
        vstup = stdscr.getch()
        stdscr.addstr("\n" + str(vstup))
        if vstup == curses.KEY_MOUSE:
            coords = curses.getmouse()
            stdscr.addstr("\n" + str(coords))
        stdscr.refresh()
        time.sleep(0.01)
    
curses.wrapper(main)