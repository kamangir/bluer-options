from bluer_options.timing import timing
from time import sleep


def test_timing_timing():
    @timing.time
    def func1():
        sleep(0.01)

    func1()

    timing.log()

    timing.calculate()

    assert len(timing.stats) == 1
    assert isinstance(timing.as_dict, dict)

    # ---

    @timing.time("func2, other name")
    def func2():
        sleep(0.005)

    func2()

    timing.log()

    assert len(timing.stats) == 2

    # ---

    timing.reset()
    timing.log()

    assert len(timing.stats) == 0

    # ---

    @timing.time()
    def func3(count: int = 100):
        for _ in range(count):
            func1()

            func2()

    func3()

    timing.log()

    assert len(timing.stats) == 3
