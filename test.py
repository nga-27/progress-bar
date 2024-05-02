import time

from progress_bar import ProgressBar


def test():
    test_len = 15
    p_bar = ProgressBar(test_len, name="Testing PBAR 1", stopwatch=False)
    p_bar.start()
    for _ in range(test_len):
        p_bar.uptick()
        time.sleep(0.5)
    p_bar.end()

    print("\r\n\r\n")
    p_bar = ProgressBar(test_len, name="Testing PBAR 2", stopwatch=True)
    p_bar.start()
    for _ in range(test_len):
        p_bar.uptick()
        time.sleep(0.5)
    p_bar.end()

test()
