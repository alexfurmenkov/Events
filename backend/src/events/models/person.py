import binascii
import hashlib
import os

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, update_last_login
from django.db import models

from rest_framework_jwt.settings import api_settings


class Person(AbstractBaseUser):
    """
    User model
    """
    class Meta:
        app_label = 'events'

    email = models.EmailField(max_length=512, default=None, unique=True)
    password = models.CharField(max_length=512, default=None)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @classmethod
    def get_user_by_email(cls, email):
        """
        Gets user by email
        :param email: email of the Person object
        :return: Person object with corresponding email
        """
        try:
            existing_user = cls.objects.get(email=email)
            return existing_user
        except cls.DoesNotExist:
            return None

    @classmethod
    def hash_password_with_salt(cls, password):
        """
        Hashes password with sha256 algorithm and salt
        :param password: Password entered by user
        :return: Hashed password with salt.
                 First 64 symbols are the salt.
        """
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        hashed_password = hashlib.pbkdf2_hmac('sha512',
                                              password.encode('utf-8'),
                                              salt, 100000)
        hashed_password = binascii.hexlify(hashed_password)
        return (salt + hashed_password).decode('ascii')

    @classmethod
    def authenticate_user(cls, email, password):
        """
        Authenticates user if email and password are correct
        :param email: email of the Person object
        :param password: password of the Person object
        :return: Company object
        """
        user = cls.get_user_by_email(email)

        if user is not None:
            salt = user.password[:64]
            hashed_password = hashlib.pbkdf2_hmac('sha512',
                                                  password.encode('utf-8'),
                                                  salt.encode('ascii'),
                                                  100000)
            hashed_password = salt + binascii.hexlify(hashed_password).decode(
                'ascii'
            )
            if hashed_password == user.password:
                return user

    def login(self):
        """
        Generates JWT token and updates last login
        :return: JWT token
        """
        payload = api_settings.JWT_PAYLOAD_HANDLER(self)
        jwt_token = api_settings.JWT_ENCODE_HANDLER(payload)
        update_last_login(None, self)
        return jwt_token
