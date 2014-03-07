import re
import operator


class EpubcheckSummary(object):
    """Shows a summary of the epubcheck output, with an option to drill down into full results by error"""
    def __init__(self, input_file):
        self.generic_errors = {}
        self.original_errors = []
        self.file = input_file

    def make_generic_error(self, message):
        # normalize message a bit; take out everything within quotes as these are
        # file-specific (just want an idea of the types)
        return re.sub(r"'.+?'", '<...>', message)

    def populate(self):
        for line in self.file:
            match = re.match(r'(?P<type>.+?): (?P<filename>.+?): (?P<message>.+)', line)

            if match is None:
                continue

            match_dict = match.groupdict()

            key = self.make_generic_error(match_dict["message"])
            generic_error = self.generic_errors.setdefault(key, {"count": 0, "type": match_dict["type"]})
            generic_error["count"] += 1

            self.original_errors.append(match_dict)

    def display(self, index=None):
        generic_errors_list = [(key, error["count"], error["type"]) for key, error in self.generic_errors.items()]
        generic_errors_list.sort(key=operator.itemgetter(2, 1))

        if index:
            current_error = generic_errors_list[int(index)-1][0]
            for error in self.original_errors:
                if self.make_generic_error(error['message']) == current_error:
                    print("%s: %s" % (error['filename'], error['message']))
        else:
            total = 0
            index = 1
            for error, count, error_type in generic_errors_list:
                print("%2d) %4d times   %s: %s" % (index, count, error_type, error))
                total += count
                index += 1

            print("----\n%4d total" % total)
