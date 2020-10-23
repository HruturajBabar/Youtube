# Generated by Django 3.0.6 on 2020-10-22 13:02

from django.db import migrations, models
import youtube.models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0004_actor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('genre', models.CharField(max_length=30)),
                ('year', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=youtube.models.Movie.current_year, verbose_name='year')),
            ],
        ),
    ]
