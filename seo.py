# -*- coding: utf-8 -*-
from rollyourown import seo


class SEOMetadata(seo.Metadata):
    title = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords = seo.KeywordTag()

    class Meta:
        backends = ('path',)
        verbose_name = "SEO Meta-tag"
        verbose_name_plural = "SEO Meta-tags"