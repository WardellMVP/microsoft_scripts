variable "user_principal_name" {
  description = "User principal name of the baseline user"
  type        = string
}

variable "display_name" {
  description = "Display name for the baseline user"
  type        = string
  default     = "baseline-user"
}

variable "password" {
  description = "Initial password for the baseline user"
  type        = string
  sensitive   = true
}
