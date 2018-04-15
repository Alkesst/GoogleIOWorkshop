# Python Bot MiniWorkshop!

### [Try the bot!](https://t.me/gdgio_bot)

Welcome. If you are reading this, you have probably attended to the
GDG Malaga's retransmission of the Google I/O the past
8th of May. Before the retransmission I did a little workshop about
Bots made with Python.

Link to the workshop slides:
```
Insertar link a las slides.
```

##### Requirements
- Python or Docker

##### How to install
Just run this command ` pip install -r requirements.txt ` and all done ;)

### Docker time!
Before creating the image with docker, we need to create the
.env with the next content:
```
TELEGRAM_TOKEN=*REPLACE WITH YOUR TELEGRAM TOKEN!*
BOT_PATH=*USE A CUSTOM PATH*
```

By default the BOT_PATH is set to `.`

First create the image with `docker image build -t *tag_name*` .
 and will create an image from the Dockerfile.

Once created your image, just run with
`docker run -it --rm -v *pytel_files_path*:/pytel_stuff
--env-file .env *tag_name*`.


