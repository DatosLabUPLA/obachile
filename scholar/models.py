from django.db import models
import ast

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    id_a = models.TextField(db_column='Id_A', unique=True, blank=True)  # Field name made lowercase.
    nombre_autor = models.TextField(db_column='Nombre_Autor')  # Field name made lowercase.
    cargo = models.TextField(db_column='Cargo')  # Field name made lowercase.
    dominio = models.TextField(db_column='Dominio')  # Field name made lowercase.
    citas = models.TextField(db_column='Citas')  # Field name made lowercase.
    intereses = models.TextField(db_column='Intereses')  # Field name made lowercase.
    links = models.TextField(db_column='Links')  # Field name made lowercase.
    año_desde = models.IntegerField(db_column='Año_Desde', blank=True, null=True)  # Field name made lowercase.
    hindex_todo = models.IntegerField(db_column='Hindex_todo', blank=True, null=True)  # Field name made lowercase.
    hindex_desde = models.IntegerField(db_column='Hindex_Desde', blank=True, null=True)  # Field name made lowercase.
    todas_citas = models.IntegerField(db_column='Todas_Citas', blank=True, null=True)  # Field name made lowercase.
    citas_desde = models.IntegerField(db_column='Citas_Desde', blank=True, null=True)  # Field name made lowercase.
    id_institucion = models.TextField(db_column='Id_Institucion', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Autor'
        def __str__(self):
            return "{} - {}", format(self.nombre_autor, self.citas)




class AutorPaper(models.Model):
    a_id = models.IntegerField(db_column='A_id', blank=True, primary_key=True)  # Field name made lowercase.
    paper_id = models.TextField(db_column='Paper_Id')  # Field name made lowercase.
    autorpaper_id = models.TextField(db_column='AutorPaper_Id')  # Field name made lowercase.
    autor_id = models.TextField(db_column='Autor_Id')  # Field name made lowercase.
    titulo_paper = models.TextField(db_column='Titulo_Paper')  # Field name made lowercase.
    autores_paper = models.TextField(db_column='Autores_Paper')  # Field name made lowercase.
    revista = models.TextField(db_column='Revista')  # Field name made lowercase.
    revista_sp = models.TextField(db_column='Revista_sp')  # Field name made lowercase.
    revista_m = models.TextField(db_column='Revista_m')  # Field name made lowercase.
    citado_por = models.TextField(db_column='Citado_Por')  # Field name made lowercase.
    año = models.TextField(db_column='Año')  # Field name made lowercase.
    link_paper = models.TextField(db_column='Link_Paper')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Autor_Paper'


class Citas(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    autor_id = models.TextField(db_column='Autor_Id', blank=True, null=True)  # Field name made lowercase.
    year_hist = models.TextField(db_column='Year_hist', blank=True, null=True)  # Field name made lowercase.
    citas_hist = models.TextField(db_column='Citas_hist', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Citas'


class Coautores(models.Model):
    id = models.IntegerField(db_column='Id', blank=True,  primary_key=True)  # Field name made lowercase.
    coautor_id = models.TextField(db_column='Coautor_Id', blank=True, null=True)  # Field name made lowercase.
    coautor = models.TextField(db_column='Coautor', blank=True, null=True)  # Field name made lowercase.
    institucion = models.TextField(db_column='Institucion', blank=True, null=True)  # Field name made lowercase.
    dominio = models.TextField(db_column='Dominio', blank=True, null=True)  # Field name made lowercase.
    a_id = models.TextField(db_column='A_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coautores'


class Instituciones(models.Model):
    institutiontypeid = models.IntegerField(db_column='InstitutionTypeID', blank=True, null=True)  # Field name made lowercase.
    institutiontype = models.TextField(db_column='InstitutionType', blank=True, null=True)  # Field name made lowercase.
    institutionacronymid = models.TextField(db_column='InstitutionAcronymID', blank=True, null=True)  # Field name made lowercase.
    institutionacronym = models.TextField(db_column='InstitutionAcronym', blank=True, null=True)  # Field name made lowercase.
    institutionid = models.IntegerField(db_column='InstitutionID', blank=True, null=True)  # Field name made lowercase.
    institution = models.TextField(db_column='Institution', blank=True, null=True)  # Field name made lowercase.
    students = models.IntegerField(db_column='Students', blank=True, null=True)  # Field name made lowercase.
    googlescholarid = models.TextField(db_column='GoogleScholarID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Instituciones'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'
# Unable to inspect table 'auth_group_permissions'
# The error was: list index out of range


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'
# Unable to inspect table 'auth_user_groups'
# The error was: list index out of range
# Unable to inspect table 'auth_user_user_permissions'
# The error was: list index out of range
# Unable to inspect table 'django_admin_log'
# The error was: list index out of range


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

