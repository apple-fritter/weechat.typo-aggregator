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

---

## <a id="irc-meta"></a>🤪 IRC Meta
### <a id="fritterz"></a> [@apple-fritter](https://github.com/apple-fritter)'s IRC Repositories:

---

#### Driftwood Suite of IRC Analytics
###### Driftwood utilities
- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format definition. (Rust)
- [flotsam](https://github.com/apple-fritter/flotsam): Aggregate a per-user metric of flagged contributions to any given user. (Rust)
- [jetsam](https://github.com/apple-fritter/jetsam): Flag lines of driftwood formatted IRC logs for sanitization, moderation, or further review. (Rust)
- [scrimshaw](https://github.com/apple-fritter/scrimshaw): Create a quoteslist of any given user, from your driftwood formatted logs. (Rust)

##### Driftwood native logging plugins
- [weechat.driftwood](https://github.com/apple-fritter/weechat.driftwood): Natively log WeeChat messages in the driftwood standard. (Python)

---

#### heX-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. (Python)
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. (Python bundle)

---

#### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from IRCcloud format to Weechat format. (Rust)
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from IRCcloud format to XChat format. (Rust)

---

#### WeeChat
- [weechat.driftwood](https://github.com/apple-fritter/weechat.driftwood): Natively log WeeChat messages in the driftwood standard. (Python)
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. (Python)
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Record misspelled words in a TSV (tab-separated values) file. (Python)
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. (Python)
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Deprecated. Extract video information from a YouTube URL and post it back to the channel. (Python)
- [weechat.youtube-api](https://github.com/apple-fritter/weechat.youtube-api): Extract video information from a YouTube URL and post it back to the channel. (Python)

---

### IRC usage considerations
When working with any project involving IRC (Internet Relay Chat), it's important to keep the following considerations in mind to ensure a positive and respectful environment for all participants.

#### Philosophy of Use
Tailor your project's behavior and responses to align with the expected norms and conventions of IRC. Take into account the preferences and expectations of IRC users, ensuring that your project provides a seamless and familiar experience within the IRC ecosystem.

#### Foster a Positive and Inclusive Environment
Respect and adhere to the guidelines and policies of the IRC platform you are using. Familiarize yourself with the platform's rules regarding script usage, automation, and acceptable behavior. Comply with the platform's Terms of Service, and be mindful of any limitations or restrictions imposed by the platform. Strive to create an inclusive and welcoming environment where all users can engage respectfully and comfortably.

#### Respect the Rights and Dignity of Other Users
Maintain a polite and courteous demeanor in all interactions. Uphold the fundamental principles of respect, avoiding engagement in illegal, inappropriate, or offensive behavior. This includes refraining from using derogatory or inflammatory language, sharing explicit, triggering, or offensive content, engaging in harassment, or launching personal attacks. Obtain explicit consent before interacting with other users or sending automated responses. Respect the privacy of other users and avoid invading their personal space without their permission.

#### Respect the IRC Community and Channels
Avoid disrupting the normal flow of conversation within IRC channels. Ensure that your project's actions and responses do not cause unnecessary disruptions or inconvenience to other users. Implement mechanisms to prevent spamming or flooding the channel with excessive or irrelevant messages. Handle errors gracefully, preventing unintended behavior or disruptions to the IRC platform or the experiences of other users.

#### Ensure Compatibility
Consider the potential variations in behavior across different IRC platforms and clients. While aiming for compatibility, be aware that certain functionalities may not be available or consistent across all platforms. Test your project on multiple IRC platforms and clients to ensure compatibility and provide the best possible experience for users.

---

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

---

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

---

## License
This project is licensed under the [MIT License](LICENSE).
