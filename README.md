# {{cookiecutter.service_name}}

This is a repository for a cloud function developed with [Crowdbotics](https://www.crowdbotics.com/)

## Features

* Uses the [Serverless](https://serverless.com/) framework.
* Build to deploy to [AWS Lambda](https://aws.amazon.com/lambda/).
* Provides a single REST endpoint at `GET /hello`.
* Uses Python 3.7.

## Getting Started

1. [Install](https://serverless.com/framework/docs/getting-started/) the Serverless framework on your local machine.
2. [Configure](https://serverless.com/framework/docs/providers/aws/guide/credentials/) your AWS provider credentials for Serverless framework.
3. `$ cd <clone root directory>`
4. `$ serverless deploy -v`
5. Invoke the function:
    `$ serverless invoke -f hello`

