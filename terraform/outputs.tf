output "user_object_id" {
  description = "Object ID of the baseline user"
  value       = azuread_user.baseline.id
}

output "role_ids" {
  description = "IDs of the assigned directory roles"
  value = {
    cloud_administrator       = data.azuread_directory_role.cloud_admin.id
    application_administrator = data.azuread_directory_role.app_admin.id
    exchange_administrator    = data.azuread_directory_role.exchange_admin.id
  }
}
