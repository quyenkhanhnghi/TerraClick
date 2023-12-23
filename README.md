# Realtime DevOps Project: Static Website Hosting with Terraform on AWS

<img width="394" alt="Screenshot 2023-12-21 at 07 30 13" src="https://github.com/quyenkhanhnghi/TerraClick/assets/108847306/2436cb82-e52c-4c2b-bc66-9454a3592bd0">

[Demo Link HERE 🔗](https://terraclick.s3.amazonaws.com/index.html)
## Introduction

This project demonstrates the power of Infrastructure as Code (IaC) through Terraform to provision and manage AWS resources for hosting a static website.
It is designed to help beginners understand the principles of Terraform, AWS, and the power of automation in DevOps practices.
## Stack

- **Infrastructure Management**: Terraform
- **Cloud Provider**: AWS Cloud
- **Content Generation**: OpenAI

## Features

- **Fully Automated Static Website Hosting**: With a single command, Terraform scripts will provision the necessary AWS infrastructure for hosting a static website.
- **Realtime Infrastructure Setup**: The entire setup process takes only 3 seconds, showcasing the efficiency and speed of Terraform in a DevOps environment.
- **Educational Tool for DevOps Beginners**: This project serves as an excellent starting point for those new to Terraform and AWS, highlighting best practices in IaC.
- **Dynamic Content Generation**: Utilizes OpenAI to generate the initial HTML content.

## Getting Started

### Prerequisites

- An AWS account with the necessary permissions to create S3 buckets and other related services.
- Terraform installed on your machine.
- AWS CLI configured with access to your AWS account.

### Get Started

1. **Clone the Repository**:
    ```
    git clone git@github.com:quyenkhanhnghi/TerraClick.git
    cd terraclick
    ```

2. **Initialize Terraform**:
    ```
    terraform init
    ```

3. **Deploy the Infrastructure**:
    ```
    terraform apply
    ```

4. **Verify Deployment**:
    - Check the AWS Management Console to see the new S3 bucket with your static website.
    - Access the website via the provided S3 bucket endpoint.

## How It Works

The Terraform scripts in this project are configured to interact with the AWS Cloud to perform the following actions:

- Create an S3 bucket configured for static website hosting.
- Set appropriate permissions so the website is publicly accessible.
- Generate an initial `index.html`, `error.html` using OpenAI's content generation prompt.
- Upload the generated `index.html`, `error.html` to the S3 bucket.
- Provide the URL to access the hosted static website upon successful deployment.
- A Python script `update_urls.py` updates the `src` attributes in the HTML files to point to the correct image URLs hosted in the S3 bucket.

## Maintainers

This project is maintained by [quyenkhanhnghi](https://github.com/quyenkhanhnghi). Feel free to reach out if you have any questions or suggestions.

## License

This project is not currently under any open-source license and is available for educational purposes.

## Acknowledgments

Special thanks to OpenAI for providing the AI-powered content generation tool used in this project.
