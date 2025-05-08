import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def list_ec2_regions():
    """
    Retrieves and lists all available AWS EC2 regions

    This function retrieves the list of EC2 regions
    and prints each region's name. It also includes error handling for
    common AWS authentication and connection issues
    """
    try:
        # Create an EC2 client
        # Describing regions is a global API call
        ec2_client = boto3.client('ec2')

        # Retrieve all regions that are opted-in or opt-in-not-required
        response = ec2_client.describe_regions(AllRegions=False) # Set to True to see all possible regions including those not opted-in

        print("Available AWS EC2 Regions:")
        if 'Regions' in response:
            for region in response['Regions']:
                print(f"- {region['RegionName']}")
        else:
            print("No regions found or an error occurred.")

    except NoCredentialsError:
        print("AWS credentials not found.")
    except ClientError as e:
        error_code = e.response.get('Error', {}).get('Code')
        error_message = e.response.get('Error', {}).get('Message')
        if error_code == 'AuthFailure':
            print(f"AWS Authentication Failure: {error_message}")
        else:
            print(f"An AWS client error occurred: {e}")
            print("This could be due to network issues, service unavailability or invalid request parameters.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    list_ec2_regions()
