output "rg_name_value" {
  value = module.resource_group.resource_group_name
}
output "subnet_id_test" {
  value = "${azurerm_subnet.test.id}"
}
