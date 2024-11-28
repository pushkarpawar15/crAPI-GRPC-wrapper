import grpc
import os
from dotenv import load_dotenv
from generated import community_pb2, community_pb2_grpc
from .utils import make_rest_call,extract_jwt_from_context

# Load environment variables from .env file
load_dotenv()
CRAPI_BASE_URL = os.getenv("CRAPI_BASE_URL", "http://localhost:8888")  # Default to localhost

class CommunityService(community_pb2_grpc.CommunityServiceServicer):
    def GetPost(self, request, context):
        """Get a specific post in the forum"""
        get_post_url = f"{CRAPI_BASE_URL}/community/api/v2/community/posts/{request.postId}"
        headers = {
            "Authorization": f"Bearer {extract_jwt_from_context(context)}"
        }

        # Make the REST API call
        return make_rest_call(
            url=get_post_url,
            payload={},  # No payload, postId is passed in the URL
            context=context,
            grpc_response_type=community_pb2.Post,
            method='GET',
            headers=headers
    )


    def CreatePost(self, request, context):
        """Create a new post in the forum"""
        create_post_url = f"{CRAPI_BASE_URL}/community/api/v2/community/posts"
        payload = {
            "title": request.title,
            "content": request.content,
        }
        headers = {
            "Authorization": f"Bearer {extract_jwt_from_context(context)}"
        }

        # Make the REST API call
        return make_rest_call(
            url=create_post_url,
            payload=payload,
            context=context,
            grpc_response_type=community_pb2.CreatePostResponse,
            method='POST',
            headers=headers
        )
    
    def PostComment(self, request, context):
        """Add a comment to an existing post in the forum"""
        post_comment_url = f"{CRAPI_BASE_URL}/community/api/v2/community/posts/{request.postId}/comment"
        headers = {
            "Authorization": f"Bearer {extract_jwt_from_context(context)}"
        }
        payload = {
            "content": request.content  # The comment content
        }

        # Make the REST API call
        return make_rest_call(
            url=post_comment_url,
            payload=payload,
            context=context,
            grpc_response_type=community_pb2.PostWithComments,
            method='POST',
            headers=headers
        )
    
    def GetRecentPosts(self, request, context):
        """Fetch the most recent posts in the forum."""
        get_recent_posts_url = f"{CRAPI_BASE_URL}/community/api/v2/community/posts/recent"
        headers = {
            "Authorization": f"Bearer {extract_jwt_from_context(context)}"
        }
        params = {
            "limit": request.limit,
            "offset": request.offset
        }

        # Make the REST API call
        return make_rest_call(
            url=get_recent_posts_url,
            payload=params,  # Pass limit and offset as query parameters
            context=context,
            grpc_response_type=community_pb2.RecentPostsResponse,
            method='GET',
            headers=headers
        )
    
    def AddNewCoupon(self, request, context):
        """Add a new coupon to the shop database."""
        add_coupon_url = f"{CRAPI_BASE_URL}/community/api/v2/coupon/new-coupon"
        headers = {
            "Authorization": f"Bearer {extract_jwt_from_context(context)}"
        }
        payload = {
            "coupon_code": request.coupon_code,
            "description": request.description,
            "discount": request.discount,
            "expiryDate": request.expiryDate
        }

        # Make the REST API call
        return make_rest_call(
            url=add_coupon_url,
            payload=payload,
            context=context,
            grpc_response_type=community_pb2.AddCouponResponse,
            method='POST',
            headers=headers
        )
    
    def ValidateCoupon(self, request, context):
        """Validate the provided discount coupon code."""
        validate_coupon_url = f"{CRAPI_BASE_URL}/community/api/v2/coupon/validate-coupon"
        headers = {
            "Authorization": f"Bearer {extract_jwt_from_context(context)}"
        }
        payload = {
            "coupon_code": request.coupon_code
        }

        # Make the REST API call
        return make_rest_call(
            url=validate_coupon_url,
            payload=payload,
            context=context,
            grpc_response_type=community_pb2.ValidateCouponResponse,
            method='POST',
            headers=headers
    )





