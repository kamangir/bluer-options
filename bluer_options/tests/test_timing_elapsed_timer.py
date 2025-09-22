from bluer_options.timing import ElapsedTimer
from time import sleep


def test_timing_elapsed_timer():
    elapsed_timer = ElapsedTimer()

    sleep(0.2)

    elapsed_timer_as_str = elapsed_timer.as_str(
        stop=False,
        include_ms=True,
    )
    assert isinstance(elapsed_timer_as_str, str)

    elapsed_timer.stop()

    assert elapsed_timer.elapsed_time_ > 0

    elapsed_timer_elapsed_time = elapsed_timer.elapsed_time
    assert isinstance(elapsed_timer_elapsed_time, float)
    assert elapsed_timer_elapsed_time > 0

    elapsed_timer_as_str = elapsed_timer.as_str(include_ms=True)
    assert isinstance(elapsed_timer_as_str, str)

    sleep(0.2)

    assert elapsed_timer.as_str(include_ms=True) == elapsed_timer_as_str
    assert elapsed_timer.elapsed_time == elapsed_timer_elapsed_time

    elapsed_timer.reset()

    sleep(0.1)

    assert isinstance(elapsed_timer.as_str(include_ms=True), str)
