
#description: alter long embedded youtube URLs in source code of internet pages back to shorter youtube URLs using regular expressions.

import re

def main():
    print(parse(input("HTML: ")))























def parse(s):
    matches = re.search(r'<iframe.*src="https?://(?:www\.)?youtube.com/embed/(.+)"', s)
    if matches:
      return ("https://youtu.be/" + matches.group(1))

    else:
      return None


if __name__ == "__main__":
    main()
