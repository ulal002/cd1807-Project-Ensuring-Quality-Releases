output "rg_name_value" {
  value = module.network.resource_group_name
}
output "subnet_id_test" {
  value = "${azurerm_subnet.test.id}"
}
