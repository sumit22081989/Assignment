from PageObjects.BrokenLink import BrokenLinks
import pytest
import requests


def FindBrokenLink(self, setup):
    self.bl = BrokenLinks(setup)
    links = self.bl.getImages()
    i=0
    dictLinks={}
    for link in links:
        req = requests.get(link)
        dictLinks.update({link: req.status_code})
    print(dictLinks)
    brokenLinkCount = [i for i in dictLinks.values() if i != 200]
    if len(brokenLinkCount) == 0:
        return True
    else:
        return False