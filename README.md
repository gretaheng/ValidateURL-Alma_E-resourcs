# ValidateURL-Alma_E-resourcs

Due to changes of vendors, the links of e-resources may change as well. Some changes like server and domain change may make the old URLs not accessible. However, Alma does not have a URL validation job. While it has a export URLs job, the URLs exported may not be the portfolio link. Although vendor may provide MARC records with updated URLs, when import existing records to Alma, only bib records will be updated, not the portfolio information. For records with PO line associated or local fields and course reserve titles, deleting and re-importing should not be performed  just to update the portfolio URLs. 

The best way we have found is to check URLs collection by collection. This makes sense to us as one collection is usually come from the same vendor and the URL address should have the same "prefix." We use MARCEDIT and OpenRefine to extract only 020 and 856 fields from the vendor provided MARC record. Then, match the link in the MARC with the URLs in the collection portfolio list using ISBN. Then update the portfolios using porfolio loader. 

Details about how to use this python script to update URLs can be found here: https://libguides.sdsu.edu/ebook/erm/urls
