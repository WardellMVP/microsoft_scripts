# Obsidian Demo Scripts

This repository contains a Terraform module and a Python simulator used to generate baseline activity in an Azure tenant for demo purposes.

## Terraform Deployment

1. Install [Terraform](https://www.terraform.io/).
2. Change into the `terraform` directory:
   ```bash
   cd terraform
   ```
3. Create a `terraform.tfvars` file with the following values:
   ```hcl
   user_principal_name = "baseline-user@<your-domain>"
   user_password       = "<strong password>"
   resource_group_name = "<existing resource group>"
   location            = "eastus"
   ```
4. Initialize and apply the module:
   ```bash
   terraform init
   terraform apply
   ```
   This will create the `baseline-user`, assign the Cloud Administrator, Application Administrator and Exchange Administrator roles, and configure diagnostic settings to send subscription activity logs to the `baseline-logs` workspace.

To destroy the environment run `terraform destroy` from the same directory.

## Python Baseline Simulator

The simulator authenticates as `baseline-user` and performs a variety of Microsoft Graph actions on a schedule.

### Setup

1. Ensure Python 3.8+ is installed.
2. Install required packages:
   ```bash
   pip install msal msgraph-core azure-identity azure-mgmt-storage
   ```
3. Run the simulator:
   ```bash
   python -m python_baseline.main --tenant-id <tenant> --client-id <app id> \
       --client-secret <secret> --mail-to user@example.com --duration 30 --rate 6
   ```
   The `--duration` flag specifies how long (in minutes) to run. `--rate` controls the average number of actions per minute.

Log output is written to `baseline.log` in JSON format.

## File Overview

| Path | Purpose |
|------|---------|
| `terraform/main.tf` | Terraform resources for user, role assignments and diagnostic settings |
| `terraform/variables.tf` | Input variables for the Terraform module |
| `terraform/outputs.tf` | Output values from the Terraform module |
| `python_baseline/auth.py` | Authentication helper using MSAL and Graph SDK |
| `python_baseline/actions.py` | Library of simulator actions using Microsoft Graph |
| `python_baseline/scheduler.py` | Runs random actions over a time window |
| `python_baseline/logger.py` | Rotating JSON logger for action results |
| `python_baseline/main.py` | Entry point CLI for running the simulator |
