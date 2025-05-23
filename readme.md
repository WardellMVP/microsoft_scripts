You are a DevSecOps coding assistant. Your goal is to generate two code modules for my Obsidian Security demo tenant:

1. **Terraform module**  
   - Defines a user named `baseline-user`  
   - Assigns the built-in roles: Cloud Administrator, Application Administrator, and Exchange Administrator  
   - Configures diagnostic settings on the subscription to send all activity logs to a Log Analytics workspace named `baseline-logs`  

2. **Python baseline simulator**  
   - Uses MSAL and the Microsoft Graph Python SDK to authenticate as `baseline-user`  
   - Performs a random sequence of the following over a configurable time window:  
     - Sign-in (Graph `/me` query)  
     - Send an email via `/me/sendMail`  
     - Read the inbox via `/me/mailFolders/Inbox/messages`  
     - List all App Registrations (`/applications`)  
     - Create or update a group (`/groups`)  
     - Create and delete a storage account in an existing resource group  
     - Sleep a random 30–120 seconds between actions  

   - Logs each action to a rotating JSON file with fields: `timestamp`, `action`, `status`, and `response_id`  
   - Provides a CLI flag `--duration` for total run time and `--rate` for average actions per minute  

**Requirements:**  
- Idempotent Terraform so repeated `apply`/`destroy` works cleanly  
- Python code must be modular—separate auth, action library, scheduler, and logger  
- README with instructions to deploy Terraform, configure Python dependencies, and run the simulator  

Please output:  
1. A Terraform `main.tf` (plus variables and outputs) for the module.  
2. A Python project skeleton (`auth.py`, `actions.py`, `scheduler.py`, `logger.py`, `main.py`) with stub functions and comments where specific Graph calls should go.  
3. A brief summary table of what files were created and their purpose.  
