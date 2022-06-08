# NotSengrid
NotSendgrid is a docker base image for developing and testing locally end-to-end email automation platforms, from mocking a Sendgrid API call to send emails and received them in a local SMTP Server with Web Interface, allowing sending, viewing, testing emails during development phase.

## Dockerized

The **notsengrid** server and the UI are both contained in the same docker-image which you can pull from [docker-hub](https://hub.docker.com/repository/docker/carrasquel/notsendgrid) and start it via:

```shell
docker run -it -p 3000:3000 -p 8025:8025 -e "API_KEY=sendgrid-api-key" carrasquel/notsendgrid:latest
```

Notsendgrid also supports SSL using [Let's Encrypt](https://letsencrypt.org/). To enable SSL, run it as follows:
```shell
docker run -it -p 3000:3000 -p 8025:8025 -e "API_KEY=sendgrid-api-key" -e "CERT_DOMAINNAMES=[your-domain-name]" -e "CERT_EMAIL=[your-email-address]" carrasquel/notsendgrid:latest
```

### Support development

If you liked this, donate to the cause.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/carrasquel)

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2022-present, Nelson Carrasquel