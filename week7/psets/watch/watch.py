import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r'^<iframe(?:[a-zA-Z0-9=" ]+)?src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]{11})"(?:[a-zA-Z0-9="\;\- ]+)?></iframe>$', s):
        video = matches.group(1)
        return f"https://youtu.be/{video}"


if __name__ == "__main__":
    main()


# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# <iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>
# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# <iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>
# <iframe width="560" height="315"src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>