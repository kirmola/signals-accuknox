import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel


# Signal receiver
@receiver(post_save, sender=TestModel)
def testEntryHandler(sender, instance, **kwargs):
    print("Signal handler -> Signal received, starting task.")
    time.sleep(3)  # Simulate a delay
    print("Signal handler: Task completed after 3 seconds.")


@receiver(post_save, sender=TestModel)
def entryThreadID(sender, instance, **kwargs):
    print(f"Signal handler: Running in thread {threading.current_thread().name}, ID: {threading.get_ident()}")


@receiver(post_save, sender=TestModel)
def AtomicTxnHandler(sender, instance, **kwargs):
    print("Signal handler: Saving Entry inside signal.")
    TestModel.objects.create(message=f"{secrets.token_urlsafe(23)}")