from django.db import models

class IPO(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    price_band = models.CharField(max_length=50)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.CharField(max_length=100)
    listing_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2)
    rhp_pdf = models.FileField(upload_to='pdfs/')
    drhp_pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.company_name