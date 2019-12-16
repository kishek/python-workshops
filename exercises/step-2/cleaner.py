from shutil import copyfile
from re import search, compile
from json import dumps

# Name of file where formatted lines are to be placed:
FILE_NAME = 'server.log'
# Regex paths for logging:
REGEX_TIME = r'\w+:127.0.0.1.*?\[(?P<date>.*?) (?P<timestamp>.*?)\] '
REGEX_REQUEST = r'\"(?P<http_method>.*?) (?P<http_path>.*?) (?P<http_protocol>.*?)\" '
REGEX_RESPONSE = r'(?P<response_status>\d+).*?'
REGEX_LINE = compile("%s%s%s" % (REGEX_TIME, REGEX_REQUEST, REGEX_RESPONSE))


# Copy over the server log file from the application directory.
def setup(src_file):
    copyfile(src_file, FILE_NAME)


# Parses a log file and returns lines which match the expected regex.
def getLines(src_file):
    lines = []
    # Open source file and filter application lines.
    with open(src_file) as logFile:
        for line in logFile:
            # TODO: use the REGEX_LINE above to parse
            # lines which we want to extract and add them
            # to the list returned from this function.
            print(line)
    # Close the file, return all lines we want to analyse.
    logFile.close()
    return lines


# Writes formatted lines to a dest file/directory.
def write_lines(dest_file, lines):
    # TODO: write the formatted lines as a list of dictionaries
    # to the `dest_file` specified.
    return


if __name__ == '__main__':
    setup('../step-1/server.log')
    write_lines('../step-3/logs.json', getLines(FILE_NAME))
