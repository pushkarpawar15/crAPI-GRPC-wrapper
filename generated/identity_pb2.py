# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: identity.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'identity.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eidentity.proto\x12\x08identity\"N\n\rSignupRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"!\n\x0eSignupResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"R\n\rLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x13\n\x0bmfaRequired\x18\x04 \x01(\x08\"&\n\x15\x46orgotPasswordRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\")\n\x16\x46orgotPasswordResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"?\n\x0f\x43heckOTPRequest\x12\x0b\n\x03otp\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"#\n\x10\x43heckOTPResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"N\n\x17VerifyEmailTokenRequest\x12\x11\n\told_email\x18\x01 \x01(\t\x12\x11\n\tnew_email\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"+\n\x18VerifyEmailTokenResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"5\n\x15LoginWithTokenRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"7\n\x14ResetPasswordRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"8\n\x15ResetPasswordResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\":\n\x12\x43hangeEmailRequest\x12\x11\n\tnew_email\x18\x01 \x01(\t\x12\x11\n\told_email\x18\x02 \x01(\t\"&\n\x13\x43hangeEmailResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x15\n\x13GetDashboardRequest\"\xc5\x01\n\x14GetDashboardResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06number\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\x18\n\x10\x61vailable_credit\x18\x06 \x01(\x02\x12\x10\n\x08video_id\x18\x07 \x01(\x05\x12\x12\n\nvideo_name\x18\x08 \x01(\t\x12\x11\n\tvideo_url\x18\t \x01(\t\x12\x13\n\x0bpicture_url\x18\n \x01(\t\"\'\n\x17UpdateProfilePicRequest\x12\x0c\n\x04\x66ile\x18\x01 \x01(\x0c\"}\n\x18UpdateProfilePicResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07picture\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x18\n\x10\x61vailable_credit\x18\x05 \x01(\x02\x12\x0c\n\x04user\x18\x06 \x01(\t\")\n\x19UploadProfileVideoRequest\x12\x0c\n\x04\x66ile\x18\x01 \x01(\x0c\"*\n\x16GetProfileVideoRequest\x12\x10\n\x08video_id\x18\x01 \x01(\x03\"_\n\x0cProfileVideo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nvideo_name\x18\x02 \x01(\t\x12\x19\n\x11\x63onversion_params\x18\x03 \x01(\t\x12\x14\n\x0cprofileVideo\x18\x04 \x01(\t\"!\n\x0e\x44\x65leteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"A\n\x19UpdateProfileVideoRequest\x12\x10\n\x08video_id\x18\x01 \x01(\x03\x12\x12\n\nvideo_name\x18\x02 \x01(\t\".\n\x1a\x43onvertProfileVideoRequest\x12\x10\n\x08video_id\x18\x01 \x01(\x03\"@\n\x1b\x43onvertProfileVideoResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x11\n\tvideo_url\x18\x02 \x01(\t\"2\n\x1e\x41\x64minDeleteProfileVideoRequest\x12\x10\n\x08video_id\x18\x01 \x01(\x03\" \n\rCRAPIResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x18\n\x16GetUserVehiclesRequest\"*\n\x0eVehicleCompany\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x83\x01\n\x0cVehicleModel\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05model\x18\x02 \x01(\t\x12\x11\n\tfuel_type\x18\x03 \x01(\t\x12\x13\n\x0bvehicle_img\x18\x04 \x01(\t\x12\x30\n\x0evehiclecompany\x18\x05 \x01(\x0b\x32\x18.identity.VehicleCompany\"\xe1\x01\n\x07Vehicle\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0f\n\x07pincode\x18\x03 \x01(\t\x12\x0b\n\x03vin\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x16\n\x0epreviousOwners\x18\x07 \x03(\t\x12%\n\x05model\x18\x08 \x01(\x0b\x32\x16.identity.VehicleModel\x12\x32\n\x0fvehicleLocation\x18\t \x01(\x0b\x32\x19.identity.VehicleLocation\x12\r\n\x05owner\x18\n \x01(\t\";\n\x17GetUserVehiclesResponse\x12 \n\x05items\x18\x01 \x03(\x0b\x32\x11.identity.Vehicle\"1\n\x11\x41\x64\x64VehicleRequest\x12\x0f\n\x07pincode\x18\x01 \x01(\t\x12\x0b\n\x03vin\x18\x02 \x01(\t\".\n\x19GetVehicleLocationRequest\x12\x11\n\tvehicleId\x18\x01 \x01(\t\"B\n\x0fVehicleLocation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08latitude\x18\x02 \x01(\t\x12\x11\n\tlongitude\x18\x03 \x01(\t\"\x80\x01\n\x1aGetVehicleLocationResponse\x12\r\n\x05\x63\x61rId\x18\x01 \x01(\t\x12\x10\n\x08\x66ullName\x18\x02 \x01(\t\x12\x32\n\x0fvehicleLocation\x18\x03 \x01(\x0b\x32\x19.identity.VehicleLocation\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"\"\n ResendVehicleDetailsEmailRequest2\x8c\x0e\n\x0fIdentityService\x12;\n\x06Signup\x12\x17.identity.SignupRequest\x1a\x18.identity.SignupResponse\x12\x38\n\x05Login\x12\x16.identity.LoginRequest\x1a\x17.identity.LoginResponse\x12S\n\x0e\x46orgotPassword\x12\x1f.identity.ForgotPasswordRequest\x1a .identity.ForgotPasswordResponse\x12\x43\n\nCheckOTPv3\x12\x19.identity.CheckOTPRequest\x1a\x1a.identity.CheckOTPResponse\x12\x43\n\nCheckOTPv2\x12\x19.identity.CheckOTPRequest\x1a\x1a.identity.CheckOTPResponse\x12J\n\x0b\x43hangeEmail\x12\x1c.identity.ChangeEmailRequest\x1a\x1d.identity.ChangeEmailResponse\x12Y\n\x10VerifyEmailToken\x12!.identity.VerifyEmailTokenRequest\x1a\".identity.VerifyEmailTokenResponse\x12P\n\rResetPassword\x12\x1e.identity.ResetPasswordRequest\x1a\x1f.identity.ResetPasswordResponse\x12L\n\x10LoginWithTokenv2\x12\x1f.identity.LoginWithTokenRequest\x1a\x17.identity.LoginResponse\x12L\n\x10LoginWithTokenv4\x12\x1f.identity.LoginWithTokenRequest\x1a\x17.identity.LoginResponse\x12M\n\x0cGetDashboard\x12\x1d.identity.GetDashboardRequest\x1a\x1e.identity.GetDashboardResponse\x12Y\n\x10UpdateProfilePic\x12!.identity.UpdateProfilePicRequest\x1a\".identity.UpdateProfilePicResponse\x12Q\n\x12UploadProfileVideo\x12#.identity.UploadProfileVideoRequest\x1a\x16.identity.ProfileVideo\x12K\n\x0fGetProfileVideo\x12 .identity.GetProfileVideoRequest\x1a\x16.identity.ProfileVideo\x12Q\n\x12UpdateProfileVideo\x12#.identity.UpdateProfileVideoRequest\x1a\x16.identity.ProfileVideo\x12P\n\x12\x44\x65leteProfileVideo\x12 .identity.GetProfileVideoRequest\x1a\x18.identity.DeleteResponse\x12\x62\n\x13\x43onvertProfileVideo\x12$.identity.ConvertProfileVideoRequest\x1a%.identity.ConvertProfileVideoResponse\x12\\\n\x17\x41\x64minDeleteProfileVideo\x12(.identity.AdminDeleteProfileVideoRequest\x1a\x17.identity.CRAPIResponse\x12V\n\x0fGetUserVehicles\x12 .identity.GetUserVehiclesRequest\x1a!.identity.GetUserVehiclesResponse\x12\x42\n\nAddVehicle\x12\x1b.identity.AddVehicleRequest\x1a\x17.identity.CRAPIResponse\x12_\n\x12GetVehicleLocation\x12#.identity.GetVehicleLocationRequest\x1a$.identity.GetVehicleLocationResponse\x12`\n\x19ResendVehicleDetailsEmail\x12*.identity.ResendVehicleDetailsEmailRequest\x1a\x17.identity.CRAPIResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'identity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SIGNUPREQUEST']._serialized_start=28
  _globals['_SIGNUPREQUEST']._serialized_end=106
  _globals['_SIGNUPRESPONSE']._serialized_start=108
  _globals['_SIGNUPRESPONSE']._serialized_end=141
  _globals['_LOGINREQUEST']._serialized_start=143
  _globals['_LOGINREQUEST']._serialized_end=190
  _globals['_LOGINRESPONSE']._serialized_start=192
  _globals['_LOGINRESPONSE']._serialized_end=274
  _globals['_FORGOTPASSWORDREQUEST']._serialized_start=276
  _globals['_FORGOTPASSWORDREQUEST']._serialized_end=314
  _globals['_FORGOTPASSWORDRESPONSE']._serialized_start=316
  _globals['_FORGOTPASSWORDRESPONSE']._serialized_end=357
  _globals['_CHECKOTPREQUEST']._serialized_start=359
  _globals['_CHECKOTPREQUEST']._serialized_end=422
  _globals['_CHECKOTPRESPONSE']._serialized_start=424
  _globals['_CHECKOTPRESPONSE']._serialized_end=459
  _globals['_VERIFYEMAILTOKENREQUEST']._serialized_start=461
  _globals['_VERIFYEMAILTOKENREQUEST']._serialized_end=539
  _globals['_VERIFYEMAILTOKENRESPONSE']._serialized_start=541
  _globals['_VERIFYEMAILTOKENRESPONSE']._serialized_end=584
  _globals['_LOGINWITHTOKENREQUEST']._serialized_start=586
  _globals['_LOGINWITHTOKENREQUEST']._serialized_end=639
  _globals['_RESETPASSWORDREQUEST']._serialized_start=641
  _globals['_RESETPASSWORDREQUEST']._serialized_end=696
  _globals['_RESETPASSWORDRESPONSE']._serialized_start=698
  _globals['_RESETPASSWORDRESPONSE']._serialized_end=754
  _globals['_CHANGEEMAILREQUEST']._serialized_start=756
  _globals['_CHANGEEMAILREQUEST']._serialized_end=814
  _globals['_CHANGEEMAILRESPONSE']._serialized_start=816
  _globals['_CHANGEEMAILRESPONSE']._serialized_end=854
  _globals['_GETDASHBOARDREQUEST']._serialized_start=856
  _globals['_GETDASHBOARDREQUEST']._serialized_end=877
  _globals['_GETDASHBOARDRESPONSE']._serialized_start=880
  _globals['_GETDASHBOARDRESPONSE']._serialized_end=1077
  _globals['_UPDATEPROFILEPICREQUEST']._serialized_start=1079
  _globals['_UPDATEPROFILEPICREQUEST']._serialized_end=1118
  _globals['_UPDATEPROFILEPICRESPONSE']._serialized_start=1120
  _globals['_UPDATEPROFILEPICRESPONSE']._serialized_end=1245
  _globals['_UPLOADPROFILEVIDEOREQUEST']._serialized_start=1247
  _globals['_UPLOADPROFILEVIDEOREQUEST']._serialized_end=1288
  _globals['_GETPROFILEVIDEOREQUEST']._serialized_start=1290
  _globals['_GETPROFILEVIDEOREQUEST']._serialized_end=1332
  _globals['_PROFILEVIDEO']._serialized_start=1334
  _globals['_PROFILEVIDEO']._serialized_end=1429
  _globals['_DELETERESPONSE']._serialized_start=1431
  _globals['_DELETERESPONSE']._serialized_end=1464
  _globals['_UPDATEPROFILEVIDEOREQUEST']._serialized_start=1466
  _globals['_UPDATEPROFILEVIDEOREQUEST']._serialized_end=1531
  _globals['_CONVERTPROFILEVIDEOREQUEST']._serialized_start=1533
  _globals['_CONVERTPROFILEVIDEOREQUEST']._serialized_end=1579
  _globals['_CONVERTPROFILEVIDEORESPONSE']._serialized_start=1581
  _globals['_CONVERTPROFILEVIDEORESPONSE']._serialized_end=1645
  _globals['_ADMINDELETEPROFILEVIDEOREQUEST']._serialized_start=1647
  _globals['_ADMINDELETEPROFILEVIDEOREQUEST']._serialized_end=1697
  _globals['_CRAPIRESPONSE']._serialized_start=1699
  _globals['_CRAPIRESPONSE']._serialized_end=1731
  _globals['_GETUSERVEHICLESREQUEST']._serialized_start=1733
  _globals['_GETUSERVEHICLESREQUEST']._serialized_end=1757
  _globals['_VEHICLECOMPANY']._serialized_start=1759
  _globals['_VEHICLECOMPANY']._serialized_end=1801
  _globals['_VEHICLEMODEL']._serialized_start=1804
  _globals['_VEHICLEMODEL']._serialized_end=1935
  _globals['_VEHICLE']._serialized_start=1938
  _globals['_VEHICLE']._serialized_end=2163
  _globals['_GETUSERVEHICLESRESPONSE']._serialized_start=2165
  _globals['_GETUSERVEHICLESRESPONSE']._serialized_end=2224
  _globals['_ADDVEHICLEREQUEST']._serialized_start=2226
  _globals['_ADDVEHICLEREQUEST']._serialized_end=2275
  _globals['_GETVEHICLELOCATIONREQUEST']._serialized_start=2277
  _globals['_GETVEHICLELOCATIONREQUEST']._serialized_end=2323
  _globals['_VEHICLELOCATION']._serialized_start=2325
  _globals['_VEHICLELOCATION']._serialized_end=2391
  _globals['_GETVEHICLELOCATIONRESPONSE']._serialized_start=2394
  _globals['_GETVEHICLELOCATIONRESPONSE']._serialized_end=2522
  _globals['_RESENDVEHICLEDETAILSEMAILREQUEST']._serialized_start=2524
  _globals['_RESENDVEHICLEDETAILSEMAILREQUEST']._serialized_end=2558
  _globals['_IDENTITYSERVICE']._serialized_start=2561
  _globals['_IDENTITYSERVICE']._serialized_end=4365
# @@protoc_insertion_point(module_scope)
