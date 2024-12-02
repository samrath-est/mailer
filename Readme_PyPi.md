# Mailer Module

## Overview

The Mailer module is a configurable Python class that handles email functionalities across an application. It provides robust features for sending emails with HTML templates, attachments, and scheduling, as well as reading emails with advanced filtering capabilities.

## Features

- Send emails with HTML templates
- Dynamic HTML template rendering
- Attachment support
- CC and BCC email support
- Email validation
- Email scheduling
- Email reading with filtering
- IMAP and SMTP support

## Installation

### Dependencies

- Python 3.7+
- Required libraries:
  - `Pillow` (PIL)
  - `beautifulsoup4`

Install dependencies using pip:
```bash
pip install Pillow beautifulsoup4
```

## Usage

### Initializing the Mailer

```python
from mailer import Mailer

mailer = Mailer(
    sender_email="your_email@example.com",
    password="your_password",
    sender_name="Your Name",
    port=587,
    smtp_server="smtp.gmail.com"
)
```

### Sending an Email

```python
result = mailer.send_email(
    subject="Welcome",
    html_template="app/templates/welcome",
    recipients=["recipient@example.com"],
    data={"name": "John Doe"},
    cc_email=["cc@example.com"],
    bcc_email=["bcc@example.com"]
)
```

### Scheduling an Email

```python
result = mailer.schedule_email(
    subject="Delayed Notification",
    html_template="app/templates/notification",
    recipients=["recipient@example.com"],
    delay_seconds=3600  # Send after 1 hour
)
```

### Reading Emails

```python
emails = mailer.read_emails(
    username="your_email@example.com",
    password="your_password",
    folder="INBOX",
    limit=5,
    filter_criteria={
        "from": "sender@example.com",
        "subject": "Important"
    },
    mark_as_read=True
)
```


## Important Notes

- Use app-specific passwords for Gmail
- Ensure HTML templates are properly formatted
- Handle exceptions when sending or reading emails

## Security

- Never hardcode sensitive information like passwords
- Use environment variables or secure credential management

## Limitations

- Requires internet connectivity
- Email sending/reading depends on SMTP/IMAP server availability

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the project repository.

## License

[Add your project's license information]