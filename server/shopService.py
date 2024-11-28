from .utils import make_rest_call, extract_jwt_from_context
from generated import workshop_pb2, workshop_pb2_grpc
import os
CRAPI_BASE_URL = os.getenv("CRAPI_BASE_URL", "http://localhost:8888")  # Default to localhost

class ShopService(workshop_pb2_grpc.ShopServiceServicer):

    def GetProducts(self, request, context):
        """Get products for the shop"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)
        
        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/products"
        return make_rest_call(
            url=url,
            payload={},  # No payload needed for this GET request
            context=context,
            grpc_response_type=workshop_pb2.ProductResponse,
            method='GET',
            headers=headers
        )

    def AddNewProduct(self, request, context):
        """Add a new product to the shop"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the product data to be added
        product_data = {
            "name": request.name,
            "price": request.price,
            "image_url": request.image_url
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/products"
        return make_rest_call(
            url=url,
            payload=product_data,
            context=context,
            grpc_response_type=workshop_pb2.Product,
            method='POST',
            headers=headers
        )

    def CreateOrder(self, request, context):
        """Create an order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the order data
        order_data = {
            "product_id": request.product_id,
            "quantity": request.quantity
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/orders"
        return make_rest_call(
            url=url,
            payload=order_data,
            context=context,
            grpc_response_type=workshop_pb2.OrderResponse,
            method='POST',
            headers=headers
        )

    def UpdateOrder(self, request, context):
        """Update an existing order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the order update data
        order_data = {
            "status": request.status,
            "quantity": request.quantity
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/orders/{request.order_id}"
        return make_rest_call(
            url=url,
            payload=order_data,
            context=context,
            grpc_response_type=workshop_pb2.UpdateOrderResponse,
            method='PUT',
            headers=headers
        )

    def GetOrderByID(self, request, context):
        """Get order details by ID"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/orders/{request.order_id}"
        return make_rest_call(
            url=url,
            payload={},  # No payload needed for this GET request
            context=context,
            grpc_response_type=workshop_pb2.GetOrderResponse,
            method='GET',
            headers=headers
        )

    def GetOrders(self, request, context):
        """Get a list of past orders"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/orders/all?limit={request.limit}&offset={request.offset}"
        return make_rest_call(
            url=url,
            payload={},  # No payload needed for this GET request
            context=context,
            grpc_response_type=workshop_pb2.OrdersResponse,
            method='GET',
            headers=headers
        )

    def ReturnOrder(self, request, context):
        """Return an order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the return order data
        return_order_data = {
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/orders/return_order?order_id={request.order_id}"
        return make_rest_call(
            url=url,
            payload=return_order_data,
            context=context,
            grpc_response_type=workshop_pb2.ReturnOrderResponse,
            method='POST',
            headers=headers
        )

    def ApplyCoupon(self, request, context):
        """Apply coupon to the current order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the coupon data
        coupon_data = {
            "coupon_code": request.coupon_code,
            "amount": request.amount,
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/apply_coupon"
        return make_rest_call(
            url=url,
            payload=coupon_data,
            context=context,
            grpc_response_type=workshop_pb2.ApplyCouponResponse,
            method='POST',
            headers=headers
        )

    def GetQRCode(self, request, context):
        """Get QR code for returning an order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/shop/return_qr_code"
        return make_rest_call(
            url=url,
            payload={},  # No payload needed for this GET request
            context=context,
            grpc_response_type=workshop_pb2.QRCode,
            method='GET',
            headers=headers
        )

    def GetAllUsers(self, request, context):
        """Get QR code for returning an order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/management/users/all"
        return make_rest_call(
            url=url,
            payload={},  # No payload needed for this GET request
            context=context,
            grpc_response_type=workshop_pb2.Users,
            method='GET',
            headers=headers
        )
    
    def GetAllMechanics(self, request, context):
        """Get QR code for returning an order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/mechanic/"
        return make_rest_call(
            url=url,
            payload={},  # No payload needed for this GET request
            context=context,
            grpc_response_type=workshop_pb2.Mechanics,
            method='GET',
            headers=headers
        )
    
    def ContactMechanic(self, request, context):
        """Apply coupon to the current order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the coupon data
        data = {
            "number_of_repeats": request.number_of_repeats,
            "mechanic_api": request.mechanic_api,
            "vin": request.vin,
            "repeat_request_if_failed": request.repeat_request_if_failed,
            "problem_details": request.problem_details,
            "mechanic_code": request.mechanic_code,
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/merchant/contact_mechanic"
        return make_rest_call(
            url=url,
            payload=data,
            context=context,
            grpc_response_type=workshop_pb2.ContactMechanicResponse,
            method='POST',
            headers=headers
        )

    def GetMechanicReportById(self, request, context):
        """Apply coupon to the current order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the coupon data
        data = {
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/mechanic/mechanic_report?report_id={request.id}"
        return make_rest_call(
            url=url,
            payload=data,
            context=context,
            grpc_response_type=workshop_pb2.MechanicReport,
            method='GET',
            headers=headers
        )
    

    def CreateServiceReport(self, request, context):
        """Apply coupon to the current order"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the coupon data
        data = {
            "mechanic_code":request.mechanic_code,
            "problem_details": request.mechanic_code,
            "vin":request.vin,
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/mechanic/receive_report"
        return make_rest_call(
            url=url,
            payload=data,
            context=context,
            grpc_response_type=workshop_pb2.CreateServiceReportResponse,
            method='GET',
            headers=headers
        )
    
    def MechanicSignUp(self, request, context):
        """Apply coupon to the current order"""

        # Prepare the coupon data
        data = {
            "name": request.name,
            "email": request.email,
            "number": request.number,
            "password": request.password,
            "mechanic_code": request.mechanic_code,
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/mechanic/signup"
        return make_rest_call(
            url=url,
            payload=data,
            context=context,
            grpc_response_type=workshop_pb2.Message,
            method='POST',
            headers=None
        )
    
    def ServiceRequests(self, request, context):
        """Get a list of past orders"""
        # Extract JWT token from the gRPC context
        jwt_token = extract_jwt_from_context(context)

        # Set up headers for the REST API request
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call the make_rest_call function to make a REST API call
        url = f"{CRAPI_BASE_URL}/workshop/api/mechanic/service_requests?limit={request.limit}&offset={request.offset}"
        return make_rest_call(
            url=url,
            payload={},  # No payload needed for this GET request
            context=context,
            grpc_response_type=workshop_pb2.ServiceRequestsResponse,
            method='GET',
            headers=headers
        )
    
    
