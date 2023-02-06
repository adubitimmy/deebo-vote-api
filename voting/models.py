from django.db import models

# Create your models here.
class Candidates(models.Model):
    candidates_name = models.CharField(verbose_name="Candidate's name", max_length = 200, blank=True, null=True)
    manifesto = models.TextField()
    portfolio = models.TextField()
    
    def __str__(self):
        return self.candidates_name
    
    
class Vote(models.Model):
    nationality_options = (
        ("nigeria", "nigeria"),
        ("choose_nationality", "choose_nationality")
    )
    nationality = models.CharField(
        max_length=200,
        choices=nationality_options,
        default="choose_nationality"
    )
    location_options = (
        ("in_nigeria", "in_nigeria"),
        ("nigeria_diasppora", "nigeria_diasppora")
    )
    location = models.CharField(
        max_length=200,
        choices=location_options,
        blank=True,
        null=True
    )
    state_options = (
        ("Abia_State(Umuahia)","Abia_State(Umuahia)"),
        ("Adamawa_State(Yola)","Adamawa_State(Yola)"),
        ("Akwa_Ibom_State(Uyo)","Akwa_Ibom_State(Uyo)"),
        ("Anambra_State(Awka)","Anambra_State(Awka)"),
        ("Bauchi_State(Bauchi)","Bauchi_State(Bauchi)"),
        ("Bayelsa_State(Yenagoa)","Bayelsa_State(Yenagoa)"),
        ("Benue_State(Makurdi)","Benue_State(Makurdi)"),
        ("Borno_State(Maiduguri)","Borno_State(Maiduguri)"),
        ("Cross_River_State(Calabar)","Cross_River_State(Calabar)"),
        ("Delta_State(Asaba)","Delta_State(Asaba)"),
        ("Ebonyi_State(Abakaliki)","Ebonyi_State(Abakaliki)"),
        ("Edo_State(Benin City)","Edo_State(Benin City)"),
        ("Ekiti_State(Ado Ekiti)","Ekiti_State(Ado Ekiti)"),
        ("Enugu_State(Enugu)","Enugu_State(Enugu)"),
        ("Gombe_State(Gombe)","Gombe_State(Gombe)"),
        ("Imo_State(Owerri)","Imo_State(Owerri)"),
        ("Jigawa_State(Dutse)","Jigawa_State(Dutse)"),
        ("Kaduna_State(Kaduna)","Kaduna_State(Kaduna)"),
        ("Kano_State(Kano)","Kano_State(Kano)"),
        ("Katsina_State(Katsina)","Katsina_State(Katsina)"),
        ("Kebbi_State(Birnin Kebbi)","Kebbi_State(Birnin Kebbi)"),
        ("Kogi_State(Lokoja)","Kogi_State(Lokoja)"),
        ("Kwara_State(Ilorin)","Kwara_State(Ilorin)"),
        ("Lagos_State(Ikeja)","Lagos_State(Ikeja)"),
        ("Nasarawa_State(Lafia)","Nasarawa_State(Lafia)"),
        ("Niger_State(Minna)","Niger_State(Minna)"),
        ("Ogun_State(Abeokuta)","Ogun_State(Abeokuta)"),
        ("Ondo_State(Akure)","Ondo_State(Akure)"),
        ("Osun_State(Oshogbo)","Osun_State(Oshogbo)"),
        ("Oyo_State(Ibadan)","Oyo_State(Ibadan)"),
        ("Plateau_State(Jos)","Plateau_State(Jos)"),
        ("Rivers_State(Port_Harcourt)","Rivers_State(Port_Harcourt)"),
        ("Sokoto_State(Sokoto)","Sokoto_State(Sokoto)"),
        ("Taraba_State(Jalingo)","Taraba_State(Jalingo)"),
        ("Yobe_State(Damaturu)","Yobe_State(Damaturu)"),
        ("Zamfara_State(Gusau)","Zamfara_State(Gusau)")
    )
    state_of_origin = models.CharField(
        max_length=200,
        choices=state_options,
        blank=True,
        null=True
    )
    pvc_options = (
        ("yes","yes"),
        ("no","no")
    )
    pvc_collected = models.CharField(
        max_length=200,
        choices=pvc_options,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.location
    
class RequestForm(models.Model):
    poll_category = models.CharField(max_length=200)
    poll_title = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True, null=True)
    additional_information = models.TextField()
    
    def __str__(self):
        return self.full_name
    
    
 