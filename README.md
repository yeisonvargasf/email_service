email_service
=============

[![pipeline](https://github.com/unofficialopensource-knit/email_service/actions/workflows/pipeline.yml/badge.svg?branch=main)](https://github.com/unofficialopensource-knit/email_service/actions/workflows/pipeline.yml)
[![Updates](https://pyup.io/repos/github/unofficialopensource-knit/email_service/shield.svg)](https://pyup.io/repos/github/unofficialopensource-knit/email_service/)

### Intro
This is a codebase for email microservice.
This microservice is responsible for email delievery.
Internally it uses google's SMTP server to send emails.
For configuration details please refer to the `.env.example` file.

This microservice is implemented using Flask, a web framework for python.
This serves following routes
```
GET /health
```
```
GET /mail/<string:mail_id>
```
```
GET /mail/
```
```
POST /mail
{
    request_id -> string
    from_address -> string
    to_address -> string
    template_id -> integer
    params -> json
}
```
```
POST /mail/batch
[
    {
        request_id -> string
        from_address -> string
        to_address -> string
        template_id -> integer
        params -> json
    }
]
```

### Contact
* **onlinejudge95**
