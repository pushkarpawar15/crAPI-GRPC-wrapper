import grpc
import os
from dotenv import load_dotenv
from generated import identity_pb2, identity_pb2_grpc
from .utils import make_rest_call,extract_jwt_from_context
# Load environment variables from .env file
load_dotenv()
CRAPI_BASE_URL = os.getenv("CRAPI_BASE_URL", "http://localhost:8888")  # Default to localhost

class IdentityService(identity_pb2_grpc.IdentityServiceServicer):
    def Signup(self, request, context):
        signup_url = f"{CRAPI_BASE_URL}/identity/api/auth/signup"
        payload = {
            "email": request.email,
            "name": request.name,
            "number": request.number,
            "password": request.password,
        }
        return make_rest_call(signup_url, payload, context, identity_pb2.SignupResponse)

    def Login(self, request, context):
        login_url = f"{CRAPI_BASE_URL}/identity/api/auth/login"
        payload = {
            "email": request.email,
            "password": request.password,
        }
        return make_rest_call(login_url, payload, context, identity_pb2.LoginResponse)

    def ForgotPassword(self, request, context):
        forgot_password_url = f"{CRAPI_BASE_URL}/identity/api/auth/forget-password"
        payload = {
            "email": request.email,
        }
        return make_rest_call(forgot_password_url, payload, context, identity_pb2.ForgotPasswordResponse)

    def CheckOTPv3(self, request, context):
        """Check OTP - Version 3"""
        check_otp_v3_url = f"{CRAPI_BASE_URL}/identity/api/auth/v3/check-otp"
        payload = {
            "otp": request.otp,
            "email": request.email,
            "password": request.password,
        }
        return make_rest_call(check_otp_v3_url, payload, context, identity_pb2.CheckOTPResponse)

    def CheckOTPv2(self, request, context):
        """Check OTP - Version 3"""
        check_otp_v3_url = f"{CRAPI_BASE_URL}/identity/api/auth/v2/check-otp"
        payload = {
            "otp": request.otp,
            "email": request.email,
            "password": request.password,
        }
        return make_rest_call(check_otp_v3_url, payload, context, identity_pb2.CheckOTPResponse)
    

    def ResetPassword(self, request, context):
        reset_password_url = f"{CRAPI_BASE_URL}/identity/api/auth/reset-password"
        payload = {
            "email": request.email,
            "password": request.password,
        }
        return make_rest_call(reset_password_url, payload, context, identity_pb2.ResetPasswordResponse)


    def VerifyEmailToken(self, request, context):
        verify_email_token_url = f"{CRAPI_BASE_URL}/identity/api/auth/verify-email-token"
        payload = {
            "old_email": request.old_email,
            "new_email": request.new_email,
            "token": request.token,
        }
        return make_rest_call(verify_email_token_url, payload, context, identity_pb2.VerifyEmailTokenResponse)

    def LoginWithTokenv4(self, request, context):
        """Login with Email Token"""
        login_with_token_url = f"{CRAPI_BASE_URL}/identity/api/auth/v4.0/user/login-with-token"
        payload = {
            "email": request.email,
            "token": request.token,
        }
        return make_rest_call(login_with_token_url, payload, context, identity_pb2.LoginResponse)
    
    def LoginWithTokenv2(self, request, context):
        """Login with Email Token"""
        login_with_token_url = f"{CRAPI_BASE_URL}/identity/api/auth/v2.7/user/login-with-token"
        payload = {
            "email": request.email,
            "token": request.token,
        }
        return make_rest_call(login_with_token_url, payload, context, identity_pb2.LoginResponse)

    def ResetPassword(self, request, context):
        """Reset Password using JWT token"""
        reset_password_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/reset-password"
        payload = {
            "email": request.email,
            "password": request.password,
        }
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call _make_rest_call with headers
        return make_rest_call(
            url=reset_password_url,
            payload=payload,
            context=context,
            grpc_response_type=identity_pb2.ResetPasswordResponse,
            headers=headers
        )

    def ChangeEmail(self, request, context):
        """Change user email"""
        change_email_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/change-email"
        payload = {
            "new_email": request.new_email,
            "old_email": request.old_email,
        }
        jwt_token = extract_jwt_from_context(context)

        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call _make_rest_call with headers
        return make_rest_call(
            url=change_email_url,
            payload=payload,
            context=context,
            grpc_response_type=identity_pb2.ChangeEmailResponse,
            method='POST',
            headers=headers
        )
    
    def VerifyEmailToken(self, request, context):
        """Verify Email Token"""
        verify_email_token_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/verify-email-token"
        payload = {
            "old_email": request.old_email,
            "new_email": request.new_email,
            "token": request.token,
        }
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call _make_rest_call with headers
        return make_rest_call(
            url=verify_email_token_url,
            payload=payload,
            context=context,
            grpc_response_type=identity_pb2.VerifyEmailTokenResponse,
            headers=headers
        )

    def GetDashboard(self, request, context):
        """Get user dashboard data"""
        get_dashboard_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/dashboard"
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        
        return make_rest_call(
            url=get_dashboard_url,
            payload={},  # GET request often doesn't need a payload
            context=context,
            grpc_response_type=identity_pb2.GetDashboardResponse,
            method='GET',
            headers=headers
        )

    def UploadProfileVideo(self, request, context):
        """Upload user profile video"""
        upload_profile_video_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/videos"
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the files for upload
        files = {
            "file": request.file  # The binary video file from the request
        }

        # Make the REST API call using the updated _make_rest_call function
        return make_rest_call(
            url=upload_profile_video_url,
            payload={},  # No JSON payload, file is sent as part of the 'files' parameter
            context=context,
            grpc_response_type=identity_pb2.ProfileVideo,
            method='POST',  # Using POST method for file upload
            headers=headers,
            files=files
        )
    
    def UpdateProfilePic(self, request, context):
        """Upload user profile video"""
        upload_profile_video_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/pictures"
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Prepare the files for upload
        files = {
            "file": request.file  # The binary video file from the request
        }

        # Make the REST API call using the updated _make_rest_call function
        return make_rest_call(
            url=upload_profile_video_url,
            payload={},  # No JSON payload, file is sent as part of the 'files' parameter
            context=context,
            grpc_response_type=identity_pb2.UpdateProfilePicResponse,
            method='POST',  # Using POST method for file upload
            headers=headers,
            files=files
        )

    def GetProfileVideo(self, request, context):
        """Get user profile video"""
        get_profile_video_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/videos/{request.video_id}"
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call _make_rest_call for GET request
        return make_rest_call(
            url=get_profile_video_url,
            payload={},  # No payload, video_id is passed as part of the URL
            context=context,
            grpc_response_type=identity_pb2.ProfileVideo,
            method='GET',
            headers=headers
        )

    def UpdateProfileVideo(self, request, context):
        """Update user profile video"""
        update_profile_video_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/videos/{request.video_id}"
        payload = {
            "video_name": request.video_name,  # Assuming video name can be updated
        }
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call _make_rest_call for PUT request
        return make_rest_call(
            url=update_profile_video_url,
            payload=payload,
            context=context,
            grpc_response_type=identity_pb2.ProfileVideo,
            method='PUT',
            headers=headers
        )

    def DeleteProfileVideo(self, request, context):
        """Delete user profile video"""
        delete_profile_video_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/videos/{request.video_id}"
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Call _make_rest_call for DELETE request
        return make_rest_call(
            url=delete_profile_video_url,
            payload={},  # No payload, video_id is passed as part of the URL
            context=context,
            grpc_response_type=identity_pb2.DeleteResponse,
            method='DELETE',
            headers=headers
        )

    def ConvertProfileVideo(self, request, context):
        """Convert profile video format"""
        convert_video_url = f"{CRAPI_BASE_URL}/identity/api/v2/user/videos/convert_video"
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        params = {
            "video_id": request.video_id
        }

        # Make the REST API call
        return make_rest_call(
            url=convert_video_url,
            payload=params,  # Video ID passed as query parameter
            context=context,
            grpc_response_type=identity_pb2.ConvertProfileVideoResponse,
            method='GET',
            headers=headers
        )

    def AdminDeleteProfileVideo(self, request, context):
        """Admin delete profile video"""
        delete_profile_video_url = f"{CRAPI_BASE_URL}/identity/api/v2/admin/videos/{request.video_id}"
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Make the REST API call
        return make_rest_call(
            url=delete_profile_video_url,
            payload={},  # No payload, video_id is passed as part of the URL
            context=context,
            grpc_response_type=identity_pb2.CRAPIResponse,
            method='DELETE',
            headers=headers
        )

    def GetUserVehicles(self, request, context):
        """Get all user vehicles"""
        get_vehicles_url = f"{CRAPI_BASE_URL}/identity/api/v2/vehicle/vehicles"
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Make the REST API call
        return make_rest_call(
            url=get_vehicles_url,
            payload={},  # No payload needed
            context=context,
            grpc_response_type=identity_pb2.GetUserVehiclesResponse,
            method='GET',
            headers=headers
        )

    def AddVehicle(self, request, context):
        """Add a vehicle for the user"""
        add_vehicle_url = f"{CRAPI_BASE_URL}/identity/api/v2/vehicle/add_vehicle"
        payload = {
            "pincode": request.pincode,
            "vin": request.vin
        }
        jwt_token = extract_jwt_from_context(context)


        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Make the REST API call
        return make_rest_call(
            url=add_vehicle_url,
            payload=payload,
            context=context,
            grpc_response_type=identity_pb2.CRAPIResponse,
            method='POST',
            headers=headers
        )

    def GetVehicleLocation(self, request, context):
        """Get user's vehicle location"""
        get_vehicle_location_url = f"{CRAPI_BASE_URL}/identity/api/v2/vehicle/{request.vehicleId}/location"
        jwt_token = extract_jwt_from_context(context)


        print(jwt_token)
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Make the REST API call
        return make_rest_call(
            url=get_vehicle_location_url,
            payload={},  # No payload, vehicleId passed in URL
            context=context,
            grpc_response_type=identity_pb2.GetVehicleLocationResponse,
            method='GET',
            headers=headers
        )

    def ResendVehicleDetailsEmail(self, request, context):
        """Resend vehicle details email to the user"""
        resend_vehicle_details_email_url = f"{CRAPI_BASE_URL}/identity/api/v2/vehicle/resend_email"
        metadata = dict(context.invocation_metadata())
        jwt_token = metadata.get('authorization', '').split('Bearer ')[-1]  # Extract the token
        if not jwt_token:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Authorization token is missing or invalid")
            return identity_pb2.GetVehicleLocationResponse()  # Return an empty response in case of missing token

        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }

        # Make the REST API call
        return make_rest_call(
            url=resend_vehicle_details_email_url,
            payload={},  # No payload, resend request
            context=context,
            grpc_response_type=identity_pb2.CRAPIResponse,
            method='POST',
            headers=headers
        )


