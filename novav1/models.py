from django.db import models
from datetime import *
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime
# Create your models here.
from django.db.models.signals import post_save
import math
from django.db import models
from django.conf import settings
from django.db import transaction
from django.db.models import Sum
import random
import string


def create_ref_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))



class DoctorOut(models.Model):
    DocName=models.CharField(db_column='DocNameOut',default='New Doctor', max_length=150, blank=True, null=True) 
    Active =models.BooleanField(default=True) 
    def __str__ (self):
        return  str(self.DocName)


class DoctorIn(models.Model):
    DocName=models.CharField(db_column='DocNameIN',default='New Doctor', max_length=150, blank=True, null=True) 
    DocSpecialty=models.CharField(db_column='DocSpecialty',default='', max_length=150, blank=True, null=True) 
    Active =models.BooleanField(default=True) 
    def __str__ (self):
        return  str(self.DocName)


class Area(models.Model):
    AreaName = models.CharField(db_column='Text_Area', max_length=150, blank=True, null=True)  # Field name made lowercase.
    Active =models.BooleanField(default=True) 
    def __str__ (self):
        return  str(self.AreaName)

# class Clinc(models.Model):
#     ClincName = models.CharField(db_column='Text_Clinc', max_length=150, blank=True, null=True)  # Field name made lowercase.

#     def __str__ (self):
#         return  str(self.ClincName)


class Comefrom(models.Model):
    ComeFrom= models.CharField(db_column='Text_ComeFrom', max_length=150, blank=True, null=True)  # Field name made lowercase.

    def __str__ (self):
        return  str(self.ComeFrom)


