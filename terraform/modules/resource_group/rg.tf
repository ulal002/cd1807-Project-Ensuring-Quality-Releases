resource "azurerm_resource_group_name" "Udacity-Urvesh" {
  name     = "${var.resource_group}"
  location = "${var.location}"
}
