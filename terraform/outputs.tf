output "baseline_user_object_id" {
  value = azuread_user.baseline.object_id
}

output "log_analytics_workspace_id" {
  value = azurerm_log_analytics_workspace.baseline.id
}
