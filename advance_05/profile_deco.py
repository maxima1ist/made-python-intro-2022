import io
import pstats
import cProfile


def profile_deco(func):
    pr = cProfile.Profile()

    def wrapper(*args, **kwargs):
        pr.enable()
        res = func(*args, **kwargs)
        pr.disable()
        return res

    wrapper.pr = pr

    def print_stat():
        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(wrapper.pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

    wrapper.print_stat = print_stat

    return wrapper
