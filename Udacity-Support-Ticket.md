##Error##
<img width="1725" alt="image" src="https://github.com/ulal002/cd1807-Project-Ensuring-Quality-Releases/assets/139964364/a8c59caf-52e6-4d93-9271-2dbe0b2f7967">

##Logs##
2023-10-20T08:56:20.1877598Z ##[section]Starting: Terraform apply
2023-10-20T08:56:20.1884559Z ==============================================================================
2023-10-20T08:56:20.1884904Z Task         : Terraform
2023-10-20T08:56:20.1885093Z Description  : Execute terraform commands to manage resources on AzureRM, Amazon Web Services(AWS) and Google Cloud Platform(GCP)
2023-10-20T08:56:20.1885328Z Version      : 3.209.24
2023-10-20T08:56:20.1885508Z Author       : Microsoft Corporation
2023-10-20T08:56:20.1885638Z Help         : [Learn more about this task](https://aka.ms/AAf0uqr)
2023-10-20T08:56:20.1885860Z ==============================================================================
2023-10-20T08:56:21.9985644Z [command]/home/urvesh/myagent/_work/_tool/terraform/1.2.9/x64/terraform providers
2023-10-20T08:56:27.2265061Z 
2023-10-20T08:56:27.2609413Z Providers required by configuration:
2023-10-20T08:56:27.2610578Z .
2023-10-20T08:56:27.3094202Z ├── provider[registry.terraform.io/hashicorp/azurerm]
2023-10-20T08:56:27.3095406Z ├── module.publicip
2023-10-20T08:56:27.3095829Z │   └── provider[registry.terraform.io/hashicorp/azurerm]
2023-10-20T08:56:27.3096178Z ├── module.resource_group
2023-10-20T08:56:27.3096663Z │   └── provider[registry.terraform.io/hashicorp/azurerm]
2023-10-20T08:56:27.3097016Z ├── module.appservice
2023-10-20T08:56:27.3097386Z │   └── provider[registry.terraform.io/hashicorp/azurerm]
2023-10-20T08:56:27.3097709Z ├── module.network
2023-10-20T08:56:27.3098073Z │   └── provider[registry.terraform.io/hashicorp/azurerm]
2023-10-20T08:56:27.3098394Z └── module.nsg-test
2023-10-20T08:56:27.3098760Z     └── provider[registry.terraform.io/hashicorp/azurerm]
2023-10-20T08:56:27.3098908Z 
2023-10-20T08:56:27.3628777Z [command]/home/urvesh/myagent/_work/_tool/terraform/1.2.9/x64/terraform apply -auto-approve
2023-10-20T08:56:41.7188704Z [31m╷[0m[0m
2023-10-20T08:56:41.7201105Z [31m│[0m [0m[1m[31mError: [0m[0m[1mInvalid value for input variable[0m
2023-10-20T08:56:41.7201604Z [31m│[0m [0m
2023-10-20T08:56:41.7202896Z [31m│[0m [0m[0m  on main.tf line 38, in module "nsg-test":
2023-10-20T08:56:41.7204337Z [31m│[0m [0m  38:   resource_group_name   = [4mmodule.resource_group.resource_group_name[0m[0m
2023-10-20T08:56:41.7204724Z [31m│[0m [0m
2023-10-20T08:56:41.7637607Z [31m│[0m [0mThe given value is not suitable for module.nsg-test.var.resource_group_name
2023-10-20T08:56:41.7644688Z [31m│[0m [0mdeclared at ../../modules/networksecuritygroup/input.tf:5,1-31: string
2023-10-20T08:56:41.7645351Z [31m│[0m [0mrequired.
2023-10-20T08:56:41.7646126Z [31m╵[0m[0m
2023-10-20T08:56:41.7646457Z [31m╷[0m[0m
2023-10-20T08:56:41.7646867Z [31m│[0m [0m[1m[31mError: [0m[0m[1mInvalid value for input variable[0m
2023-10-20T08:56:41.7647224Z [31m│[0m [0m
2023-10-20T08:56:41.7647674Z [31m│[0m [0m[0m  on main.tf line 54, in module "publicip":
2023-10-20T08:56:41.7665788Z [31m│[0m [0m  54:   resource_group_name   = [4mmodule.resource_group.resource_group_name[0m[0m
2023-10-20T08:56:41.7666792Z [31m│[0m [0m
2023-10-20T08:56:41.7668423Z [31m│[0m [0mThe given value is not suitable for module.publicip.var.resource_group_name
2023-10-20T08:56:41.7669016Z [31m│[0m [0mdeclared at ../../modules/publicip/input.tf:3,1-31: string required.
2023-10-20T08:56:41.7669777Z [31m╵[0m[0m
2023-10-20T08:56:41.7670067Z [31m╷[0m[0m
2023-10-20T08:56:41.7672026Z [31m│[0m [0m[1m[31mError: [0m[0m[1mIncorrect attribute value type[0m
2023-10-20T08:56:41.7672392Z [31m│[0m [0m
2023-10-20T08:56:41.7672852Z [31m│[0m [0m[0m  on ../../modules/appservice/appservice.tf line 4, in resource "azurerm_service_plan" "test":
2023-10-20T08:56:41.7673341Z [31m│[0m [0m   4:   resource_group_name = [4mvar.resource_group_name[0m[0m
2023-10-20T08:56:41.7673757Z [31m│[0m [0m    [90m├────────────────[0m
2023-10-20T08:56:41.7674201Z [31m│[0m [0m[0m    [90m│[0m [1mvar.resource_group_name[0m is object with 6 attributes
2023-10-20T08:56:41.8169782Z [31m│[0m [0m[0m
2023-10-20T08:56:41.8170742Z [31m│[0m [0mInappropriate value for attribute "resource_group_name": string required.
2023-10-20T08:56:41.8171314Z [31m╵[0m[0m
2023-10-20T08:56:41.8171627Z [31m╷[0m[0m
2023-10-20T08:56:41.8172130Z [31m│[0m [0m[1m[31mError: [0m[0m[1mIncorrect attribute value type[0m
2023-10-20T08:56:41.8172494Z [31m│[0m [0m
2023-10-20T08:56:41.8173047Z [31m│[0m [0m[0m  on ../../modules/network/network.tf line 5, in resource "azurerm_virtual_network" "test":
2023-10-20T08:56:41.8173711Z [31m│[0m [0m   5:   resource_group_name  = [4mvar.resource_group_name[0m[0m
2023-10-20T08:56:41.8174147Z [31m│[0m [0m    [90m├────────────────[0m
2023-10-20T08:56:41.8174693Z [31m│[0m [0m[0m    [90m│[0m [1mvar.resource_group_name[0m is object with 6 attributes
2023-10-20T08:56:41.8175155Z [31m│[0m [0m[0m
2023-10-20T08:56:41.8175597Z [31m│[0m [0mInappropriate value for attribute "resource_group_name": string required.
2023-10-20T08:56:41.8176501Z [31m╵[0m[0m
2023-10-20T08:56:42.7419229Z ##[error]Error: The process '/home/urvesh/myagent/_work/_tool/terraform/1.2.9/x64/terraform' failed with exit code 1
2023-10-20T08:56:42.7476530Z ##[section]Finishing: Terraform apply
