from django.shortcuts import render
from django.http import JsonResponse
from .models import TestModel
import secrets, threading
from django.db import transaction

def createEntry1(request):
    print("Before saving the entry.")
    entry = TestModel.objects.create(name=f"{secrets.token_urlsafe(23)}")
    print("After saving the entry.", entry)
    return JsonResponse({
        "data":entry.name,
        "status":True
    })


def createEntry2(request):
    print(f"Caller: Running in thread {threading.current_thread().name}, ID: {threading.get_ident()}")
    TestModel.objects.create(message=f"{secrets.token_urlsafe(23)}")


def createEntry3(request):
    try:
        with transaction.atomic():
            print("Caller -> Saving entry.")
            data = TestModel.objects.create(name=f"{secrets.token_urlsafe(23)}")
            print("Caller -> Raising exception.")
            raise Exception("exception raised manually")  # This will cause a rollback since all signals run in same db txn. 
    except Exception as e:
        print(f"Exception occurred: {e}")

