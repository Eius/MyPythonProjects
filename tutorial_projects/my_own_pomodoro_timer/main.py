from timer import Timer
from termcolor import colored
import colorama

timer = Timer()
colorama.init()
is_configured = False

print(colored("Welcome to RajčinaTimer™ v0.2!\n"
              "Please set your preferred work and break times to begin.", "light_green"))

while True:
    try:

        if not timer.is_configured:
            timer.set_times()
            timer.is_configured = True
            continue

        else:
            timer.tick()
            continue

    except ValueError:
        is_configured = False
        print(colored("You tried to break my program. Nice try, but no.", "light_red"))
        continue

    except KeyboardInterrupt or EOFError:
        print(colored("\nExiting program...", "light_red"))
        break
