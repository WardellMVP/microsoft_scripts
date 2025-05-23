terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.0"
    }
  }
}

provider "azurerm" {
  features {}
}

provider "azuread" {}

resource "azuread_user" "baseline" {
  user_principal_name = var.user_principal_name
  display_name        = "baseline-user"
  mail_nickname       = "baseline-user"
  password            = var.user_password
  force_password_change = false
}

data "azuread_directory_role" "cloud_admin" {
  display_name = "Cloud Administrator"
}

data "azuread_directory_role" "app_admin" {
  display_name = "Application Administrator"
}

data "azuread_directory_role" "exchange_admin" {
  display_name = "Exchange Administrator"
}

resource "azuread_directory_role_member" "cloud_admin" {
  role_object_id  = data.azuread_directory_role.cloud_admin.id
  member_object_id = azuread_user.baseline.id
}

resource "azuread_directory_role_member" "app_admin" {
  role_object_id  = data.azuread_directory_role.app_admin.id
  member_object_id = azuread_user.baseline.id
}

resource "azuread_directory_role_member" "exchange_admin" {
  role_object_id  = data.azuread_directory_role.exchange_admin.id
  member_object_id = azuread_user.baseline.id
}

resource "azurerm_log_analytics_workspace" "baseline" {
  name                = var.log_analytics_workspace_name
  location            = var.location
  resource_group_name = var.resource_group_name
  sku                 = "PerGB2018"
  retention_in_days   = 30
}

data "azurerm_subscription" "current" {}

resource "azurerm_monitor_diagnostic_setting" "subscription" {
  name               = "baseline-activity-logs"
  target_resource_id = data.azurerm_subscription.current.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.baseline.id

  dynamic "log" {
    for_each = [
      "Administrative",
      "Security",
      "ServiceHealth",
      "Alert",
      "Recommendation",
      "Policy",
      "Autoscale",
      "ResourceHealth"
    ]
    content {
      category = log.value
      enabled  = true
      retention_policy {
        enabled = false
      }
    }
  }
}
