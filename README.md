# ed-discman-discord-bot
Bot for my favourite tiktoker EdDiscman!

It can:

Slash commands:
- Post random EdDiscman quotes
- Post random useless facts in both English and German language
- Shorten a URL
- Post the message in uppercase
- Check it's own latency
- It has a functional YouTube music bot (and support other services that youtube-dl supports)

Background tasks:
- Give an alert when new tiktok video shows up (the check is set to take place every 1 hour)
- Greet a user when he shows up on the server for the first time (sprawdzić bo chyba znikło jakoś w trakcie pisania)
- Greet a user when he says "Hello"
- Post random funny Robert Kubica pictures if any message on the server contains consecutive "EEEE"

TODO:
- Offload every constant left to constants.py
- Cogs shouldn't be loaded if required constants hasn't been set in constants.py
- Implement possibility to reload cogs if necessary when bot is still online as a slash command

