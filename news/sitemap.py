from django.contrib import sitemaps

class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return self.objects.all()

class NewsCatagorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return self.objects.all()
