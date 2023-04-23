import weechat
import enchant
import csv

# Load the spellchecker dictionary
dictionary = enchant.Dict("en_US")

def process_message(data, buffer, date, tags, displayed, highlight, prefix, message):
    # Extract the username of the sender
    username = prefix.split("!")[0]

    # Split the message into words
    words = message.split()

    # Check each word for spelling errors
    for word in words:
        if not dictionary.check(word):
            misspelled_word = word

            # Check if the word has already been recorded in the TSV file
            found = False
            with open("misspelled_words.tsv", "r") as file:
                reader = csv.reader(file, delimiter="\t")
                for row in reader:
                    if row[0] == username and row[1] == misspelled_word:
                        found = True
                        count = int(row[2]) + 1
                        row[2] = str(count)
                        break

            # If the word has not been recorded, add a new row to the TSV file
            if not found:
                count = 1
                with open("misspelled_words.tsv", "a") as file:
                    writer = csv.writer(file, delimiter="\t")
                    writer.writerow([username, misspelled_word, str(count)])

    return weechat.WEECHAT_RC_OK

# Connect to the IRC channel
weechat.register("misspelled_words", "OpenAI", "1.0", "GPL3", "misspelled_words", "", "")
weechat.hook_print("", "", "", 1, "process_message", "")
