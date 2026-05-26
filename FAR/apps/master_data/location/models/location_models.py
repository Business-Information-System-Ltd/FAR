from django.db import models

class Location(models.Model):
    
    class LocationType(models.TextChoices):
        WAREHOUSE = 'WAREHOUSE', 'Warehouse'
        OFFICE = 'OFFICE', 'Office'
        STORE = 'STORE', 'Store'
        FACTORY = 'FACTORY', 'Factory'
        BRANCH = 'BRANCH', 'Branch'

    location_id = models.AutoField(primary_key=True)
   # models.py
    country_id = models.IntegerField(null=True, blank=True) 
    
    parent_location = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='sub_locations',
        db_column='parent_location_id'
    )
    
    location_code = models.CharField(max_length=10)
    location_name = models.CharField(max_length=100)
    location_type = models.CharField(
        max_length=20, 
        choices=LocationType.choices, 
        default=LocationType.OFFICE
    )
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    line1 = models.CharField(max_length=255, null=True, blank=True)
    line2 = models.CharField(max_length=255, null=True, blank=True)
    gps_map_reference = models.CharField(max_length=255, null=True, blank=True)
    
    full_location_code = models.CharField(max_length=100, null=True, blank=True)
    full_path = models.TextField(null=True, blank=True)
    
  
    allow_asset_assignment = models.BooleanField(default=True) 
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'location'  
    def save(self, *args, **kwargs):
        if self.parent_location:
            self.full_path = f"{self.parent_location.full_path} > {self.location_name}"
            self.full_location_code = f"{self.parent_location.full_location_code}-{self.location_code}"
        else:
            self.full_path = self.location_name
            self.full_location_code = self.location_code
            
        super(Location, self).save(*args, **kwargs)

    def __str__(self):
        return self.location_name