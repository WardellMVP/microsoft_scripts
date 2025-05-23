# Obsidian Demo Scripts

This repository contains two independent modules used to generate baseline activity in a demo Azure AD tenant.

## Terraform Module `baseline_user`

Creates a single Azure AD user and assigns a few built‑in roles.

### Usage

1. Install [Terraform](https://www.terraform.io/).
2. Change into the `terraform` folder and create a `terraform.tfvars` file:

```hcl
user_principal_name = "baseline-user@<your-domain>"
password            = "<strong password>"
```

3. Initialize and apply the configuration:

```bash
terraform init
terraform apply
```

The module creates `baseline-user` and assigns the *Cloud Administrator*, *Application Administrator* and *Exchange Administrator* roles.

### Outputs

- `user_object_id` – the created user's object ID
- `role_ids` – IDs of the assigned roles

Run `terraform destroy` to remove all resources.

## Python Baseline Activity Simulator

Generates Microsoft Graph activity using the newly created user.

### Setup

1. Ensure Python 3.8+ is installed.
2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Create a `config.yaml` file (or set environment variables):

```yaml
auth_type: client_credentials
tenant_id: <tenant id>
client_id: <application id>
client_secret: <client secret>
```

4. Run the simulator:

```bash
python main.py --duration 300 --rate 2
```

The `--duration` flag specifies how long to run in seconds. `--rate` controls the approximate actions per minute. Logs are written to `baseline.log` in JSON format and include a `"baseline": true` tag for filtering.

## File Overview

| Path | Purpose |
|------|---------|
| `terraform/main.tf` | Terraform resources for user creation and role assignment |
| `terraform/variables.tf` | Input variables for the Terraform module |
| `terraform/outputs.tf` | Output values from the Terraform module |
| `python/auth.py` | Authentication helper using MSAL |
| `python/actions.py` | Stubbed action implementations using Microsoft Graph |
| `python/logger.py` | Rotating JSON logger for action results |
| `python/scheduler.py` | Randomized scheduler for executing actions |
| `python/main.py` | Entry point that wires everything together |
| `python/requirements.txt` | Python dependencies |
