from rest_framework import serializers
from .models import Driver, Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class DriverInfoSerializer(serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = ['id', 'name', 'cars', 'age']

    def get_cars(self, obj):
        blue_red_cars = Car.objects.filter(driver=obj, color__in=['blue', 'red'])
        car_data = CarSerializer(blue_red_cars, many=True).data
        return car_data



class DriverRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['license_no', 'phone', 'address', 'city', 'state', 'national_code', 'age']


    # logics to register a driver
    def create(self, validated_data):
        # create deiver and car objects and return them together
        car_data = validated_data.pop('car')
        car = Car.objects.create(**car_data)
        driver = Driver.objects.create(car=car, **validated_data)
        return driver

    def update(self, instance, validated_data):
        instance.license_no = validated_data.get('license_no', instance.license_no)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.national_code = validated_data.get('national_code', instance.national_code)
        instance.age = validated_data.get('age', instance.age)
        # update car data
        instance.car.car_model = validated_data.get('car_model', instance.car.car_model)
        instance.car.car_tag = validated_data.get('car_tag', instance.car.car_tag)
        instance.car.car_type = validated_data.get('car_type', instance.car.car_type)
        instance.car.color = validated_data.get('color', instance.car.color)
        instance.car.save()
        instance.save()
        return instance

    def validate(self, data):
        if not data['license_no']:
            raise serializers.ValidationError('license_no is required')
        if not data['phone']:
            raise serializers.ValidationError('phone is required')
        if not data['address']:
            raise serializers.ValidationError('address is required')
        # if user already have a Big car big type, cant add another big car
        if data['car_type'] == 'big':
            if Driver.objects.filter(car__car_type='big').exists():
                raise serializers.ValidationError('You already have a big car')
        return data

    def validate_license_no(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('license_no is too short')
        return value

    def destroy(self, instance):
        instance.delete()
        return instance





