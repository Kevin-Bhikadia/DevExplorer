# Generated by Django 4.1 on 2022-09-05 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_tag_project_vote_ratio_project_vote_total_review_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project", old_name="desciption", new_name="description",
        ),
    ]