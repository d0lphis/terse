#!/usr/bin/python
# coding=utf-8

# https://github.com/andrewissac/pyProgressbar

import sys
import colorsys as c
from collections import deque



class BackgroundColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def rgb_to_bash(r,g,b):
    return '\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'
def hls_to_bash(h,l,s):
    r,g,b = tuple(int(x * 255) for x in c.hls_to_rgb(h, l, s))
    return rgb_to_bash(r,g,b)
class Progressbar():
    def __init__(
        self, _total_count, _segments = 60, _bold = False, _rainbow_wave_enabled = True, 
        _animate_left_to_right = True, _animation_speed = 5, _rainbow_color_change_speed = 2.0, 
        _rainbow_color_increment = 25, _luminosity = 0.65, _saturation = 1.0):
        self._total_count = _total_count
        # _segments % len(_display_pattern) should be 0 to get a perfect loop
        self._segments = _segments
        self._bold = _bold
        self._rainbow_wave_enabled = _rainbow_wave_enabled
        self._rainbow_color_increment = _rainbow_color_increment
        self._animation_speed = 5 # every 5 steps -> cyclic rotate displaypattern, may vary on each case!
        self._animate_left_to_right = _animate_left_to_right
        self._rainbow_color_change_speed = _rainbow_color_change_speed
        self._luminosity = _luminosity
        self._saturation = _saturation
        self._patterns = { 
            "wave" : ',.~*^`^*~.', 
            "table_flip" : '(ノಠ 益ಠ)ノ彡┻━┻........', 
            "rectangle" : '▮'
        }
        self._display_pattern = self.__generate_chars_deque(self._patterns["wave"])

    def add_new_display_pattern(self, pattern_name, pattern_string):
        self._patterns[pattern_name] = pattern_string
    
    def set_display_pattern(self, display_pattern):
        if (display_pattern not in self._patterns.keys()):
            self.add_new_display_pattern(display_pattern, display_pattern)
        self._display_pattern = self.__generate_chars_deque(self._patterns[display_pattern])
    
    def add_and_set_new_display_pattern(self, pattern_name, pattern_string):
        self.add_new_display_pattern(pattern_name, pattern_string)
        self.set_display_pattern(pattern_name)

    def show_progress(self, count=0, message= ''):
        if(count % self._animation_speed == 0): # simple mechanism to only rotate chars every n loop steps (may vary in your case)
            if(self._animate_left_to_right):
                self._display_pattern.rotate(-1) # cyclic rotation of _display_pattern
            else:
                self._display_pattern.rotate(1) # cyclic rotation of _display_pattern
        _filled_progress_bar_segments = int(round(self._segments * count / float(self._total_count)))

        # using HLS colorspace
        h = 0.0 
        if (count / float(self._total_count)) * self._rainbow_color_change_speed < 1.0:
            h = (count / float(self._total_count)) * self._rainbow_color_change_speed
        else:
            h = (count / float(self._total_count)) * self._rainbow_color_change_speed - 1.0 # make it repeat (remember hue interval: 0..1)
        l = self._luminosity # should be between 0 and 1
        s = self._saturation # should be between 0 and 1

        percentage = round(100.0 * count / float(self._total_count-2), 1)
        bar = hls_to_bash(h,l,s)
        if self._bold:
            bar += BackgroundColors.BOLD
        if self._rainbow_wave_enabled:
            h_increment = (self._rainbow_color_increment / float(self._total_count)) * self._rainbow_color_change_speed
            for i in range(_filled_progress_bar_segments):
                bar += self._display_pattern[i] + hls_to_bash(h,l,s)
                h += h_increment
        else:
            for i in range(_filled_progress_bar_segments):
                bar += self._display_pattern[i]
        bar += BackgroundColors.ENDC
        bar += '-' * (self._segments - _filled_progress_bar_segments)

        if(count >= self._total_count-1):
            sys.stdout.write('\n')
            sys.stdout.flush()
            return
        sys.stdout.write('[{0}] {1}% ...{2}\r'.format(bar, percentage, message))
        sys.stdout.flush()

    def __generate_chars_deque(self, pattern_string):
        chars = [char for char in pattern_string]
        display_pattern = deque(self.__repeat_list(chars, self._segments))
        return display_pattern

    def __repeat_list(self, l, n):
        '''
        Repeats a given list l until length n is reached.
        e.g. [1,2,3] -> repeatList([1,2,3], 7) -> returns [1,2,3,1,2,3,1]
        '''
        l.extend(l * n)
        l = l[:n]
        return l



from time import sleep

def simulate_long_task(progress_bar):
    for i in range(total):
        sleep(0.02) # simulate task that takes a while
        progress_bar.show_progress(i, 'my message')

# demo usage
total = 1000
progress_bar = Progressbar(total)
# optional parameters that can be set to your liking
progress_bar.set_display_pattern("wave")
progress_bar._animation_speed = 5
simulate_long_task(progress_bar)

progress_bar.set_display_pattern("rectangle")
simulate_long_task(progress_bar)

progress_bar.set_display_pattern("table_flip")
progress_bar._rainbow_color_change_speed = 1.0
progress_bar._animate_left_to_right = False
simulate_long_task(progress_bar)

progress_bar.set_display_pattern("rectangle")
progress_bar._rainbow_wave_enabled = False
progress_bar._rainbow_color_change_speed = 3.0
simulate_long_task(progress_bar)

# you can also set your own DisplayPattern
progress_bar.add_new_display_pattern("my_pattern", "custom_display_pattern") # _segments % len(_display_pattern) should be 0 to get a perfect loop
progress_bar.set_display_pattern("my_pattern")
# you could also add and set the displaypattern in one line
# progress_bar.add_and_set_new_display_pattern("myNewPattern", "custom_display_pattern")
progress_bar._rainbow_wave_enabled = True
progress_bar._rainbow_color_change_speed = 1.0
simulate_long_task(progress_bar)
# endregion