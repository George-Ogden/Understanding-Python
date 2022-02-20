from progress.bar import *
from progress.spinner import *
from progress.counter import *
from progress.colors import COLORS

import random
import time

def display_bar(bar_type,steps=10000):
    bar = bar_type(max=steps,color=random.choice(COLORS),message=f"{type(bar_type()).__name__:<20}")
    bar.start()
    for i in range(random.randint(1, steps)):
        bar.next()
    bar.goto(random.randint(int(bar.progress * steps), steps))
    while bar.remaining:
        bar.next()
    bar.finish()

def display_spinner(spinner_type,steps=20):
    spinner = spinner_type(max=steps,message=f"{type(spinner_type()).__name__:<20}")
    spinner.start()
    for i in range(steps):
        spinner.next()
        time.sleep(0.1)
    spinner.finish()

def display_counter(counter_type,steps=100):
    counter = counter_type(max=steps,message=f"{type(counter_type()).__name__:<20}")
    counter.start()
    for i in range(steps):
        counter.next()
        time.sleep(0.01)
    counter.finish()

display_bar(Bar)
display_bar(ChargingBar)
display_bar(FillingSquaresBar)
display_bar(FillingCirclesBar)
display_bar(IncrementalBar)
display_bar(PixelBar)
display_bar(ShadyBar)

display_spinner(Spinner)
display_spinner(LineSpinner)
display_spinner(MoonSpinner)
display_spinner(PieSpinner)
display_spinner(PixelSpinner)

display_counter(Counter)
display_counter(Countdown)
display_counter(Pie)
display_counter(Stack)