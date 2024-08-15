# `ml-service-template`
This is a machine learning service template that contains the sample code of a [scikit-learn](https://scikit-learn.org/stable/) machine learning model. The model is
1. served using [FastAPI](https://fastapi.tiangolo.com/),
2. containerized using [Docker](https://www.docker.com/), and
3. deployed to [Amazon Web Services (AWS)](https://aws.amazon.com/) using [Terraform](https://www.terraform.io/).

## What motivated the creation of this template?
To enable data scientists and ML practitioner to focus on building machine learning models in production and not worry about model serving or model deployment.

## What resources did I use to help create this template?
- [Serve machine learning models with FastAPI](https://medium.com/@theDrewDag/serve-machine-learning-models-with-fastapi-e329ca3a89c6) by [Andrea D'Agostino](https://www.linkedin.com/in/andrewdag/)
- [Deploy a FastAPI App on AWS ECS](https://medium.com/aspiring-data-scientist/deploy-a-fastapi-app-on-aws-ecs-034b8b7b5ac2) by [Tom Sharp](https://medium.com/@tomsharp)

## I'm in. How do I use the template to build models?
1. Clone this repository:
   ```
   $ git clone git@github.com:shilongjaycui/ml-service-template.git
   ```
2. Navigate into the repository:
   ```
   $ cd ml-service-template
   ```
3. [Create an AWS account](https://aws.amazon.com/resources/create-account/) if you don't have one already.
4. [Install AWS Command Line Interface (CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html); then, verify you have AWS CLI successfully installed on your local machine by running the following commands:
   ```
   $ which aws
   /usr/local/bin/aws
   $ aws --version
   aws-cli/2.15.30 Python/3.11.6 Darwin/23.3.0 botocore/2.4.5
   ```
5. Create an [IAM](https://aws.amazon.com/iam/) user with just enough permissions (see why [here](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html)) to deploy Docker containers to [ECS](https://aws.amazon.com/ecs/):

   ![`ml-service-template` IAM user](./ml-service-template-iam-user.png)
6. Configure the terminal session to use the newly-created IAM user:
   ```
   $ aws configure
   AWS Access Key ID: <paste your access key ID from the previous step and hit enter>
   AWS Secret Access Key: <paste your secret access key from the previous step and hit enter>
   Default region name: us-west-2
   Default output format [None]: <just hit enter>
   ```
7. Set up Amazon Elastic Container Registry (Amazon ECR) in your AWS account:
   ```
   $ make setup-ecr
   ```
8. Build and push your Docker image to Amazon ECR:
   ```
   $ make deploy-container
   ```
9. Deploy your machine learning service (served & containerized scikit-learn model) to AWS:
   ```
   $ make deploy-service
   ```
10. Click on the link (Terraform output) in your terminal to interact with your machine learning service.
11. **IMPORTANT:** When you're done interacting with your service, destroy it.
    ```
    $ make destroy-service
    ```

## What upcoming features can I expect in the future?
- [ ] library-agnostic development: You can develop your machine learning model using scikit-learn, PyTorch, TensorFlow, or Keras.
- [ ] cloud-agnostic deployment: You can deploy your machine learning model to AWS, Azure, or GCP.
