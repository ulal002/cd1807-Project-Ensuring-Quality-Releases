output "resource_group_name" {
  value = azurerm_resource_group.Udacity-Urvesh-Test
}
output "subnet_id_test" {
  value = "${azurerm_subnet.test.id}"
}
