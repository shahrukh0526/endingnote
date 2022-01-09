from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from .models import Ending

@receiver(post_save,sender=User)
def create_ending(sender,instance, created, **kwargs):
    if created :
        ending=Ending(base_info ="例）私の名前は・・・",property_info ="例) 年金証書の保管場所は・・・",
            around_info = "例) 使用していたSNSのIDとパスワードは・・・",
            family_info = "例) 私の形見は〇〇に受け取ってほしい・・・",friends_info ="例) 〇〇との思い出は・・・",
            pets_info = "例) ペットの性格は・・・",medical_info = "例) 介護の費用はここから出してほしい・・・",
            inherit_info ="例) 遺言書の保管場所は・・・",contact_info = "例) 私の親友の連絡先は・・・",message_info ="例) ありがとう・・・",email=instance.email)
        ending.save()