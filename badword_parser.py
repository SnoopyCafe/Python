import sys
import os
import urllib

# Open a file of text

dir = "."
file_name = "movie_quotes_good.txt"

def read_text():
    quotes = open(file_name)
    contents = quotes.read()

    if contents is not None:
        try:
            # This only returns True if bad word or False, if not, but
            # it doesn't tell you the bad words
            response = check_profanity(contents)
            print response
            if response and response.lower() == "true":
                print check_profanity_list(contents)

        except Exception as e:
            print("Error: %s" % e.message)
        finally:
            quotes.close()
    else:
        print "Nothing to check"

def check_profanity_list(text_to_check):
    bad_word_list = ["damn","hell","shit"]

    # Parse list of words
    if isinstance(text_to_check,str):
        word_list = text_to_check.split()
        # Match words in text to bad word list
        return set([x.lower() for x in word_list]) & set(bad_word_list)

def check_profanity(text_to_check):
    try:
        url = "http://www.wdylike.appspot.com?q=" + text_to_check
        connection = urllib.urlopen(url)
        output = connection.read()
        connection.close()
        return output
    except Exception as e:
        raise e
    else:
        connection.close()


read_text()