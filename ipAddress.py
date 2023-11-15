import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python public_ip_address_create_customized_values.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    load_dotenv()

    subscription_id=os.getenv("298f8fe6-924c-4eaf-bbf6-eb25e12d5ead")
    resource_group_name=os.getenv("lab4_2")
    nic=os.getenv("NIC")
    public_ip_address_name=os.getenv("Test")
    location=os.getenv("West Europe")

    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="298f8fe6-924c-4eaf-bbf6-eb25e12d5ead",
    )

    response = client.public_ip_addresses.begin_create_or_update(
        resource_group_name="lab4_2",
        public_ip_address_name="Test",
        parameters={
            "location": f"{location}",
            "properties": {
                "idleTimeoutInMinutes": 10,
                "publicIPAddressVersion": "IPv4",
                "publicIPAllocationMethod": "Static",
            },
            "sku": {"name": "Standard", "tier": "Regional"},
        }, # type: ignore
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-05-01/examples/PublicIpAddressCreateCustomizedValues.json
if __name__ == "__main__":
    main()