from django.db import models

# Create your models here.
SCHOOL_LEVEL_CHOICES = (
        ('Complete primary education', 'Complete primary education'),
        ('Incomplete elementary school', 'Incomplete elementary school'),
        ('Complete high school', 'Complete high school'),
        ('Incomplete high school', 'Incomplete high school'),
        ('Complete higher education', 'Complete higher education'),
        ('Incomplete higher education', 'Incomplete higher education'),
        ('Higher education more', 'Higher education more'),
)

BREED_CHOICES = (
        ('Whites' , 'Whites'),
        ('Dun' , 'Dun'),
        ('Black' , 'Black'),
        ('Yellow' , 'Yellow'),
        ('Native' , 'Native'),
)

ETHNICITY_CHOICES = (
        ('Whites' , 'Whites'),
        ('Black' , 'Black'),
        ('Native' , 'Native'),
        ('Dun' , 'Dun'),
        ('Mulatto' , 'Mulatto'),
        ('Caboclos' , 'Caboclos'),
        ('Cafuzos' , 'Cafuzos'),
)

STATE_CHOICES = (
    ('AC' , 'Acre'),
    ('AL', 'Alagoas'),
    ('AP','Amapá'),
    ('AM','Amazonas'),
    ('BA','Bahia'),
    ('CE','Ceará'),
    ('ES','Espírito Santo'),
    ('GO','Goiás'),
    ('MA','Maranhão'),
    ('MT','Mato Grosso'),
    ('MS','Mato Grosso do Sul'),
    ('MG','Minas Gerais'),
    ('PA','Pará'),
    ('PB','Paraíba'),
    ('PR','Paraná'),
    ('PE','Pernambuco'),
    ('PI','Piauí'),
    ('RJ','Rio de Janeiro'),
    ('RN','Rio Grande do Norte'),
    ('RS','Rio Grande do Sul'),
    ('RO','Rondônia'),
    ('RR','Roraima'),
    ('SC','Santa Catarina'),
    ('SP','São Paulo'),
    ('SE','Sergipe'),
    ('TO','Tocantins'),
    ('DF','Distrito Federal'),

)


class Nationality(models.Model):
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)

    class Meta:
        db_table='nationality'

    def __str__(self):
        return '{} ({})'.format(self.city, self.state)


class About(models.Model):
    description = models.TextField(max_length=999)
    history = models.TextField(max_length=999)
    sexual_orientation = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, choices=BREED_CHOICES)
    ethnicity = models.CharField(max_length=30, choices=ETHNICITY_CHOICES)
    school_level = models.CharField(max_length=40, choices=SCHOOL_LEVEL_CHOICES)

    class Meta:
        db_table ='about'
