import requests
from time import sleep

# We got these ids from this web page:
# http://www.tbs-sct.gc.ca/pol/hierarch-eng.aspx
# and then used the following code in the Chrome Dev tools to find everything
# with a class of "tv-in" and extract the query params from the URL:
# console.log(JSON.stringify(Array.from(document.querySelectorAll('.tv-in')).map(a => new URL(a.href).search.split('=')[1])))
ids = ["25049","13616","27122","12022","12025","14494","28230","28107","14676","12038","18225","17660","12062","12063","12064","28105","12065","28288","14671","13872","12066","12074","18229","21252","28190","27807","21261","28001","27421","25576","12042","12044","12045","17316","27419","17562","24834","25595","12056","12047","25868","12043","30683","30682","12315","27167","12315","27167","12084","12522","12120","12111","14220","13589","12139","13848","13951","12129","13583","12133","12116","12588","13953","13954","15771","15774","15773","15772","21104","12135","12552","12553","13856","12135","12552","12553","12141","13593","12143","17151","25178","32495","32499","20886","12182","20888","20885","32502","25593","27256","32503","27260","32504","17068","17065","19018","27177","25600","32505","17067","17066","19024","15796","27228","28203","12364","12169","14265","16578","16577","26776","26262","30678","16579","12324","12331","12328","12329","12323","20008","12332","12333","20010","28115","12452","12453","18310","12360","12742","18910","27600","16553","12754","16557","18909","28108","16552","18910","18909","25875","12755","15249","25687","26295","12328","27088","17251","17253","17260","15746","17280","17281","17282","17283","17285","17284","15260","23601","24227","25875","12510","26761","26154","18308","18309","18311","13342","13720","16484","32533","13607","19134","28697","28698","28699","28700","22370","12541","12542","12543","12572","14218","14219","13628","13877","14220","14226","27146","22379","26041","26040","12552","12553","12405","12409","12407","13937","12560","12562","13661","12563","13662","12561","12561","13605","26160","26163","26164","26168","12358","27146","12607","27987","12582","12559","12584","13890","12583","12614","12612","31300","32556","31306","27916","25748","25761","28422","25750","19422","20930"]

for id in ids:
    # the original url: http://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=27122&section=xml
    response = requests.get("http://www.tbs-sct.gc.ca/pol/doc-eng.aspx", 
            params = {"id": id, "section": "xml"}, stream=True)
    print(response.url)
    with open("individual_policy_documents2/" + "policy_" + id + ".xml" , 'wb') as fd:
        for chunk in response.iter_content(chunk_size=128): # Write the chunks of the response into a file
            fd.write(chunk)
    sleep(1) # We'll be polite and have a brief pause between requests
