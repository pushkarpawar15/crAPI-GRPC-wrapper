import grpc
import requests
def make_rest_call( url, payload, context, grpc_response_type,method='POST',headers=None,files=None):
    print(method,"Call to url",url)
    """Helper method to make REST calls and map responses to gRPC."""
    try:
        if method == 'POST':
            response = requests.post(url, json=payload, headers=headers,files=files)
        elif method == 'GET':
            response = requests.get(url, params=payload, headers=headers)
        elif method == 'PUT':
            response = requests.put(url, json=payload, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, json=payload, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        if response.status_code == 200:
            data = response.json()
            print(data)
            grpc_response = grpc_response_type()

            if isinstance(data, dict):
                print("boject ka mamla")
                map_dict_to_grpc(data,grpc_response)

            elif isinstance(data, list):
                print("list ka mamla hai")
                for item in data:
                    repeated_field = grpc_response.items.add()
                    map_dict_to_grpc(item, repeated_field)
            return grpc_response

        else:
            http_to_grpc_status = {
                400: grpc.StatusCode.INVALID_ARGUMENT,
                401: grpc.StatusCode.UNAUTHENTICATED,
                403: grpc.StatusCode.PERMISSION_DENIED,
                404: grpc.StatusCode.NOT_FOUND,
                409: grpc.StatusCode.ALREADY_EXISTS,
                429: grpc.StatusCode.RESOURCE_EXHAUSTED,
                499: grpc.StatusCode.CANCELLED,
                500: grpc.StatusCode.INTERNAL,
                501: grpc.StatusCode.UNIMPLEMENTED,
                503: grpc.StatusCode.UNAVAILABLE,
                504: grpc.StatusCode.DEADLINE_EXCEEDED
            }
            grpc_status = http_to_grpc_status.get(response.status_code, grpc.StatusCode.UNKNOWN)
            error_message = f"REST API error: {response.status_code} {response.text}"
            
            # Log the error message for debugging
            print(error_message)
            
            # Set gRPC context with the appropriate status and details
            context.set_code(grpc_status)
            context.set_details(error_message)
            return grpc_response_type()
    except Exception as e:
        context.set_code(grpc.StatusCode.INTERNAL)
        context.set_details(f"Error calling REST API: {str(e)}")
        return grpc_response_type()

# def map_dict_to_grpc( data, grpc_response):
#     """Helper function to map a dictionary to a gRPC response message."""
#     # Iterate through dictionary keys and set corresponding gRPC message fields
#     for key, value in data.items():
#         # If it's a repeated field, handle adding items to it
#         if isinstance(value, list) and hasattr(grpc_response, key):
#             print("list hai")
#             for item in value:
#                 # Add new item to the repeated field
#                 repeated_field = getattr(grpc_response, key)
#                 if hasattr(repeated_field, "add"):
#                     # It's a repeated field; add() is safe to use
#                     print(f"Field '{key}' is a repeated field. Using add(). with value {item}")
#                 else:
#                     print(f"Field '{key}' is not repeated. Cannot use add().")
#                 repeated_item = repeated_field.add()  
#                 map_dict_to_grpc(item, repeated_item)  # Recursively map the item fields

#         # For non-repeated fields, set the value directly
#         elif hasattr(grpc_response, key):
#             if isinstance(value, dict):
#                 # Handle nested messages explicitly
#                 nested_message = getattr(grpc_response, key)
#                 map_dict_to_grpc(value, nested_message)  # Recursively map to the nested message
#             else:
#                 # For basic fields, just set the value
#                 if key and value:
#                     setattr(grpc_response, key, value)

def map_dict_to_grpc(data, grpc_response):
    """
    Helper function to map a dictionary to a gRPC response message.
    Maps dictionary fields to the corresponding gRPC response fields.
    """
    for key, value in data.items():
        # print(f"key is {key} for value {value}")
        # Check if the field exists in the gRPC response
        if hasattr(grpc_response, key):
            grpc_field = getattr(grpc_response, key)

            # Handle repeated fields
            if isinstance(value, list):
                # print(f"key is {key} for value {value}")
                if len(value) == 0:
                    continue
                elif hasattr(grpc_field, "add"):
                    print(f"{key} and {value}")
                    for item in value:
                        # Add a new item to the repeated field
                        repeated_item = grpc_field.add()
                        # Recursively map the dictionary to the repeated item
                        map_dict_to_grpc(item, repeated_item)
                else:
                    raise TypeError(f"Field '{key}' is not a repeated field.")
            
            # Handle nested fields (dict)
            elif isinstance(value, dict):
                map_dict_to_grpc(value, grpc_field)
            
            # Handle basic scalar fields
            else:
                if value is not None:  # Skip None values
                    try:
                        setattr(grpc_response, key, value)
                    except TypeError as e:
                        print(f"Error setting field '{key}': {e}")
        else:
            # Warn if the key is not found in the gRPC message
            print(f"Field '{key}' not found in gRPC response.")


def extract_jwt_from_context(context):
    """Extract JWT token from gRPC metadata"""
    metadata = dict(context.invocation_metadata())
    jwt_token = metadata.get('authorization', '').split('Bearer ')[-1]
    if not jwt_token:
        context.set_code(grpc.StatusCode.UNAUTHENTICATED)
        context.set_details("Authorization token is missing or invalid")
    return jwt_token
