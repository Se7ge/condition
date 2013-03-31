# -*- coding: utf-8 -*-
from rollyourown import seo


class SEOMetadata(seo.Metadata):
    title = seo.Tag(head=True)
    keywords = seo.MetaTag()
    description = seo.MetaTag()

    class Meta:
        use_cache = False