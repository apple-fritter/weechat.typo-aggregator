# Typo Monger
This script is designed to run on the `WeeChat` IRC client and checks for spelling errors in messages sent by users in the IRC channel. It uses the `PyEnchant` library to check spelling and the csv module to record misspelled words in a TSV (tab-separated values) file.

The `process_message()` function is called every time a message is sent to the IRC channel. It first extracts the username of the sender from the message prefix. Then it splits the message into words and checks each word for spelling errors using the dictionary.check() method provided by PyEnchant.

If a misspelled word is found, the script checks if the word has already been recorded in the TSV file. If it has, it increments the count of the misspelled word for that user. If it has not been recorded, it adds a new row to the TSV file with the username, misspelled word, and a count of 1.

The script is registered as a WeeChat plugin using the `weechat.register()` function. It also uses the `weechat.hook_print()` function to register the `process_message()` function as a hook for incoming messages.

## Requirements
To run this script, you'll need to have the following:

`WeeChat` IRC client: This script is designed to run on the WeeChat client, so you'll need to have it installed on your system. WeeChat is available for Linux, macOS, and Windows.

`Python 3`: The script is written in Python, so you'll need to have Python 3 installed on your system.

`PyEnchant` library: This library is used to check spelling in the messages. You can install it using pip, the Python package manager, by running the following command in your terminal:

```bash
pip install pyenchant
```

This will install the PyEnchant library and its dependencies.

TSV file: The script writes misspelled words to a TSV (tab-separated values) file. You'll need to create an empty file named "misspelled_words.tsv" in the same directory as the script. The script will create the file if it does not exist.

Once you have all of these requirements installed, you can run the script in WeeChat by copying the script code into a file named "misspelled_words.py" in your WeeChat plugins directory (usually ~/.weechat/python/), and then loading the script in WeeChat using the /python load command.

## Process Flowchart
```
.
├── Initialize
│   ├── Import modules
│   ├── Set spellchecker dictionary
│   └── Define process_message()
├── Process Message
│   ├── Extract username
│   ├── Split message into words
│   └── For each word:
│       ├── If word is misspelled:
│       │   ├── Assign word
│       │   ├── Check if recorded
│       │   │   ├── If found:
│       │   │   │   ├── Set flag
│       │   │   │   ├── Increment count
│       │   │   │   └── Update row
│       │   │   └── If not found:
│       │   │       ├── Set flag
│       │   │       └── Create new row
├── Return
│   └── Return weechat.WEECHAT_RC_OK
└── Register and Connect
    ├── Register script with weechat
    ├── Connect to IRC channel
    └── Hook print event
```
## Potential use cases
Here are some use cases where this script could be helpful:

1. Language learners: If you are learning a new language and using an IRC channel to practice, this script could help you identify and learn from your spelling mistakes.
2. Moderators: If you are a moderator of an IRC channel and want to encourage users to write in correct English, this script could help you keep track of common spelling mistakes and provide feedback to users.
3. Writing communities: If you are a member of a writing community that uses an IRC channel to collaborate and share work, this script could help you improve the quality of writing by identifying and correcting spelling errors.
4. Quality assurance: If you are developing a product that involves user-generated content, this script could help you identify and correct spelling errors in user submissions.
5. Language researchers: If you are a researcher studying language use in online communities, this script could help you analyze the prevalence of spelling errors and patterns of usage in IRC channels.

## Potential concerns
1. Privacy concerns: The script records misspelled words along with the username of the person who wrote them. Depending on the context, this could be seen as a violation of privacy or as a potential source of embarrassment for users.
2. False positives: The script uses the PyEnchant library to check spelling, which may not be perfect. In some cases, the library may flag a word as misspelled even if it is not. This could lead to users being incorrectly identified as making spelling mistakes.
3. False negatives: The script may not catch all spelling errors. For example, it may miss misspellings of proper nouns or technical terms that are not included in the dictionary.
4. Performance issues: The script reads and writes to a TSV file every time a misspelled word is found, which could impact the performance of the system if the file becomes large or there are many users generating misspelled words.
5. Legal issues: Depending on the context, recording misspelled words could be seen as a potential liability. For example, if the IRC channel is used for professional communication, incorrect spelling could lead to misunderstandings or legal disputes.

> It is important to consider the potential benefits and drawbacks of using this script in the context of your specific use case and to be transparent with users about how their data is being used.

## IRC Meta

### WeeChat
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. (Python)
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Record misspelled words in a TSV (tab-separated values) file. (Python)
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. (Python)
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Extract video information from a YouTube URL and post it back to the channel. (Python)

### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from IRCcloud format to Weechat format. (Rust)
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from IRCcloud format to XChat format. (Rust)

### X-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. (Python)
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. (Python bundle)

### Other
- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format definition. (Rust)

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
