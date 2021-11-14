# Email Builder

Send emails with [EBBS](https://eons.dev/project/basic-build-system/)!

## Usage

You'll need 2 files. The first is the account info that looks like:
```json
{
    "mail_from": "MY_EMAIL@gmail.com",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "MY_EMAIL@gmail.com",
    "password": "PASSWORD"
}
```
(replacing "MY_EMAIL" and "PASSWORD")

The next file is the actual email to send:
```json
{
    "mail_to": "RECIPIENT@gmail.com",
    "subject": "TEST",
    "message": "This is a test. I hope you like it!"
}
```
(replacing all values with what you want to send)

To send the email, invoke a command like the following:
`ebbs -v -l email . --email-config 'config.json' --message 'message.json'`
NOTE: the "." after email is still necessary even though no files from the given directory are pulled in.
This is done so that the message file can be named whatever you'd like (e.g. something more descriptive than "message.json")