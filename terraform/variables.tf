variable "user_principal_name" {
  description = "UPN for baseline user"
  type        = string
}

variable "user_password" {
  description = "Password for baseline user"
  type        = string
  sensitive   = true
}

variable "resource_group_name" {
  description = "Resource group for log analytics workspace"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "log_analytics_workspace_name" {
  description = "Name of the log analytics workspace"
  type        = string
  default     = "baseline-logs"
}
