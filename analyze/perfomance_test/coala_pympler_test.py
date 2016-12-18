from pympler.tracker import SummaryTracker
from tests.TestUtilities import bear_test_module
from tests.TestUtilities import execute_coala
from coalib import coala
from coalib import coala_json


def coala_test():
    execute_coala(coala.main, 'coala', '-F', '--json')


tracker = SummaryTracker()
coala_test()
tracker.print_diff()
