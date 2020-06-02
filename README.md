# economic_times_daywise_scrapper_zecide
# each section has several sub-sections, and 16 articles are extracted from each sub-section


#to scrape subsections individually:

scrapy crawl et_all_banking_article -o et_industry_auto.json

scrapy crawl et_all_industry_article -o et_industry_banking_and_finance.json

scrapy crawl et_all_cons_product_article -o et_industry_cons_product.json

scrapy crawl et_all_energy_article -o et_industry_energy.json

scrapy crawl et_all_indl_goods_and_services_article -o et_industry_goods_and_services.json

scrapy crawl et_all_healthcare_and_biotech_article -o et_industry_healthcare_and_biotech.json

scrapy crawl et_all_services_article -o et_industry_services.json

scrapy crawl et_all_media_and_entertainment_article -o et_industry_media_and_entertainment.json

scrapy crawl et_all_transportation_article -o et_industry_transportation.json

scrapy crawl et_all_tech_article -o et_industry_tech.json

scrapy crawl et_all_telecom_article -o et_industry_telecom.json

scrapy crawl et_all_miscellaneous_article -o et_industry_miscellaneous.json

scrapy crawl et_all_environment_article -o et_industry_environment.json



# to srape all subsections at once

scrapy crawl et_all_banking_article -o et_industry_auto.json; scrapy crawl et_all_industry_article -o et_industry_banking_and_finance.json; scrapy crawl et_all_cons_product_article -o et_industry_cons_product.json; scrapy crawl et_all_energy_article -o et_industry_energy.json; scrapy crawl et_all_indl_goods_and_services_article -o et_industry_goods_and_services.json; scrapy crawl et_all_healthcare_and_biotech_article -o et_industry_healthcare_and_biotech.json; scrapy crawl et_all_services_article -o et_industry_services.json; scrapy crawl et_all_media_and_entertainment_article -o et_industry_media_and_entertainment.json; scrapy crawl et_all_transportation_article -o et_industry_transportation.json; scrapy crawl et_all_tech_article -o et_industry_tech.json; scrapy crawl et_all_telecom_article -o et_industry_telecom.json; scrapy crawl et_all_miscellaneous_article -o et_industry_miscellaneous.json; scrapy crawl et_all_environment_article -o et_industry_environment.json
