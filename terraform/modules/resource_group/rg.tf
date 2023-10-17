resource "azurerm_resource_group" "Udacity-Urvesh" {
  name     = "${var.resource_group}"
  location = "${var.location}"
}
