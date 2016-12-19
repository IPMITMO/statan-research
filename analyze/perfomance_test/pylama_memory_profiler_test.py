from pylama.main import shell

@profile
def pylama_test():
    shell('-l pylint ../perf_test/requests-2.12.1/'.split(), error=False)

if __name__ == '__main__':
    pylama_test()