#!/usr/bin/env python3
import subprocess
import boto3
import botocore


def upload_cert(cert_name, path_to_public_cert, path_to_private_cert):
    """Upload self signed security certificate to IAM. 
    Args:
        cert_name: Desired name of the security certificate to show on IAM
        path_to_public_cert: A self signed key to upload.
        path_to_private_cert: A private key pair of the self-seigned public key.
            

