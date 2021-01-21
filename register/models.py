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

BLOOD_TYPE_CHOICES = (
        ('A +', 'A +'),
        ('A -', 'A -'),
        ('AB +', 'AB +'),
        ('AB -', 'AB -'),
        ('O +', 'O +'),
        ('O -', 'O -'),
    )

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
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

    def __str__(self):
        return self.description


class Homeless (models.Model):
    frist_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cpf = models.CharField(max_length=14, blank=True, verbose_name='CPF')
    rg = models.CharField(max_length=13, blank=True, verbose_name=('RG'))
    issuing_body = models.CharField(max_length=12, blank=True)
    height = models.DecimalField(decimal_places=3, max_digits=8)
    weight = models.DecimalField(decimal_places=3, max_digits=8)
    blood_type = models.CharField(max_length=4, choices=BLOOD_TYPE_CHOICES)
    registration_date = models.DateField(auto_now = False, auto_now_add=True)
    nationality = models.ForeignKey('Nationality', on_delete=models.PROTECT) #ForeignKey
    about = models.OneToOneField('About', on_delete=models.PROTECT) #ForeignKey
    
    class Meta:
        db_table = 'homeless'

    def __str__(self):
        return '{} {}  in nickname:({})' .format(self.frist_name, self.second_name, self.nickname)



class Addiction(models.Model):
    name_addiction = models.CharField(max_length=200)
    type_addiction = models.CharField(max_length=200)
    homeless = models.ForeignKey('Homeless', on_delete=models.PROTECT)

    class Meta:
        db_table = 'addiction'

    def __str__(self):
        return '{} of type {} of homeless ({})' .format(self.name_addiction, self.type_addiction, self.homeless.nickname)
        