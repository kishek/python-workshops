from shutil import copyfile
from re import search, compile
from json import dumps

# Regex paths for logging:
REGEX_TIME = r'\w+:127.0.0.1.*?\[(?P<date>.*?) (?P<timestamp>.*?)\] '
REGEX_REQUEST = r'\"(?P<http_method>.*?) (?P<http_path>.*?) (?P<http_protocol>.*?)\" '
REGEX_RESPONSE = r'(?P<response_status>\d+).*?'
REGEX_LINE = compile("%s%s%s" % (REGEX_TIME, REGEX_REQUEST, REGEX_RESPONSE))


def setup():
    copyfile('../step-1/server.log', 'server.log')


def getLines(srcFile):
    lines = []
    # Open source file and filter application lines.
    with open(srcFile) as logFile:
        for line in logFile:
            matches = search(REGEX_LINE, line)
            if matches:
                lines.append(matches.groupdict())
    # Close the file, return all lines we want to analyse.
    logFile.close()
    return lines


def writeLines(destFile, lines):
    file = open(destFile, 'w')
    file.write(dumps(lines))
    file.close()


if __name__ == '__main__':
    setup()
    writeLines('../step-3/logs.json', getLines('server.log'))
