import sys
import getopt
from epubcheck_summary import EpubcheckSummary


def print_usage():
    print("%s --file=filename [--error=error_number]" % sys.argv[0])
    sys.exit(1)


def run():
    opts, args = getopt.getopt(sys.argv[1:], None, ["file=", "error=", "help"])
    epubcheck_filename = None
    error_index = None
    for opt, arg in opts:
        if opt == "--file":
            epubcheck_filename = arg
        if opt == "--error":
            error_index = arg
        if opt == "--help":
            print_usage()

    if epubcheck_filename is None:
        print_usage()

    results_file = open(epubcheck_filename, 'r')

    summary = EpubcheckSummary(results_file)
    summary.populate()
    summary.display(error_index)

    results_file.close()

if __name__ == "__main__":
    run()
