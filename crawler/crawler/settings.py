BOT_NAME = "crawler"
SPIDER_MODULES = ["crawler.spiders"]
NEWSPIDER_MODULE = "crawler.spiders"
DOWNLOAD_HANDLERS = {
  "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
  "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_BROWSER_TYPE = "chromium"
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 8
ITEM_PIPELINES = {}
FEEDS = {"output.json": {"format": "json", "overwrite": True}}