class Gender(models.Model):
    Gender = models.CharField(db_column='Gender_Text', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__ (self):
        return  str(self.Gender)


class Jop(models.Model):
    JopName = models.CharField(db_column='Text_Jop', max_length=150, blank=True, null=True)  # Field name made lowercase.

    def __str__ (self):
        return  str(self.JopName)



class Device(models.Model):
    DeviceName=models.CharField(max_length=50)      
    DeviceFunction = models.CharField( max_length=50)
    Active =models.BooleanField(default=True) 
    def __str__ (self):
        return  str(self.DeviceName)

class Room(models.Model):
    RoomName=models.CharField( max_length=50) 
    RoomActive =models.BooleanField(default=True) 
    Branch = models.ForeignKey("Branch", verbose_name=("Branch Name"), on_delete=models.CASCADE, blank=True, null=True)

    def __str__ (self):
        return  str(self.RoomName)
class Branch(models.Model):
    BranchName=models.CharField(max_length=50,default="")
    Active =models.BooleanField(default=True) 
    def __str__ (self):
        return  str(self.BranchName)

class Clinc(models.Model):
    ClincName=models.CharField( max_length=50)
    Branch =models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    Room=models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    Device=models.ForeignKey(Device,  on_delete=models.CASCADE, blank=True, null=True)
    cereatedDate=models.DateField( auto_now_add=True, blank=True, null=True)
    Active= models.BooleanField(default=True)
    StartDdate=models.DateField(auto_now_add=True, blank=True, null=True)
    CloseDdate=models.DateField( blank=True, null=True)
    
    def __str__ (self):
        return  str(self.ClincName)




class Patient(models.Model):
    PatientName = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    PatientSecondName = models.CharField(db_column='SecondName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    PatientThirdName = models.CharField(db_column='ThirdName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    Gender = models.ForeignKey('Gender', models.DO_NOTHING, db_column='Id_Gender', blank=True, null=True)
    Active = models.BooleanField(default=True)  # Field name made lowercase.
    PatientCode = models.CharField(db_column='Pationt_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    PatientBbarcode = models.CharField(db_column='Pationt_BarCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    Birtdate = models.DateField( blank=True, null=True) # Field name made lowercase.
    ComeFrom = models.ForeignKey(Comefrom, models.DO_NOTHING, db_column='Id_ComeFrom', blank=True, null=True)  # Field name made lowercase.
    PatientFfriend =models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    doctor = models.ForeignKey(DoctorOut, models.DO_NOTHING, db_column='Id_Doctor', blank=True, null=True , default=0)  # Field name made lowercase.
    Jop = models.ForeignKey(Jop,  on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    JopArea = models.ForeignKey(Area, models.DO_NOTHING, db_column='JopArea', blank=True, null=True, related_name='JopArea')  # Field name made lowercase.
    PlaceJop = models.CharField(db_column='Place_Jop', max_length=150, blank=True, null=True)  # Field name made lowercase.
    Area = models.ForeignKey(Area, models.DO_NOTHING, db_column='Area', blank=True, null=True, related_name='Area')  # Field name made lowercase.
    PatientMobile1= models.CharField(blank=True, null=True, max_length=50)
    PatientMobile2= models.IntegerField(blank=True, null=True)
    #CreatedDate =models.DateField(auto_now_add=True, blank=True, null=True)
 #   PatientPackages= models.ManyToManyField("Packages", related_name="PPackages" )
    BallceBalance=models.IntegerField(default=0)
    UsedBalls=models.IntegerField(default=0)
    RemmainingBalance=models.IntegerField(default=0)
    AmountBalance=models.IntegerField(default=0)
    paid=models.IntegerField(default=0)
    Remmainingamount=models.IntegerField(default=0)   


    def __str__ (self):
        return  str(self.PatientName)

    def save(self, *args, **kwargs):
            self.RemmainingBalance = self.BallceBalance-self.UsedBalls
            self.Remmainingamount =self.AmountBalance-self.paid
            super(Patient, self).save(*args, **kwargs)
    


class Reservation(models.Model):
    Patient = models.ForeignKey("Patient", on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    DateReservation = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    FromTimeReservation = models.DateTimeField(db_column='FromTime_Reservation', blank=True, null=True)  # Field name made lowercase.
    ToTimeReservation = models.DateTimeField(db_column='ToTime_Reservation', blank=True, null=True)  # Field name made lowercase.
    Doctor=models.ForeignKey(DoctorIn,  on_delete=models.CASCADE, blank=True, null=True)
    Branch = models.ForeignKey("Branch",  on_delete=models.CASCADE, blank=True, null=True)# Field name made lowercase.
    #StractuerDevice = models.IntegerField(db_column='Id_Stractuer_Machine')  # Field name made lowercase.
    #StractuerRoom = models.IntegerField(db_column='Id_Stractuer_Room')  # Field name made lowercase.
    Clinc = models.ForeignKey('novav1.Clinc', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    Reservation = models.CharField(db_column='Text_Reservation', max_length=350, blank=True, null=True)  # Field name made lowercase.
    #CreatedDate =models.DateField(auto_now_add=True, blank=True, null=True)
    balance = models.FloatField()
    def __str__ (self):
        return  str(self.Patient)


class Stractuer(models.Model):
    StractuerPer = models.IntegerField(db_column='Id_Stractuer_Per', blank=True, null=True)  # Field name made lowercase.
    NameStractuer = models.IntegerField(db_column='Name_Stractuer', blank=True, null=True)  # Field name made lowercase.
    
    def __str__ (self):
        return  str(self.NameStractuer)



class pricing(models.Model):
    BodyPart=models.CharField( max_length=50)
    price=models.IntegerField(default=0)
    BallsNumber=models.IntegerField(default=0)
    time_of_part=models.IntegerField(default=0)
    def __str__(self):
        return self.BodyPart

    def partprice(self):
        return self.price

    def parts_time(self):
        t_time=0
        for i in pricing:
            t_time =+ time_of_part
        return  t_time  


class Packages(models.Model):
    PackageName=models.CharField(max_length=50)      
    PackageParts=models.ManyToManyField('pricing',related_name='PackageParts') 
  # PackageOldPrice=models.FloatField( blank=True, null=True)
    PackageNewPrice=models.FloatField()
    OneBalcesPrice=models.FloatField(default=0)
    CountBalces=models.FloatField(default=0)
    Active = models.BooleanField(default=True)

    def __str__(self):
        return self.PackageName

    # def oldp(self):
    #     qs = Packages.objects.all()
              
    #     total=0
    #     for value in qs:
    #         total += value.PackageParts.prefetch_related('price')
    #         print(total)
    #     return total

    # def save(self, *args, **kwargs):
    #         self.PackageOldPrice = self.oldp()
    #         super(Packages, self).save(*args, **kwargs)
    
# class ItemManager(models.Manager):
#     def get_queryset(self):
#         return ItemQuerySet(self.model, using=self._db)

#     def all(self):
#         return self.get_queryset().active()

#     def featured(self): #Product.objects.featured() 
#         return self.get_queryset().featured()

#     def get_by_id(self, id):
#         qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
#         if qs.count() == 1:
#             return qs.first()
#         return None

#     def search(self, query):
#         return self.get_queryset().active().search(query)     


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:category", kwargs={
            'slug': self.slug
        })

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code





class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    PackageParts=models.ManyToManyField('pricing',related_name='itemPackageParts',blank=True, null=True)
    CountBalces=models.FloatField(default=0)
    BalcesNumber=models.FloatField(default=0)
    #slug = models.SlugField()
    #stock_no = models.CharField(max_length=10)
    description_short = models.CharField(max_length=150,blank=True, null=True)
    #description_long = models.TextField()
    image = models.ImageField(blank=True, null=True)
    Active = models.BooleanField(default=True)
    #objects = ItemManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'id': self.id
        })
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    # def get_add_to_cart_url(self):
    #     return reverse("core:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })

    # def get_remove_from_cart_url(self):
    #     return reverse("core:remove-from-cart", kwargs={
    #         'slug': self.slug
    #     })


class OrderItem(models.Model):
    Patient=models.ForeignKey("Patient", on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price =models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    #size = models.ForeignKey('size',on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_balls(self):
        return self.quantity * self.item.CountBalces

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


    def get_total(self):
        total = 0
        for order_item in OrderItem:
            total += get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


        cstomer = OrderItem.objects.all()
        for group in cstomer:
            group.cstomer = OrderItem.objects.filter(id=id)    
        print(group)    
    
    def save(self, *args, **kwargs):
        self.price= self.get_final_price()
        super(OrderItem, self).save(*args, **kwargs)



class Order_type(models.Model):
    Type=models.CharField( max_length=50)
    Cash_efect=models.IntegerField(default=0)
    Balls_efect=models.IntegerField(default=0)

    def __str__(self):
        return self.Type        

ORDER_TYPE = (
    
    (1, 'SALE'),
    (2, 'BALLS TRANSFER Add '),
    (3, 'BALLS TRANSFER reducing '),
    (4, 'PYMENT'),
    (5,'Refunds')
)



class Order(models.Model):
    Patient      =     models.ForeignKey("Patient", on_delete=models.CASCADE, blank=True, null=True)
    Patient_from     =     models.ForeignKey("Patient",related_name='Patient_from' ,on_delete=models.CASCADE, blank=True, null=True)
    user         =     models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ref_code     =     models.CharField(max_length=20,default=create_ref_code())
    items        =     models.ManyToManyField(OrderItem, blank=True, null=True)
    start_date   =     models.DateTimeField(auto_now_add=True)
    order_type   =     models.IntegerField(choices=ORDER_TYPE,default=1,blank=True,null=True)
    ordered_date =     models.DateTimeField()  #auto_now_add=True
    ordered      =     models.BooleanField(default=False)
    # received     =     models.BooleanField(default=False)
    # refund_requested = models.BooleanField(default=False)
    # refund_granted   = models.BooleanField(default=False)

    TotalPrice       = models.IntegerField(default=0)
    Discount         = models.IntegerField(default=0)
    Net              = models.IntegerField(default=0,blank=True,null=True)
    Cash             = models.IntegerField(default=0)
    Remmaining       = models.IntegerField(default=0)

    Refunds          = models.IntegerField(default=0)
    
    balls            = models.IntegerField(default=0)
    ballsRemmaining  = models.IntegerField(default=0)

    
    

    def __str__(self):
        return self.Patient.PatientName

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    
    def get_total_balls(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_balls()
        return total


    def net(self):
        return self.TotalPrice - self.Discount 
         

    def remider(self):
         return self.Net - self.Cash  
           

   

    def save(self, *args, **kwargs):
        if not self.id:
              super(Order, self).save(*args, **kwargs)
        else:      
              self.TotalPrice= self.get_total()
             #self.TotalPrice=  int(self.items.aggregate(Sum('price')).values())[0]
              self.Net= self.net()
              self.Remmaining =self.remider()
              self.balls = self.get_total_balls()
              super(Order, self).save(*args, **kwargs)


def balls_update(sender,**kwargs):

       created = kwargs['created']
       instance = kwargs['instance']

       Patient= instance.Patient
       balls = instance.balls
       
       
       if created:

        add_balls = ballses(
            Patient=Patient,
            transaction_type=1,
            ballses_count =balls

                        
            
            )
        add_balls.save()
post_save.connect(balls_update,sender=Order) 


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


class Transaction(models.Model):
        from_user = models.ForeignKey("Patient", on_delete=models.CASCADE, related_name='from_user', blank=True, null=True)
        to_user = models.ForeignKey("Patient", on_delete=models.CASCADE, related_name='to_user', blank=True, null=True)
        time = models.DateTimeField(default=datetime.now)
        amount = models.PositiveIntegerField()
        reason = models.CharField(max_length=100)
        success = models.BooleanField(default=False)

        @transaction.atomic
        def make_transaction(self,from_user, to_user, amount, reason):
            status = False
            if from_user.amount >= amount:
                from_user.amount -= amount
                to_user.amount += amount
                from_user.save()
                to_user.save()
                status = True
            transaction = Transaction(from_user=from_user.user, to_user=to_user.user, amount=amount, success=status, reason=reason)
            transaction.save()
            return transaction, status

        def get_absolute_url(self):
            return reverse('healthcare:transaction-detail', kwargs={'pk': self.pk})

        def __str__(self):
            return str(self.id) + ': ' + str(self.from_user) + ' to ' + str(self.to_user) + ' - ' + str(self.amount) 



class ballses(models.Model):
    Patient= models.ForeignKey("Patient",  on_delete=models.CASCADE)
    transaction_type=models.IntegerField()
    ballses_count=models.IntegerField()


    def __str__(self):
        return str(self.Patient)
    


