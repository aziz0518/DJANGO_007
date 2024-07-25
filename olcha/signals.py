from django.db.models.signals import post_save, pre_save,post_delete, pre_delete
from olcha.models import Category
from django.dispatch   import receiver
from django.core.mail import send_mail
from config.settings import DEFAULT_FROM_EMAIL,BASE_DIR
import os
import json

# def post_save_category(sender, instance, created, **kwargs):
#     if created:
#         print(f'Category {instance.category_name}  created')
#     else:
#         print(f'Category {instance.category_name} updated')




# post_save.connect(post_save_category, sender=post_save_category)


# def pre_delete_category(sender, instance, **kwargs):
#     print(kwargs)
#     print('Category saved json file before deleting')
    
    
    
# pre_delete.connect(pre_delete_category, sender=Category)


# @receiver(pre_save, sender= Category)
# def pre_save_category(sender,instance, **kwargs):
#     print('before save category')


@receiver(post_save, sender=Category)
def post_save_category(sender, instance, created, **kwargs):
    if created:
        print('Category created')
        subject = 'category created'
        message = f'test body category=> {instance.category_name}  created by admin'
        from_email = DEFAULT_FROM_EMAIL
        to = 'nuriddinovaziz75@gmail.com'
        send_mail(subject,message,from_email,[to,], fail_silently=False)
        
    else:
        print('Category updated')
    
    
@receiver(pre_delete, sender=Category) 
def pre_delete_category(sender,instance, **kwargs):
    print(dir(BASE_DIR)) 
    file_path = os.path.join(BASE_DIR, 'olcha/delete_products',f'category_{instance.id}.json')
    
    
    
    Category_data = {
        'id':instance.id,
        'Category_name':instance.category_name,
        'slug':instance.slug
    }
    
    with open(file_path, 'w')as json_file:
        json.dump(Category_data, json_file, indent=4)
        
    print('category saved json file before deleted')