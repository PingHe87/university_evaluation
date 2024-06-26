# Generated by Django 4.2.11 on 2024-04-10 20:42

from django.db import migrations, models # type: ignore
import django.db.models.deletion # type: ignore


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "course_number",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Degree",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("level", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name_plural": "Degrees",
                "unique_together": {("name", "level")},
            },
        ),
        migrations.CreateModel(
            name="Instructor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="LearningObjective",
            fields=[
                (
                    "code",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                ("semester", models.CharField(max_length=50)),
                ("section_number", models.IntegerField()),
                ("enrollment_count", models.IntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university_evaluation.course",
                    ),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university_evaluation.instructor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Evaluation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assessment_method", models.CharField(max_length=255)),
                ("performance_A", models.IntegerField()),
                ("performance_B", models.IntegerField()),
                ("performance_C", models.IntegerField()),
                ("performance_F", models.IntegerField()),
                ("improvement_suggestions", models.TextField()),
                (
                    "objective",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university_evaluation.learningobjective",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university_evaluation.section",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DegreeCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_core", models.BooleanField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university_evaluation.course",
                    ),
                ),
                (
                    "degree",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university_evaluation.degree",
                    ),
                ),
            ],
            options={"unique_together": {("degree", "course")},},
        ),
        migrations.CreateModel(
            name="CourseObjective",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university_evaluation.course",
                    ),
                ),
                (
                    "objective",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university_evaluation.learningobjective",
                    ),
                ),
            ],
            options={"unique_together": {("course", "objective")},},
        ),
    ]
