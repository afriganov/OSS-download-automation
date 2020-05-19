# OSS-automation
Web browser manipulation scripts for automation of OSS.

OSSGML input is parcel number list in .txt and (output) is used for downloading .gml files from OSS. Script runs on logged in/private oss site while OSSKAT and OSSZK run on public oss site.

OSSKAT input is possesion sheet number list in .txt. Script iterates through PSnumbers and download .pdf files for each of them.

OSSZK works on same principle for land registry.

The process itself can be further automated using 3rd party captcha solvers instead of using user inputed captcha, although this method is significantly faster already then normal web browser clicking.

Web driver documentation and tutorial can be found on https://www.selenium.dev/documentation/en/webdriver/

Although it makes no sense at first occasional .sleep() had to be implemented for scripts to run smoothly and not bug randomly.
