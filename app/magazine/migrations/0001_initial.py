# Generated by Django 3.2.12 on 2022-03-21 08:46

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.images.blocks
from django.db import migrations, models

import blocks.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0023_add_choose_permissions"),
        ("wagtailcore", "0066_collection_management_permissions"),
        ("taggit", "0004_alter_taggeditem_content_type_alter_taggeditem_tag"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArchiveArticle",
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
                ("title", models.CharField(max_length=255)),
                (
                    "toc_page_number",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Page number as it appears the original document",
                        null=True,
                    ),
                ),
                (
                    "pdf_page_number",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Page in the actual PDF file, when it differs from the original document",
                        null=True,
                    ),
                ),
                ("drupal_node_id", models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ArchiveIssue",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "publication_date",
                    models.DateField(
                        help_text="Please select the first day of the publication month",
                        null=True,
                    ),
                ),
                (
                    "internet_archive_identifier",
                    models.CharField(
                        db_index=True,
                        help_text="Identifier for Internet Archive item.",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "western_friend_volume",
                    models.CharField(
                        blank=True,
                        help_text="Related Western Friend volume.",
                        max_length=255,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="DeepArchiveIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MagazineArticle",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "teaser",
                    wagtail.fields.RichTextField(
                        blank=True,
                        help_text="Try to keep teaser to a couple dozen words.",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(),
                            ),
                            (
                                "heading",
                                wagtail.blocks.CharBlock(form_classname="full title"),
                            ),
                            (
                                "image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "width",
                                            wagtail.blocks.IntegerBlock(
                                                help_text="Enter the desired image width value in pixels up to 800 max.",
                                                max_value=800,
                                                min_value=0,
                                            ),
                                        ),
                                    ],
                                    classname="full title",
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail.blocks.RichTextBlock(
                                    features=[
                                        "h2",
                                        "h3",
                                        "h4",
                                        "bold",
                                        "italic",
                                        "ol",
                                        "ul",
                                        "hr",
                                        "link",
                                        "document-link",
                                        "image",
                                        "superscript",
                                        "superscript",
                                        "strikethrough",
                                        "blockquote",
                                    ]
                                ),
                            ),
                            ("pullquote", blocks.blocks.PullQuoteBlock()),
                        ]
                    ),
                ),
                (
                    "is_featured",
                    models.BooleanField(
                        default=False,
                        help_text="Feature this article in the related issue and allow full access without a subscription?",
                    ),
                ),
                (
                    "body_migrated",
                    models.TextField(
                        blank=True,
                        help_text="Used only for content from old Drupal website.",
                        null=True,
                    ),
                ),
                ("drupal_node_id", models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MagazineDepartment",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MagazineDepartmentIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MagazineTagIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MagazineIssue",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "publication_date",
                    models.DateField(
                        help_text="Please select the first day of the publication month",
                        null=True,
                    ),
                ),
                ("issue_number", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "cover_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MagazineIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
                ("deep_archive_intro", wagtail.fields.RichTextField(blank=True)),
                (
                    "deep_archive_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="magazine.deeparchiveindexpage",
                    ),
                ),
                (
                    "featured_deep_archive_issue",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="magazine.archiveissue",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="MagazineArticleTag",
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
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="magazine.magazinearticle",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="magazine_magazinearticletag_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MagazineArticleAuthor",
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
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "article",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="authors",
                        to="magazine.magazinearticle",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles_authored",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="magazinearticle",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="articles",
                to="magazine.magazinedepartment",
            ),
        ),
        migrations.AddField(
            model_name="magazinearticle",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="magazine.MagazineArticleTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.CreateModel(
            name="ArchiveArticleAuthor",
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
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "article",
                    modelcluster.fields.ParentalKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="archive_authors",
                        to="magazine.archivearticle",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="archive_articles_authored",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="archivearticle",
            name="issue",
            field=modelcluster.fields.ParentalKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="archive_articles",
                to="magazine.archiveissue",
            ),
        ),
    ]
