# Generated by Django 2.2.9 on 2023-01-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidates_name', models.CharField(max_length=200)),
                ('manifesto', models.TextField()),
                ('portfolio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(choices=[('nigeria', 'nigeria'), ('choose_nationality', 'choose_nationality')], default='choose_nationality', max_length=200)),
                ('location', models.CharField(blank=True, choices=[('in_nigeria', 'in_nigeria'), ('nigeria_diasppora', 'nigeria_diasppora')], max_length=200, null=True)),
                ('state_of_origin', models.CharField(blank=True, choices=[('Abia_State(Umuahia)', 'Abia_State(Umuahia)'), ('Adamawa_State(Yola)', 'Adamawa_State(Yola)'), ('Akwa_Ibom_State(Uyo)', 'Akwa_Ibom_State(Uyo)'), ('Anambra_State(Awka)', 'Anambra_State(Awka)'), ('Bauchi_State(Bauchi)', 'Bauchi_State(Bauchi)'), ('Bayelsa_State(Yenagoa)', 'Bayelsa_State(Yenagoa)'), ('Benue_State(Makurdi)', 'Benue_State(Makurdi)'), ('Borno_State(Maiduguri)', 'Borno_State(Maiduguri)'), ('Cross_River_State(Calabar)', 'Cross_River_State(Calabar)'), ('Delta_State(Asaba)', 'Delta_State(Asaba)'), ('Ebonyi_State(Abakaliki)', 'Ebonyi_State(Abakaliki)'), ('Edo_State(Benin City)', 'Edo_State(Benin City)'), ('Ekiti_State(Ado Ekiti)', 'Ekiti_State(Ado Ekiti)'), ('Enugu_State(Enugu)', 'Enugu_State(Enugu)'), ('Gombe_State(Gombe)', 'Gombe_State(Gombe)'), ('Imo_State(Owerri)', 'Imo_State(Owerri)'), ('Jigawa_State(Dutse)', 'Jigawa_State(Dutse)'), ('Kaduna_State(Kaduna)', 'Kaduna_State(Kaduna)'), ('Kano_State(Kano)', 'Kano_State(Kano)'), ('Katsina_State(Katsina)', 'Katsina_State(Katsina)'), ('Kebbi_State(Birnin Kebbi)', 'Kebbi_State(Birnin Kebbi)'), ('Kogi_State(Lokoja)', 'Kogi_State(Lokoja)'), ('Kwara_State(Ilorin)', 'Kwara_State(Ilorin)'), ('Lagos_State(Ikeja)', 'Lagos_State(Ikeja)'), ('Nasarawa_State(Lafia)', 'Nasarawa_State(Lafia)'), ('Niger_State(Minna)', 'Niger_State(Minna)'), ('Ogun_State(Abeokuta)', 'Ogun_State(Abeokuta)'), ('Ondo_State(Akure)', 'Ondo_State(Akure)'), ('Osun_State(Oshogbo)', 'Osun_State(Oshogbo)'), ('Oyo_State(Ibadan)', 'Oyo_State(Ibadan)'), ('Plateau_State(Jos)', 'Plateau_State(Jos)'), ('Rivers_State(Port_Harcourt)', 'Rivers_State(Port_Harcourt)'), ('Sokoto_State(Sokoto)', 'Sokoto_State(Sokoto)'), ('Taraba_State(Jalingo)', 'Taraba_State(Jalingo)'), ('Yobe_State(Damaturu)', 'Yobe_State(Damaturu)'), ('Zamfara_State(Gusau)', 'Zamfara_State(Gusau)')], max_length=200, null=True)),
                ('pvc_collected', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=200, null=True)),
            ],
        ),
    ]
