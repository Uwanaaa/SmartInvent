from django.db.models.signals import post_save
from .models import Product,ProductReplenishment
from django.dispatch import receiver
from django.core.mail import send_mail
from users.middlewares import get_current_user


@receiver(post_save,sender=Product)
def send_email_notification(sender,instance,**kwargs):
    instance_object = Product.objects.get(id=instance.id)
    user = get_current_user()
    if int(instance.stock) <= user.alert_value:
        if user.role == 'Admin':
            subject = "Low Stock Alert"
            message = f"Product {instance.name} has low stock. Please restock."
            send_mail(subject,message,"uwanaudofia8@gmail.com",[user.email])
 
            
            product = ProductReplenishment.objects.filter(product=instance.id).first()
            if product:
                subject = f"The Purchase of {instance.name}"
                message = (
                    f"Product {instance.name} has low stock. "
                    f"Please we would require {product.defaultValue} more for {user}. "
                    "Thank you for your partnership."
                )
            send_mail(subject,message,'uwanaudofia8@gmail.com',[product.providerEmail])