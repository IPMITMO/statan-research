from pylama.main import shell
from pympler.tracker import SummaryTracker


def pylama_test():
    shell('-l pylint ../perf_test/requests-2.12.1/'.split(), error=False)

tracker = SummaryTracker()
pylama_test()
tracker.print_diff()
