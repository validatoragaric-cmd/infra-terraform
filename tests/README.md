# infra-terraform

[![Terraform](https://img.shields.io/badge/Terraform-%237B42F0.svg?style=for-the-badge&logo=terraform)](https://www.terraform.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

This repository contains infrastructure as code (IaC) managed using Terraform. It provides a modular and reusable approach to deploying and managing cloud infrastructure.

## Overview

This project aims to automate the creation and management of infrastructure resources across various cloud providers.  It leverages Terraform's capabilities to define infrastructure in a declarative manner, ensuring consistency and repeatability.

## Structure

The repository is organized as follows:

```
infra-terraform/
├── modules/          # Reusable Terraform modules
│   ├── compute/      # Module for creating compute instances
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── README.md
│   ├── network/      # Module for creating networks
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── README.md
│   └── ...
├── environments/     # Environment-specific configurations
│   ├── dev/          # Development environment
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── README.md
│   ├── staging/      # Staging environment
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── README.md
│   ├── prod/         # Production environment
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── README.md
│   └── ...
├── scripts/          # Helper scripts for deployment and management
│   ├── deploy.sh
│   ├── destroy.sh
│   └── ...
├── code_of_conduct.md # Contributor Covenant Code of Conduct
├── LICENSE
└── README.md        # This file
```

## Getting Started

### Prerequisites

*   [Terraform](https://www.terraform.io/downloads.html) (v1.0 or later)
*   [AWS CLI](https://aws.amazon.com/cli/) (if using AWS) or equivalent CLI for your cloud provider
*   Appropriate cloud provider credentials configured (e.g., AWS access keys, Google Cloud credentials, Azure service principal)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/infra-terraform.git
    cd infra-terraform
    ```

2.  Configure your cloud provider credentials. For example, for AWS:

    ```bash
    aws configure
    ```

### Usage

1.  Navigate to the environment you want to deploy (e.g., `environments/dev`).

    ```bash
    cd environments/dev
    ```

2.  Initialize Terraform:

    ```bash
    terraform init
    ```

3.  Review the Terraform plan:

    ```bash
    terraform plan
    ```

4.  Apply the Terraform configuration:

    ```bash
    terraform apply
    ```

    *   You may be prompted to confirm the changes. Type `yes` to proceed.

5.  To destroy the infrastructure:

    ```bash
    terraform destroy
    ```

    *   You may be prompted to confirm the destruction. Type `yes` to proceed.

## Modules

The `modules/` directory contains reusable Terraform modules. Each module encapsulates a specific piece of infrastructure, such as compute instances, networks, or databases.

Refer to the `README.md` file within each module for detailed information on its usage and configuration.

## Environments

The `environments/` directory contains environment-specific configurations. Each environment (e.g., `dev`, `staging`, `prod`) has its own `main.tf`, `variables.tf`, and `terraform.tfvars` files.

*   `main.tf`: Defines the infrastructure resources for the environment.
*   `variables.tf`: Defines the input variables for the environment.
*   `terraform.tfvars`: Defines the values for the input variables, specific to the environment.

## Contributing

We welcome contributions to this project! Please read the [Contributing Guidelines](CONTRIBUTING.md) for details on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](code_of_conduct.md). By participating in this project, you agree to abide by its terms.