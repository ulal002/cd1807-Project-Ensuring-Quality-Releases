resource "azurerm_virtual_network" "flask-webappP3-NET" {
  name                 = "${var.application_type}-${var.resource_type}"
  address_space        = "${var.address_space}"
  location             = "${var.location}"
  resource_group_name  = "${var.resource_group}"
}
resource "azurerm_subnet" "flask-webappP3-NET-sub" {
  name                 = "${var.application_type}-${var.resource_type}-sub"
  resource_group_name  = "${var.resource_group}"
  virtual_network_name = "${azurerm_virtual_network.flask-webappP3-NET}"
  address_prefix       = "${var.address_prefix_test}"
}
