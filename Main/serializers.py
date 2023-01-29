from rest_framework import serializers
from .models import Ecommerce

'''to serialize the data we have to create a 
serializer class which is very similar to 
django model class & forms class'''
class EcommerceSerializers(serializers.Serializer):
    name=serializers.CharField()
    categeory=serializers.CharField()
    price=serializers.IntegerField()
    details=serializers.CharField()
    image=serializers.ImageField()

    def create(self,validated_data):
        #this method is used to add a data in database.
        return Ecommerce.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        #this method is used to update the existing data
        instance.name = validated_data.get('name',instance.name)
        #instance is the previous data
        instance.categeory = validated_data.get('categeory',instance.categeory)
        #validated_data is new data
        instance.price = validated_data.get('price',instance.price)
        instance.details = validated_data.get('details',instance.details)
        instance.image = validated_data.get('image',instance.image)
        #this will save the data
        instance.save()
        return instance
