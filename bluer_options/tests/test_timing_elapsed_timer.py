from bluer_options.timing.elapsed_timer import ElapsedTimer
from time import sleep


def test_timing_elapsed_timer():
    elapsed_timer = ElapsedTimer()
    sleep(1)
    elapsed_timer.stop()

    assert elapsed_timer.elapsed_time > 0
    assert isinstance(elapsed_timer.elapsed_pretty(), str)
