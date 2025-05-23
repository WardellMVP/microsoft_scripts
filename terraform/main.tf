terraform {
  required_providers {
    azuread = {
      source  = "hashicorp/azuread"
      version = ">= 2.0"
    }
  }
}

# Create baseline user
resource "azuread_user" "baseline" {
  user_principal_name = var.user_principal_name
  display_name        = var.display_name
  password            = var.password
  force_password_change = false
}

# Lookup directory roles by display name
# These data sources fail if the role does not exist in the tenant
# Ensure the roles are activated or they will be automatically enabled on assignment

data "azuread_directory_role" "cloud_admin" {
  display_name = "Cloud Administrator"
}

data "azuread_directory_role" "app_admin" {
  display_name = "Application Administrator"
}

data "azuread_directory_role" "exchange_admin" {
  display_name = "Exchange Administrator"
}

# Assign roles to the baseline user
resource "azuread_directory_role_member" "cloud_admin" {
  role_object_id   = data.azuread_directory_role.cloud_admin.id
  member_object_id = azuread_user.baseline.id
}

resource "azuread_directory_role_member" "app_admin" {
  role_object_id   = data.azuread_directory_role.app_admin.id
  member_object_id = azuread_user.baseline.id
}

resource "azuread_directory_role_member" "exchange_admin" {
  role_object_id   = data.azuread_directory_role.exchange_admin.id
  member_object_id = azuread_user.baseline.id
}
