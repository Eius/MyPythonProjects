import winsound
from termcolor import colored
import colorama
from time import sleep

colorama.init()


def _play_sound():
    winsound.PlaySound('bell_notification.wav', winsound.SND_FILENAME)


class Timer:

    def __init__(self):
        self.is_configured = False
        self._current_event = "work"
        self._default_times = {"work": 0, "break": 0}
        self._time_left = {"work": 0, "break": 0}

    def _switch_event(self):
        """Switches current event when timer runs out"""
        self._time_left[self._current_event] = self._default_times[self._current_event]

        if self._current_event == "work":
            self._current_event = "break"
            print("\r                               ", end='\033[K')
            print(colored("\rBreak time!", "light_green"), end='\033[K')

        elif self._current_event == "break":
            self._current_event = "work"
            print("\r                               ", end='\033[K')
            print(colored("\rBack to work!", "light_green"), end='\033[K')

        _play_sound()

    def _print_time_left(self):
        """Prints formatted time left (mm:ss)"""
        formatted_minutes = colored(str(int(self.get_minutes_left())).zfill(2), "light_red")
        formatted_seconds = colored(str(int(self.get_seconds_left())).zfill(2), "light_red")
        current_event = self.get_current_event().capitalize()
        print("\r                               ", end='\033[K')
        print(colored(f"\r{current_event} time left: ", "light_green")
              + f"{formatted_minutes}:{formatted_seconds}", end='\033[K')

    def set_times(self):
        """Sets the length of work and breaks"""
        for time in self._default_times:
            user_input = float(input(f"Set {time} minutes: "))
            self._default_times[time] = 60 * user_input
            self._time_left[time] = max(1, int(self._default_times[time]))

    def tick(self):
        """Advances the timer by one second"""
        self._print_time_left()
        self._time_left[self._current_event] -= 1

        # Check if timer reached 0
        if self._time_left[self._current_event] < 0:
            self._switch_event()
        sleep(1)

    def get_minutes_left(self):
        """Returns minutes without seconds (2 minutes : 47 seconds returns 2)"""
        minutes_left = self._time_left[self._current_event] // 60
        return minutes_left

    def get_seconds_left(self):
        """Returns seconds without minutes (2 minutes : 47 seconds returns 47)"""
        seconds_left = self._time_left[self._current_event] % 60
        return seconds_left

    def get_current_event(self):
        """Returns current event (break/work)"""
        return self._current_event

    def get_default_times(self):
        """Returns default values of work and break times set by user"""
        return self._default_times
