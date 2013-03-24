# -*- coding: utf-8 -*-
from rollyourown import seo


class Metadata(seo.Metadata):
    title = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords = seo.KeywordTag()

    class Meta:
        use_sites = True
        use_cache = True
        use_i18n = True
        backends = ('path',)
        verbose_name = "SEO Meta-tag"
        verbose_name_plural = "SEO Meta-tags"