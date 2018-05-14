# Python Bot MiniWorkshop!

### [Try the bot!](https://t.me/gdgio_bot)

Welcome. If you are reading this, you have probably attended to the
GDG Malaga's retransmission of the Google I/O the past
8th of May. Before the retransmission I did a little workshop about
Bots made with Python.

Link to the workshop slides: [Link :)](https://drive.google.com/open?id=1gf2X7STMCPofyAqK8nyVi1O4cRwkL8VTXPK1jjdIEMo)

##### Requirements
- Python or Docker

##### How to install
Just run this command ` pip install --no-cache-dir -r requirements.txt ` and all done ;)

### Docker time!
Before creating the image with docker, we need to create the
.env with the next content:
```
TELEGRAM_TOKEN=*REPLACE WITH YOUR TELEGRAM TOKEN!*
BOT_PATH=*USE A CUSTOM PATH*
```

By default the BOT_PATH is set to `.`

First create the image with `docker image build -t *tag_name* .`
 and will create an image from the Dockerfile.
 Do not forget the dot at the final of the docker image build ;)

 Yeah, I forgot that dot a couple of times ;).

Once created your image, just run with
`docker run -it --rm --env-file .env *tag_name*`.


