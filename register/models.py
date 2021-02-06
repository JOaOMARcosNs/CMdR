from django.db import models
from django.contrib.auth.models import User
# Create your models here.
SCHOOL_LEVEL_CHOICES = (
        ('Analfabeto', 'Analfabeto'),
        ('Até 5º Ano Incompleto', 'Até 5º Ano Incompleto'),
        ('5º Ano Completo', '5º Ano Completo'),
        ('6º ao 9º Ano do Fundamental', '6º ao 9º Ano do Fundamental'),
        ('Fundamental Completo', 'Fundamental Completo'),
        ('Médio Incompleto', 'Médio Incompleto'),
        ('Médio Completo', 'Médio Completo'),
        ('Superior Incompleto', 'Superior Incompleto'),
        ('Superior Completo', 'Superior Completo'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
        ('Ignorado', 'Ignorado'),
)

BREED_CHOICES = (
        ('Brancos' , 'Brancos'),
        ('Pardos' , 'Pardos'),
        ('Pretos' , 'Pretos'),
        ('Indígenas' , 'Indígenas'),
        ('Amarelos' , 'Amarelos'),
)

ETHNICITY_CHOICES = (
        ('Brancos' , 'Brancos'),
        ('Pretos' , 'Pretos'),
        ('Indígenas' , 'Indígenas'),
        ('Pardos' , 'Pardos'),
        ('Mulatos' , 'Mulatos'),
        ('Caboclos' , 'Caboclos'),
        ('Confusos' , 'Confusos'),
)

STATE_CHOICES = (
    ('AC', 'Acre'),
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
    city = models.CharField(max_length=35, verbose_name='Cidade')
    state = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name='Estado')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table='nationality'

    def __str__(self):
        return '{} ({})'.format(self.city, self.state)


class About(models.Model):
    description = models.TextField(max_length=999, verbose_name='Descrição')
    history = models.TextField(max_length=999, verbose_name='História')
    sexual_orientation = models.CharField(max_length=30, verbose_name='Orientação sexual')
    breed = models.CharField(max_length=30, choices=BREED_CHOICES, verbose_name='Raça')
    ethnicity = models.CharField(max_length=30, choices=ETHNICITY_CHOICES, verbose_name='Etnia')
    school_level = models.CharField(max_length=40, choices=SCHOOL_LEVEL_CHOICES, verbose_name='Níveis de escolaridade')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table ='about'

    def __str__(self):
        return self.description


class Homeless (models.Model):
    
    frist_name = models.CharField(max_length=30, verbose_name='Primeiro nome')
    second_name = models.CharField(max_length=30, verbose_name='Segundo nome')
    nickname = models.CharField(max_length=30, verbose_name='Apelido')
    birth_date = models.DateField(verbose_name='Data de nascimento')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Gênero')
    cpf = models.CharField(max_length=14, blank=True, verbose_name='CPF', unique=True)
    rg = models.CharField(max_length=13, blank=True, verbose_name='RG', unique=True)
    issuing_body = models.CharField(max_length=12, blank=True, verbose_name='Órgão expedidor')
    height = models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Altura')
    weight = models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Peso')
    blood_type = models.CharField(max_length=4, choices=BLOOD_TYPE_CHOICES, verbose_name='Tipo sanguíneo')
    registration_date = models.DateField(auto_now = False, auto_now_add=True)
    nationality = models.ForeignKey('Nationality', on_delete=models.PROTECT, verbose_name='Nacionalidade') #ForeignKey
    about = models.OneToOneField('About', on_delete=models.PROTECT, verbose_name='História/Sobre') #ForeignKey
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'homeless'

    def __str__(self):
        return '{} {}  in nickname:({})' .format(self.frist_name, self.second_name, self.nickname)



class Addiction(models.Model):
    name_addiction = models.CharField(max_length=200, verbose_name='Nome do vício')
    type_addiction = models.CharField(max_length=200, verbose_name='Tipo do vício')
    homeless = models.ForeignKey('Homeless', on_delete=models.PROTECT, verbose_name='Sem-teto')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'addiction'

    def __str__(self):
        return '{} of type {} of homeless ({})' .format(self.name_addiction, self.type_addiction, self.homeless.nickname)

class Disease(models.Model):
      name_disease = models.CharField(max_length=90, verbose_name='Nome da doença')
      type_disease = models.CharField(max_length=90, verbose_name='Tipo da doença')
      homeless = models.ForeignKey('Homeless', on_delete=models.PROTECT, verbose_name='Sem-teto')
      user = models.ForeignKey(User, on_delete=models.PROTECT)

      class Meta:
          db_table = 'Disease'

      def __str__(self):
          return '{} of type {} of homeless ({})'.format(self.name_disease, self.type_disease, self.homeless.nickname)



    

    